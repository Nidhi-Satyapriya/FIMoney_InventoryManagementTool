import { createContext, useContext, useState, useEffect } from 'react';
import { loginUser, registerUser } from '../api';

const AuthContext = createContext();

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
      setUser({ token });
    } else {
      localStorage.removeItem('token');
      setUser(null);
    }
    setLoading(false);
  }, [token]);

  const login = async (username, password) => {
    try {
      const response = await loginUser(username, password);
      setToken(response.access_token);
      setMessage('Login successful!');
      return true;
    } catch (error) {
      setMessage(error.response?.data?.detail || 'Login failed');
      return false;
    }
  };

  const register = async (username, password) => {
    try {
      await registerUser(username, password);
      setMessage('Registration successful! Please login.');
      return true;
    } catch (error) {
      setMessage(error.response?.data?.detail || 'Registration failed');
      return false;
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    setMessage('Logged out successfully');
  };

  const clearMessage = () => {
    setMessage('');
  };

  const value = {
    user,
    token,
    isAuthenticated: !!token,
    loading,
    message,
    login,
    register,
    logout,
    clearMessage
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
} 