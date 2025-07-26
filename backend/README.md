# FIMoney Inventory Management Tool - Backend API

A robust, scalable inventory management system built with FastAPI, MongoDB, and JWT authentication. This backend provides a complete REST API for managing products, users, and inventory operations with secure authentication and comprehensive data validation.

# Postman Collection- 
https://www.postman.com/grey-crescent-113665/workspace/fimoney-backend-apis/collection/36707787-41b8e109-c347-407d-b53d-812d131672be?action=share&source=copy-link&creator=36707787

## 🚀 Features

### Core Functionality
- **User Authentication & Authorization**
  - JWT-based authentication system
  - Secure password hashing with bcrypt
  - Protected API endpoints
  - User registration and login

- **Product Management**
  - CRUD operations for products
  - Real-time inventory tracking
  - SKU-based product identification
  - Image URL support for product visualization
  - Comprehensive product metadata

- **Inventory Operations**
  - Quantity updates with validation
  - Stock level monitoring
  - Inventory value calculations
  - Bulk product operations

### Technical Features
- **FastAPI Framework**
  - High-performance async API
  - Automatic API documentation (Swagger/OpenAPI)
  - Built-in data validation with Pydantic
  - Type hints throughout the codebase

- **MongoDB Integration**
  - NoSQL database for flexible data storage
  - Optimized queries and indexing
  - Scalable data architecture

- **Security Features**
  - JWT token-based authentication
  - Password hashing with bcrypt
  - CORS middleware support
  - Input validation and sanitization

## 📋 API Endpoints

### Authentication Endpoints
```
POST /register - User registration
POST /login - User authentication
```

### Product Endpoints (Protected)
```
GET /products - Retrieve all products (with pagination)
POST /products - Add new product
PUT /products/{id}/quantity - Update product quantity
```

### API Response Format
All endpoints return consistent JSON responses with proper HTTP status codes and error handling.

## 🛠️ Technology Stack

- **Framework**: FastAPI (Python 3.8+)
- **Database**: MongoDB
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **Data Validation**: Pydantic
- **HTTP Client**: Uvicorn (ASGI server)

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MongoDB instance (local or cloud)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd FIMoney_InventoryManagementTool
```

### Step 2: Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `.env` file in the root directory:
```env
# Database Configuration
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=fimoney_inventory

# JWT Configuration
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

### Step 5: Database Setup
1. Ensure MongoDB is running on your system
2. The application will automatically create the database and collections on first run

### Step 6: Run the Application
```bash
# Development mode
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🗄️ Database Schema

### Users Collection
```json
{
  "_id": "ObjectId",
  "username": "string (unique)",
  "password": "string (hashed)",
  "created_at": "datetime"
}
```

### Products Collection
```json
{
  "_id": "ObjectId",
  "name": "string",
  "type": "string",
  "sku": "string (unique)",
  "image_url": "string (optional)",
  "description": "string (optional)",
  "quantity": "integer",
  "price": "float",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## 🔐 Authentication Flow

1. **Registration**: User provides username and password
   - Password is hashed using bcrypt
   - User is stored in MongoDB
   - Returns user data (without password)

2. **Login**: User provides credentials
   - Password is verified against stored hash
   - JWT token is generated and returned
   - Token contains user information

3. **Protected Endpoints**: Include JWT token in Authorization header
   - `Authorization: Bearer <token>`
   - Token is validated on each request
   - User context is available in protected routes

## 📊 API Usage Examples

### User Registration
```bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "securepassword123"
  }'
```

### User Login
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "securepassword123"
  }'
```

### Add Product (Protected)
```bash
curl -X POST "http://localhost:8000/products" \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "type": "Electronics",
    "sku": "LAP001",
    "quantity": 10,
    "price": 999.99,
    "description": "High-performance laptop",
    "image_url": "https://example.com/laptop.jpg"
  }'
```

### Get Products (Protected)
```bash
curl -X GET "http://localhost:8000/products?skip=0&limit=10" \
  -H "Authorization: Bearer <your-jwt-token>"
```

### Update Product Quantity (Protected)
```bash
curl -X PUT "http://localhost:8000/products/<product-id>/quantity" \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "quantity": 15
  }'
```

## 🧪 Testing

### Manual Testing
1. Start the server: `uvicorn app.main:app --reload`
2. Access API documentation: `http://localhost:8000/docs`
3. Use the interactive Swagger UI to test endpoints

### Automated Testing
```bash
# Run tests (if test files are added)
pytest

# Run with coverage
pytest --cov=app
```

## 📚 API Documentation

Once the server is running, access the interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

The documentation includes:
- All available endpoints
- Request/response schemas
- Authentication requirements
- Interactive testing interface

## 🔧 Configuration Options

### Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `MONGODB_URL` | MongoDB connection string | `mongodb://localhost:27017` |
| `DATABASE_NAME` | Database name | `fimoney_inventory` |
| `SECRET_KEY` | JWT secret key | Required |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | `30` |
| `HOST` | Server host | `0.0.0.0` |
| `PORT` | Server port | `8000` |
| `DEBUG` | Debug mode | `False` |

## 🚀 Deployment

### Production Deployment
1. Set `DEBUG=False` in environment variables
2. Use a strong `SECRET_KEY`
3. Configure MongoDB with authentication
4. Set up reverse proxy (nginx)
5. Use process manager (PM2, systemd)

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📈 Performance Considerations

- **Database Indexing**: Ensure indexes on frequently queried fields
- **Connection Pooling**: Configure MongoDB connection pooling
- **Caching**: Implement Redis for session caching
- **Rate Limiting**: Add rate limiting middleware
- **Compression**: Enable gzip compression

## 🔒 Security Best Practices

- Use strong, unique secret keys
- Implement rate limiting
- Validate all input data
- Use HTTPS in production
- Regular security updates
- Monitor for suspicious activities

## 🐛 Troubleshooting

### Common Issues

1. **MongoDB Connection Error**
   - Verify MongoDB is running
   - Check connection string
   - Ensure network connectivity

2. **JWT Token Issues**
   - Verify secret key is set
   - Check token expiration
   - Ensure proper token format

3. **Import Errors**
   - Verify virtual environment is activated
   - Check all dependencies are installed
   - Ensure Python version compatibility

## 📞 Support

For issues and questions:
1. Check the API documentation
2. Review error logs
3. Test with the interactive Swagger UI
4. Create an issue in the repository

## 🎯 Deliverables

### Backend API
- ✅ Complete FastAPI application
- ✅ MongoDB integration
- ✅ JWT authentication system
- ✅ Product management endpoints
- ✅ Comprehensive error handling
- ✅ API documentation (Swagger/OpenAPI)
- ✅ Data validation with Pydantic
- ✅ Security best practices

### Documentation
- ✅ Detailed README with setup instructions
- ✅ API endpoint documentation
- ✅ Database schema documentation
- ✅ Authentication flow explanation
- ✅ Usage examples
- ✅ Deployment guidelines

### Code Quality
- ✅ Clean, maintainable code structure
- ✅ Type hints throughout
- ✅ Proper error handling
- ✅ Security implementations
- ✅ Scalable architecture

## 🔄 Future Enhancements

- [ ] User roles and permissions
- [ ] Bulk import/export functionality
- [ ] Advanced search and filtering
- [ ] Real-time notifications
- [ ] Analytics and reporting
- [ ] Multi-tenant support
- [ ] API rate limiting
- [ ] Caching layer
- [ ] Automated testing suite
- [ ] CI/CD pipeline

---

**Built with ❤️ using FastAPI and MongoDB** 