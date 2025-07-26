# FIMoney Inventory Management Tool - Setup Guide

This guide will help you set up and run the complete FIMoney Inventory Management System with both backend and frontend.

## 🎯 Quick Start

### Prerequisites
- **Python 3.8+** for backend
- **Node.js 16+** for frontend  
- **MongoDB** (local or cloud instance)
- **Git**

## 🚀 Step-by-Step Setup

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd FIMoney_InventoryManagementTool
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
cd FIMoney_InventoryManagementTool
pip install -r requirements.txt
```

#### Start MongoDB
Make sure MongoDB is running on your system:
- **Windows**: Start MongoDB service
- **macOS**: `brew services start mongodb-community`
- **Linux**: `sudo systemctl start mongod`

#### Start Backend Server
```bash
# Option 1: Using the startup script
python start_backend.py

# Option 2: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at: **http://localhost:8000**

### 3. Frontend Setup

#### Install Node.js Dependencies
```bash
cd frontend
npm install --legacy-peer-deps
```

#### Start Frontend Development Server
```bash
npm run dev
```

The frontend will be available at: **http://localhost:5173**

## 🧪 Testing the System

### Test Backend API
```bash
cd FIMoney_InventoryManagementTool
python test_backend.py
```

### Manual Testing
1. **Access Frontend**: http://localhost:5173
2. **Register a new user**
3. **Login with credentials**
4. **Add products**
5. **Update quantities**
6. **Test search and filtering**

## 📋 API Endpoints

### Authentication
- `POST /register` - User registration
- `POST /login` - User authentication

### Products (Protected)
- `GET /products` - Retrieve all products
- `POST /products` - Add new product  
- `PUT /products/{id}/quantity` - Update product quantity

## 🔧 Configuration

### Environment Variables (Backend)
The backend uses these environment variables (set automatically in startup script):
- `MONGODB_URL` - MongoDB connection string
- `DATABASE_NAME` - Database name
- `SECRET_KEY` - JWT secret key
- `ALGORITHM` - JWT algorithm
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time

### Frontend Configuration
The frontend automatically connects to `http://localhost:8000` for the API.

## 🐛 Troubleshooting

### Common Issues

#### Backend Issues
1. **MongoDB Connection Error**
   - Ensure MongoDB is running
   - Check connection string
   - Verify network connectivity

2. **Import Errors**
   - Verify virtual environment is activated
   - Check all dependencies are installed
   - Ensure Python version compatibility

#### Frontend Issues
1. **Dependency Installation**
   - Use `npm install --legacy-peer-deps`
   - Clear node_modules and reinstall if needed

2. **API Connection**
   - Verify backend is running on port 8000
   - Check browser console for CORS errors

### Error Messages

#### "Cannot connect to server"
- Backend is not running
- Wrong port or host
- Firewall blocking connection

#### "MongoDB connection error"
- MongoDB service not started
- Wrong connection string
- Network issues

#### "Module not found"
- Dependencies not installed
- Wrong Python/Node.js version
- Path issues

## 📊 System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (React)       │◄──►│   (FastAPI)     │◄──►│   (MongoDB)     │
│   Port: 5173    │    │   Port: 8000    │    │   Port: 27017   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🎯 Features Working

### ✅ Backend Features
- User authentication with JWT
- Product CRUD operations
- Database integration
- API documentation (Swagger)
- Error handling

### ✅ Frontend Features
- User registration and login
- Product management dashboard
- Real-time search and filtering
- Responsive design
- Form validation

### ✅ Integration Features
- JWT token management
- Protected routes
- Real-time data updates
- Error handling and user feedback

## 🚀 Production Deployment

### Backend Deployment
1. Set production environment variables
2. Use production WSGI server (Gunicorn)
3. Set up reverse proxy (Nginx)
4. Configure MongoDB with authentication

### Frontend Deployment
1. Build for production: `npm run build`
2. Deploy to hosting platform (Vercel, Netlify, etc.)
3. Configure environment variables

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review error logs
3. Test individual components
4. Create an issue in the repository

## 🎉 Success Indicators

You'll know everything is working when:
- ✅ Backend starts without errors
- ✅ Frontend loads without console errors
- ✅ User registration works
- ✅ Login returns JWT token
- ✅ Products can be added and retrieved
- ✅ Search and filtering work
- ✅ UI is responsive and functional

---

**Happy coding! 🚀** 