"""
Comprehensive API Testing Script for FIMoney Inventory Management
Tests all endpoints including the new pagination feature
"""

# Generated using AI

import requests
import json
import time

# API Configuration
BASE_URL = "http://localhost:8000/api/v1"
HEADERS = {"Content-Type": "application/json"}

def print_test_result(test_name, success, response=None, error=None):
    """Print formatted test result"""
    if success:
        print(f"✅ {test_name}")
        if response:
            print(f"   Status: {response.status_code}")
            if response.status_code != 204:
                try:
                    data = response.json()
                    print(f"   Response: {json.dumps(data, indent=2)}")
                except:
                    print(f"   Response: {response.text}")
    else:
        print(f"❌ {test_name}")
        if error:
            print(f"   Error: {error}")
        if response:
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.text}")
    print()

def test_authentication():
    """Test user registration and login"""
    print("🔐 Testing Authentication Endpoints")
    print("=" * 50)
    
    # Test 1: Register User
    register_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/register", json=register_data, headers=HEADERS)
        print_test_result("User Registration", response.status_code == 201, response)
    except Exception as e:
        print_test_result("User Registration", False, error=str(e))
    
    # Test 2: Login User
    login_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data, headers=HEADERS)
        if response.status_code == 200:
            token_data = response.json()
            token = token_data["access_token"]
            print_test_result("User Login", True, response)
            return token
        else:
            print_test_result("User Login", False, response)
            return None
    except Exception as e:
        print_test_result("User Login", False, error=str(e))
        return None

def test_product_operations(token):
    """Test product CRUD operations"""
    print("📦 Testing Product Operations")
    print("=" * 50)
    
    if not token:
        print("❌ No token available, skipping product tests")
        return []
    
    auth_headers = {**HEADERS, "Authorization": f"Bearer {token}"}
    product_ids = []
    
    # Test 3: Add Multiple Products
    products_data = [
        {
            "name": "Gaming Laptop",
            "type": "Electronics",
            "sku": "LAP001",
            "quantity": 10,
            "price": 1299.99,
            "description": "High-performance gaming laptop",
            "image_url": "https://example.com/laptop.jpg"
        },
        {
            "name": "Wireless Mouse",
            "type": "Accessories",
            "sku": "MOU001",
            "quantity": 50,
            "price": 29.99,
            "description": "Ergonomic wireless mouse",
            "image_url": "https://example.com/mouse.jpg"
        },
        {
            "name": "Mechanical Keyboard",
            "type": "Accessories",
            "sku": "KEY001",
            "quantity": 25,
            "price": 89.99,
            "description": "RGB mechanical keyboard",
            "image_url": "https://example.com/keyboard.jpg"
        },
        {
            "name": "4K Monitor",
            "type": "Electronics",
            "sku": "MON001",
            "quantity": 15,
            "price": 399.99,
            "description": "27-inch 4K gaming monitor",
            "image_url": "https://example.com/monitor.jpg"
        },
        {
            "name": "Gaming Headset",
            "type": "Accessories",
            "sku": "HEA001",
            "quantity": 30,
            "price": 79.99,
            "description": "7.1 surround sound headset",
            "image_url": "https://example.com/headset.jpg"
        }
    ]
    
    for i, product_data in enumerate(products_data, 1):
        try:
            response = requests.post(f"{BASE_URL}/products", json=product_data, headers=auth_headers)
            if response.status_code == 201:
                product_response = response.json()
                product_id = product_response["product_id"]
                product_ids.append(product_id)
                print_test_result(f"Add Product {i}: {product_data['name']}", True, response)
            else:
                print_test_result(f"Add Product {i}: {product_data['name']}", False, response)
        except Exception as e:
            print_test_result(f"Add Product {i}: {product_data['name']}", False, error=str(e))
    
    return product_ids

