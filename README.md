# FIMoney Inventory Management Tool

A complete, modern inventory management system with a FastAPI backend and React frontend. This project demonstrates a full-stack application with JWT authentication, real-time inventory tracking, and a beautiful, responsive user interface.

## 🎯 Project Overview

FIMoney Inventory Management Tool is a comprehensive solution for managing product inventory with features like user authentication, product management, real-time stock tracking, and an intuitive dashboard interface.

### Key Features
- **🔐 Secure Authentication**: JWT-based user authentication with registration and login
- **📦 Product Management**: Complete CRUD operations for inventory items
- **📊 Real-time Dashboard**: Live statistics and inventory overview
- **🔍 Search & Filter**: Advanced product search and sorting capabilities
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **🎨 Modern UI**: Beautiful, intuitive interface with smooth animations

## 🏗️ Architecture

```
FIMoney_InventoryManagementTool/
├── FIMoney_InventoryManagementTool/  # Backend API
│   ├── app/
│   │   ├── auth/          # Authentication logic
│   │   ├── crud/          # Database operations
│   │   ├── database/      # Database configuration
│   │   ├── models/        # Data models
│   │   ├── routes/        # API endpoints
│   │   ├── schemas/       # Pydantic schemas
│   │   └── main.py        # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   └── README.md         # Backend documentation
├── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── contexts/      # React contexts
│   │   ├── api.js         # API integration
│   │   └── App.jsx        # Main application
│   ├── package.json       # Node.js dependencies
│   └── README.md         # Frontend documentation
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** for backend
- **Node.js 16+** for frontend
- **MongoDB** (local or cloud instance)
- **Git**

### 1. Clone the Repository
```bash
git clone <repository-url>
cd FIMoney_InventoryManagementTool
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd FIMoney_InventoryManagementTool

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=fimoney_inventory
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30" > .env

# Start backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: MongoDB
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **Data Validation**: Pydantic
- **Server**: Uvicorn (ASGI)

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **UI Icons**: Lucide React
- **Notifications**: React Hot Toast
- **Styling**: CSS3 with modern features

## 📋 API Endpoints

### Authentication
- `POST /register` - User registration
- `POST /login` - User authentication

### Products (Protected)
- `GET /products` - Retrieve all products
- `POST /products` - Add new product
- `PUT /products/{id}/quantity` - Update product quantity

## 🎨 User Interface

### Authentication Page
- Clean login/register interface
- Form validation and error handling
- Smooth transitions between modes

### Dashboard
- Statistics cards showing key metrics
- Quick access to add products
- Real-time data updates

### Product Management
- Card-based product display
- Search and filtering capabilities
- Stock level indicators
- Interactive quantity updates

## 🔐 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt for password security
- **Protected Routes**: Authentication guards on frontend
- **Input Validation**: Comprehensive data validation
- **CORS Handling**: Proper cross-origin request handling

## 📱 Responsive Design

The application is fully responsive with:
- **Desktop**: Full-featured interface
- **Tablet**: Optimized layouts
- **Mobile**: Touch-friendly design

## 🧪 Testing

### Backend Testing
```bash
# Access interactive API documentation
http://localhost:8000/docs

# Use Swagger UI for testing endpoints
```

### Frontend Testing
```bash
# Start development server
npm run dev

# Test all user flows manually
```

## 🚀 Deployment

### Backend Deployment
```bash
# Production build
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Docker deployment available
docker build -t fimoney-backend .
docker run -p 8000:8000 fimoney-backend
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Deploy to Vercel/Netlify
# Upload dist folder to hosting platform
```

## 📊 Database Schema

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

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=fimoney_inventory
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_NAME=FIMoney Inventory
```

## 🐛 Troubleshooting

### Common Issues

1. **MongoDB Connection**
   - Ensure MongoDB is running
   - Check connection string in .env
   - Verify network connectivity

2. **Frontend Build Issues**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility
   - Verify all dependencies

3. **Authentication Problems**
   - Check JWT token format
   - Verify secret key configuration
   - Clear browser localStorage

## 📚 Documentation

- **[Backend README](./FIMoney_InventoryManagementTool/README.md)** - Detailed backend documentation
- **[Frontend README](./frontend/README.md)** - Comprehensive frontend guide
- **[API Documentation](http://localhost:8000/docs)** - Interactive API docs

## 🎯 Deliverables

### Complete Application
- ✅ Full-stack inventory management system
- ✅ Modern, responsive user interface
- ✅ Secure authentication system
- ✅ Real-time data management
- ✅ Comprehensive documentation

### Backend Features
- ✅ FastAPI REST API
- ✅ MongoDB integration
- ✅ JWT authentication
- ✅ Data validation
- ✅ Error handling
- ✅ API documentation

### Frontend Features
- ✅ React application
- ✅ Responsive design
- ✅ Authentication integration
- ✅ Product management
- ✅ Search and filtering
- ✅ Modern UI/UX

## 🔄 Future Enhancements

- [ ] User roles and permissions
- [ ] Advanced analytics dashboard
- [ ] Bulk import/export
- [ ] Real-time notifications
- [ ] Mobile app
- [ ] Multi-tenant support
- [ ] Advanced reporting
- [ ] Integration with external systems

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions and issues:
1. Check the documentation
2. Review troubleshooting section
3. Create an issue in the repository
4. Contact the development team

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ using FastAPI, React, and MongoDB**

*FIMoney Inventory Management Tool - Complete Inventory Solution*