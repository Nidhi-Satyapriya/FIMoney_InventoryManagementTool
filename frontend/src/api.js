import axios from 'axios';

// API configuration - update this for production
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

// Axios instance with default configuration
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 second timeout
});

// AI suggestions for error handling and token management

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle auth errors and common responses
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/auth';
    }
    if (!error.response) {
      console.error('Network error:', error.message);
    }
    
    return Promise.reject(error);
  }
);

// Authentication endpoints
export const loginUser = async (username, password) => {
  const response = await api.post('/login', { username, password });
  return response.data;
};

export const registerUser = async (username, password) => {
  const response = await api.post('/register', { username, password });
  return response.data;
};

// Product endpoints
export const getProducts = async (skip = 0, limit = 10) => {
  const response = await api.get(`/products?skip=${skip}&limit=${limit}`);
  return response.data;
};

export const addProduct = async (productData) => {
  const response = await api.post('/products', productData);
  return response.data;
};

export const updateProductQuantity = async (productId, quantity) => {
  const response = await api.put(`/products/${productId}/quantity`, { quantity });
  return response.data;
};

// Legacy function for backward compatibility-- AI suggested
export const setToken = (token) => {
  if (token) {
    localStorage.setItem('token', token);
  } else {
    localStorage.removeItem('token');
  }
};

export default api;
