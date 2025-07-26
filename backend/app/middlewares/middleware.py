import time
import logging
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Callable
import json
from datetime import datetime

# Initialized middleware for admin portal

#  AI suggested codes for the desired functionalities:-

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoggingMiddleware:
    """Middleware for logging all requests and responses"""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            start_time = time.time()
            
            # Log request
            logger.info(f"Request: {scope['method']} {scope['path']}")
            
            # Create custom send function to log response
            async def custom_send(message):
                if message["type"] == "http.response.start":
                    process_time = time.time() - start_time
                    logger.info(f"Response: {scope['method']} {scope['path']} - {message['status']} - {process_time:.4f}s")
                await send(message)
            
            await self.app(scope, receive, custom_send)
        else:
            await self.app(scope, receive, send)

class AdminAuthMiddleware:
    """Middleware for admin-only route protection"""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            # Check if route requires admin access
            path = scope["path"]
            if path.startswith("/api/v1/admin"):
                # This will be handled by the admin dependency in routes
                pass
        
        await self.app(scope, receive, send)

class ErrorHandlingMiddleware:
    """Middleware for centralized error handling"""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            try:
                await self.app(scope, receive, send)
            except Exception as exc:
                logger.error(f"Unhandled exception: {exc}")
                
                # Create error response
                error_response = {
                    "error": "Internal server error",
                    "message": str(exc),
                    "timestamp": datetime.utcnow().isoformat()
                }
                
                # Send error response
                await send({
                    "type": "http.response.start",
                    "status": 500,
                    "headers": [
                        (b"content-type", b"application/json"),
                    ]
                })
                
                await send({
                    "type": "http.response.body",
                    "body": json.dumps(error_response).encode()
                })
        else:
            await self.app(scope, receive, send)

class RateLimitingMiddleware:
    """Basic rate limiting middleware"""
    
    def __init__(self, app, requests_per_minute=60):
        self.app = app
        self.requests_per_minute = requests_per_minute
        self.requests = {}
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            # Get client IP (simplified)
            client_ip = scope.get("client", ("unknown",))[0]
            current_time = time.time()
            
            # Clean old requests
            if client_ip in self.requests:
                self.requests[client_ip] = [
                    req_time for req_time in self.requests[client_ip]
                    if current_time - req_time < 60
                ]
            else:
                self.requests[client_ip] = []
            
            # Check rate limit
            if len(self.requests[client_ip]) >= self.requests_per_minute:
                await send({
                    "type": "http.response.start",
                    "status": 429,
                    "headers": [
                        (b"content-type", b"application/json"),
                    ]
                })
                
                await send({
                    "type": "http.response.body",
                    "body": json.dumps({
                        "error": "Rate limit exceeded",
                        "message": "Too many requests. Please try again later."
                    }).encode()
                })
                return
            
            # Add current request
            self.requests[client_ip].append(current_time)
        
        await self.app(scope, receive, send)

# Utility functions for middleware
def get_client_ip(request: Request) -> str:
    """Extract client IP from request"""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0]
    return request.client.host if request.client else "unknown"

def log_request_details(request: Request, response_time: float = None):
    """Log detailed request information"""
    log_data = {
        "method": request.method,
        "url": str(request.url),
        "client_ip": get_client_ip(request),
        "user_agent": request.headers.get("user-agent"),
        "response_time": response_time
    }
    logger.info(f"Request details: {json.dumps(log_data)}") 