#!/usr/bin/env python3
"""
Main entry point for FIMoney Inventory Management Backend
"""

import os
import sys
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the app directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

def main():
    """Start the FastAPI server with production configuration"""
    
    # Get configuration from environment variables
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    print("🚀 Starting FIMoney Inventory Management Backend...")
    print("=" * 50)
    print("📋 Configuration:")
    print(f"   Host: {host}")
    print(f"   Port: {port}")
    print(f"   Debug: {debug}")
    print(f"   MongoDB: {os.getenv('MONGODB_URL', 'mongodb://localhost:27017')}")
    print(f"   Database: {os.getenv('DATABASE_NAME', 'fimoney_inventory')}")
    print("=" * 50)
    
    try:
        # Start the server with appropriate configuration
        uvicorn.run(
            "app.main:app",
            host=host,
            port=port,
            reload=debug,  # Only reload in debug mode
            log_level="info" if debug else "warning"
        )
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 