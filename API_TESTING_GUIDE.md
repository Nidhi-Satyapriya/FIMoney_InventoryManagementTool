# FIMoney Inventory Management API - Complete Testing Guide
# Generated using AI

## 🚀 Quick Start

### Base URL
```
http://localhost:8000/api/v1
```

### Authentication
All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## 📋 API Endpoints Testing

### 1. User Registration
**Endpoint:** `POST /register`

**Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
    "username": "testuser",
    "password": "testpassword123"
}
```

**Expected Response (201):**
```json
{
    "username": "testuser",
    "id": "507f1f77bcf86cd799439011"
}
```

**Test Cases:**
- ✅ Valid registration
- ❌ Duplicate username (409 Conflict)
- ❌ Missing username (422 Validation Error)
- ❌ Missing password (422 Validation Error)

---

### 2. User Login
**Endpoint:** `POST /login`

**Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
    "username": "testuser",
    "password": "testpassword123"
}
```

**Expected Response (200):**
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTYzNzI5NjAwMH0.example",
    "token_type": "bearer"
}
```

**Test Cases:**
- ✅ Valid credentials
- ❌ Invalid username (401 Unauthorized)
- ❌ Invalid password (401 Unauthorized)
- ❌ Missing credentials (422 Validation Error)

---

### 3. Add Product (Protected)
**Endpoint:** `POST /products`

**Headers:**
```
Content-Type: application/json
Authorization: Bearer YOUR_JWT_TOKEN
```

**Request Body:**
```json
{
    "name": "Gaming Laptop",
    "type": "Electronics",
    "sku": "LAP001",
    "quantity": 10,
    "price": 1299.99,
    "description": "High-performance gaming laptop with RTX 4060",
    "image_url": "https://example.com/laptop.jpg"
}
```

**Expected Response (201):**
```json
{
    "product_id": "507f1f77bcf86cd799439012",
    "message": "Product added successfully"
}
```

**Test Cases:**
- ✅ Valid product data
- ❌ Missing required fields (422 Validation Error)
- ❌ Invalid price (negative or zero)
- ❌ Invalid quantity (negative)
- ❌ Missing authentication (401 Unauthorized)

---

### 4. Get Products with Pagination (Protected)
**Endpoint:** `GET /products`

**Headers:**
```
Authorization: Bearer YOUR_JWT_TOKEN
```

**Query Parameters:**
- `skip`: Number of products to skip (default: 0, min: 0)
- `limit`: Number of products per page (default: 10, min: 1, max: 100)

**Example Requests:**
```
GET /products                    # First page, 10 items
GET /products?skip=0&limit=5     # First page, 5 items
GET /products?skip=10&limit=10   # Second page, 10 items
GET /products?skip=20&limit=5    # Fifth page, 5 items
```

**Expected Response (200):**
```json
{
    "products": [
        {
            "id": "507f1f77bcf86cd799439012",
            "name": "Gaming Laptop",
            "type": "Electronics",
            "sku": "LAP001",
            "quantity": 10,
            "price": 1299.99,
            "description": "High-performance gaming laptop with RTX 4060",
            "image_url": "https://example.com/laptop.jpg"
        },
        {
            "id": "507f1f77bcf86cd799439013",
            "name": "Wireless Mouse",
            "type": "Accessories",
            "sku": "MOU001",
            "quantity": 50,
            "price": 29.99,
            "description": "Ergonomic wireless mouse",
            "image_url": "https://example.com/mouse.jpg"
        }
    ],
    "pagination": {
        "total": 25,
        "page": 1,
        "per_page": 10,
        "total_pages": 3,
        "has_next": true,
        "has_prev": false,
        "next_page": 2,
        "prev_page": null
    }
}
```

**Test Cases:**
- ✅ First page (skip=0, limit=10)
- ✅ Second page (skip=10, limit=10)
- ✅ Custom page size (skip=0, limit=5)
- ✅ Last page
- ✅ Empty page (skip=100, limit=10)
- ❌ Invalid skip (negative)
- ❌ Invalid limit (0 or >100)
- ❌ Missing authentication (401 Unauthorized)

---

### 5. Update Product Quantity (Protected)
**Endpoint:** `PUT /products/{product_id}/quantity`

**Headers:**
```
Content-Type: application/json
Authorization: Bearer YOUR_JWT_TOKEN
```

**Request Body:**
```json
{
    "quantity": 15
}
```

**Expected Response (200):**
```json
{
    "id": "507f1f77bcf86cd799439012",
    "name": "Gaming Laptop",
    "type": "Electronics",
    "sku": "LAP001",
    "quantity": 15,
    "price": 1299.99,
    "description": "High-performance gaming laptop with RTX 4060",
    "image_url": "https://example.com/laptop.jpg"
}
```

**Test Cases:**
- ✅ Valid quantity update
- ❌ Product not found (404 Not Found)
- ❌ Invalid quantity (negative)
- ❌ Missing authentication (401 Unauthorized)
- ❌ Invalid product ID format

---

## 🧪 Complete Testing Workflow

### Step 1: Start Backend
```bash
cd FIMoney_InventoryManagementTool
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 2: Test Authentication Flow
1. **Register User**
   ```bash
   curl -X POST "http://localhost:8000/api/v1/register" \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "password": "testpassword123"}'
   ```