def test_pagination(token):
    """Test pagination functionality"""
    print("📄 Testing Pagination")
    print("=" * 50)
    
    if not token:
        print("❌ No token available, skipping pagination tests")
        return
    
    auth_headers = {"Authorization": f"Bearer {token}"}
    
    # Test 4: Get Products with Pagination
    pagination_tests = [
        {"skip": 0, "limit": 2, "name": "First page (2 items)"},
        {"skip": 2, "limit": 2, "name": "Second page (2 items)"},
        {"skip": 4, "limit": 2, "name": "Third page (2 items)"},
        {"skip": 0, "limit": 5, "name": "All items (5 items)"},
        {"skip": 10, "limit": 5, "name": "Empty page"},
    ]
    
    for test in pagination_tests:
        try:
            url = f"{BASE_URL}/products?skip={test['skip']}&limit={test['limit']}"
            response = requests.get(url, headers=auth_headers)
            
            if response.status_code == 200:
                data = response.json()
                products = data.get("products", [])
                pagination = data.get("pagination", {})
                
                print(f"✅ {test['name']}")
                print(f"   Status: {response.status_code}")
                print(f"   Products returned: {len(products)}")
                print(f"   Pagination: Total={pagination.get('total', 0)}, Page={pagination.get('page', 0)}, Per Page={pagination.get('per_page', 0)}")
                print(f"   Has Next: {pagination.get('has_next', False)}, Has Prev: {pagination.get('has_prev', False)}")
                print()
            else:
                print_test_result(test['name'], False, response)
        except Exception as e:
            print_test_result(test['name'], False, error=str(e))

def test_update_quantity(token, product_ids):
    """Test product quantity updates"""
    print("🔄 Testing Quantity Updates")
    print("=" * 50)
    
    if not token or not product_ids:
        print("❌ No token or products available, skipping update tests")
        return
    
    auth_headers = {**HEADERS, "Authorization": f"Bearer {token}"}
    
    # Test 5: Update Product Quantity
    for i, product_id in enumerate(product_ids[:2], 1):  # Test first 2 products
        try:
            update_data = {"quantity": 15 + i}
            response = requests.put(f"{BASE_URL}/products/{product_id}/quantity", 
                                  json=update_data, headers=auth_headers)
            print_test_result(f"Update Product {i} Quantity", response.status_code == 200, response)
        except Exception as e:
            print_test_result(f"Update Product {i} Quantity", False, error=str(e))

def test_error_cases():
    """Test error handling"""
    print("🚨 Testing Error Cases")
    print("=" * 50)
    
    # Test invalid registration (duplicate username)
    try:
        duplicate_data = {"username": "testuser", "password": "testpassword123"}
        response = requests.post(f"{BASE_URL}/register", json=duplicate_data, headers=HEADERS)
        print_test_result("Duplicate Username Registration", response.status_code == 409, response)
    except Exception as e:
        print_test_result("Duplicate Username Registration", False, error=str(e))
    
    # Test invalid login
    try:
        invalid_login = {"username": "nonexistent", "password": "wrongpassword"}
        response = requests.post(f"{BASE_URL}/login", json=invalid_login, headers=HEADERS)
        print_test_result("Invalid Login", response.status_code == 401, response)
    except Exception as e:
        print_test_result("Invalid Login", False, error=str(e))
    
    # Test protected endpoint without token
    try:
        response = requests.get(f"{BASE_URL}/products", headers=HEADERS)
        print_test_result("Protected Endpoint Without Token", response.status_code == 401, response)
    except Exception as e:
        print_test_result("Protected Endpoint Without Token", False, error=str(e))

def main():
    """Run all tests"""
    print("🧪 FIMoney Inventory Management API - Complete Testing")
    print("=" * 60)
    print(f"🌐 Base URL: {BASE_URL}")
    print("=" * 60)
    
    # Test authentication and get token
    token = test_authentication()
    
    # Test product operations
    product_ids = test_product_operations(token)
    
    # Test pagination
    test_pagination(token)
    
    # Test quantity updates
    test_update_quantity(token, product_ids)
    
    # Test error cases
    test_error_cases()
    
    print("🎉 Testing Complete!")
    print("=" * 60)
    print("📋 Summary:")
    print("   - Authentication endpoints tested")
    print("   - Product CRUD operations tested")
    print("   - Pagination functionality tested")
    print("   - Error handling tested")
    print("=" * 60)

if __name__ == "__main__":
    main() 