2. **Login User**
   ```bash
   curl -X POST "http://localhost:8000/api/v1/login" \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "password": "testpassword123"}'
   ```

3. **Save the JWT token** from the login response

### Step 3: Test Product Operations
1. **Add Multiple Products**
   ```bash
   # Add first product
   curl -X POST "http://localhost:8000/api/v1/products" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_JWT_TOKEN" \
        -d '{
          "name": "Gaming Laptop",
          "type": "Electronics",
          "sku": "LAP001",
          "quantity": 10,
          "price": 1299.99,
          "description": "High-performance gaming laptop",
          "image_url": "https://example.com/laptop.jpg"
        }'

   # Add second product
   curl -X POST "http://localhost:8000/api/v1/products" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_JWT_TOKEN" \
        -d '{
          "name": "Wireless Mouse",
          "type": "Accessories",
          "sku": "MOU001",
          "quantity": 50,
          "price": 29.99,
          "description": "Ergonomic wireless mouse",
          "image_url": "https://example.com/mouse.jpg"
        }'
   ```

2. **Test Pagination**
   ```bash
   # Get first page (5 items)
   curl -X GET "http://localhost:8000/api/v1/products?skip=0&limit=5" \
        -H "Authorization: Bearer YOUR_JWT_TOKEN"

   # Get second page (5 items)
   curl -X GET "http://localhost:8000/api/v1/products?skip=5&limit=5" \
        -H "Authorization: Bearer YOUR_JWT_TOKEN"
   ```

3. **Update Product Quantity**
   ```bash
   curl -X PUT "http://localhost:8000/api/v1/products/PRODUCT_ID_HERE/quantity" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_JWT_TOKEN" \
        -d '{"quantity": 15}'
   ```

---

## 📊 Postman Collection

### Import this complete collection:

```json
{
    "info": {
        "name": "FIMoney Inventory API - Complete",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "variable": [
        {
            "key": "base_url",
            "value": "http://localhost:8000/api/v1"
        },
        {
            "key": "token",
            "value": ""
        }
    ],
    "item": [
        {
            "name": "1. Authentication",
            "item": [
                {
                    "name": "Register User",
                    "request": {
                        "method": "POST",
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "application/json"
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": "{\n    \"username\": \"testuser\",\n    \"password\": \"testpassword123\"\n}"
                        },
                        "url": {
                            "raw": "{{base_url}}/register",
                            "host": ["{{base_url}}"],
                            "path": ["register"]
                        }
                    }
                },
                {
                    "name": "Login User",
                    "event": [
                        {
                            "listen": "test",
                            "script": {
                                "exec": [
                                    "if (pm.response.code === 200) {",
                                    "    const response = pm.response.json();",
                                    "    pm.collectionVariables.set('token', response.access_token);",
                                    "    console.log('Token saved:', response.access_token);",
                                    "}"
                                ]
                            }
                        }
                    ],
                    "request": {
                        "method": "POST",
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "application/json"
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": "{\n    \"username\": \"testuser\",\n    \"password\": \"testpassword123\"\n}"
                        },
                        "url": {
                            "raw": "{{base_url}}/login",
                            "host": ["{{base_url}}"],
                            "path": ["login"]
                        }
                    }
                }
            ]
        },
        {
            "name": "2. Products",
            "item": [
                {
                    "name": "Add Product 1",
                    "request": {
                        "method": "POST",
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "application/json"
                            },
                            {
                                "key": "Authorization",
                                "value": "Bearer {{token}}"
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": "{\n    \"name\": \"Gaming Laptop\",\n    \"type\": \"Electronics\",\n    \"sku\": \"LAP001\",\n    \"quantity\": 10,\n    \"price\": 1299.99,\n    \"description\": \"High-performance gaming laptop\",\n    \"image_url\": \"https://example.com/laptop.jpg\"\n}"
                        },
                        "url": {
                            "raw": "{{base_url}}/products",
                            "host": ["{{base_url}}"],
                            "path": ["products"]
                        }
                    }
                },
                {
                    "name": "Add Product 2",
                    "request": {
                        "method": "POST",
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "application/json"
                            },
                            {
                                "key": "Authorization",
                                "value": "Bearer {{token}}"
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": "{\n    \"name\": \"Wireless Mouse\",\n    \"type\": \"Accessories\",\n    \"sku\": \"MOU001\",\n    \"quantity\": 50,\n    \"price\": 29.99,\n    \"description\": \"Ergonomic wireless mouse\",\n    \"image_url\": \"https://example.com/mouse.jpg\"\n}"
                        },
                        "url": {
                            "raw": "{{base_url}}/products",
                            "host": ["{{base_url}}"],
                            "path": ["products"]
                        }
                    }
                },
                {
                    "name": "Get Products - Page 1",
                    "request": {
                        "method": "GET",
                        "header": [
                            {
                                "key": "Authorization",
                                "value": "Bearer {{token}}"
                            }
                        ],
                        "url": {
                            "raw": "{{base_url}}/products?skip=0&limit=5",
                            "host": ["{{base_url}}"],
                            "path": ["products"],
                            "query": [
                                {
                                    "key": "skip",
                                    "value": "0"
                                },
                                {
                                    "key": "limit",
                                    "value": "5"
                                }
                            ]
                        }
                    }
                },
                {
                    "name": "Get Products - Page 2",
                    "request": {
                        "method": "GET",
                        "header": [
                            {
                                "key": "Authorization",
                                "value": "Bearer {{token}}"
                            }
                        ],
                        "url": {
                            "raw": "{{base_url}}/products?skip=5&limit=5",
                            "host": ["{{base_url}}"],
                            "path": ["products"],
                            "query": [
                                {
                                    "key": "skip",
                                    "value": "5"
                                },
                                {
                                    "key": "limit",
                                    "value": "5"
                                }
                            ]
                        }
                    }
                },
                {
                    "name": "Update Product Quantity",
                    "request": {
                        "method": "PUT",
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "application/json"
                            },
                            {
                                "key": "Authorization",
                                "value": "Bearer {{token}}"
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": "{\n    \"quantity\": 15\n}"
                        },
                        "url": {
                            "raw": "{{base_url}}/products/PRODUCT_ID_HERE/quantity",
                            "host": ["{{base_url}}"],
                            "path": ["products", "PRODUCT_ID_HERE", "quantity"]
                        }
                    }
                }
            ]
        }
    ]
}
```

---

## 🎯 Success Criteria

### ✅ All endpoints working:
1. **Register** - Creates new user
2. **Login** - Returns JWT token
3. **Add Product** - Creates new product
4. **Get Products** - Returns paginated list with metadata
5. **Update Quantity** - Updates product quantity

### ✅ Pagination working:
- Correct total count
- Proper page calculation
- Next/previous page indicators
- Configurable page size (1-100)
- Skip/limit parameters

### ✅ Error handling:
- 401 for missing/invalid tokens
- 404 for not found resources
- 422 for validation errors
- 409 for conflicts

---

## 🔍 Testing Tips

1. **Start with authentication** - Register and login first
2. **Save the JWT token** - Use it for all protected endpoints
3. **Test pagination** - Add multiple products to see pagination in action
4. **Check response structure** - Verify all fields are present
5. **Test error cases** - Try invalid data to ensure proper error handling

---

**Happy Testing! 🚀** 