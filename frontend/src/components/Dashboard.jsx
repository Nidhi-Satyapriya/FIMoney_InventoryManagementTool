import { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { getProducts, addProduct, updateProductQuantity } from '../api';
import Header from './layout/Header';
import StatsGrid from './dashboard/StatsGrid';
import ProductList from './ProductList';
import AddProductModal from './AddProductModal';
import UpdateQuantityModal from './UpdateQuantityModal';
import './Dashboard.css';

function Dashboard() {
  const { message } = useAuth();
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showAddModal, setShowAddModal] = useState(false);
  const [showUpdateModal, setShowUpdateModal] = useState(false);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [stats, setStats] = useState({
    totalProducts: 0,
    totalValue: 0,
    lowStock: 0
  });

  useEffect(() => {
    fetchProducts();
  }, []);

  useEffect(() => {
    calculateStats();
  }, [products]);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const data = await getProducts(0, 100);
      setProducts(data);
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setLoading(false);
    }
  };

  const calculateStats = () => {
    const totalProducts = products.length;
    const totalValue = products.reduce((sum, product) => sum + (product.price * product.quantity), 0);
    const lowStock = products.filter(product => product.quantity < 10).length;

    setStats({ totalProducts, totalValue, lowStock });
  };

  const handleAddProduct = async (productData) => {
    try {
      await addProduct(productData);
      setShowAddModal(false);
      fetchProducts();
    } catch (error) {
      console.error('Error adding product:', error);
    }
  };

  const handleUpdateQuantity = async (productId, quantity) => {
    try {
      await updateProductQuantity(productId, quantity);
      setShowUpdateModal(false);
      setSelectedProduct(null);
      fetchProducts();
    } catch (error) {
      console.error('Error updating quantity:', error);
    }
  };

  const openUpdateModal = (product) => {
    setSelectedProduct(product);
    setShowUpdateModal(true);
  };

  return (
    <div className="dashboard">
      <Header />

      {message && (
        <div className={`message ${message.includes('successful') ? 'success' : 'error'}`}>
          {message}
        </div>
      )}

      <StatsGrid stats={stats} />

      <div className="dashboard-content">
        <div className="content-header">
          <h2>Product Inventory</h2>
          <button
            onClick={() => setShowAddModal(true)}
            className="add-button"
          >
            Add Product
          </button>
        </div>

        {loading ? (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Loading products...</p>
          </div>
        ) : (
          <ProductList
            products={products}
            onUpdateQuantity={openUpdateModal}
            onRefresh={fetchProducts}
          />
        )}
      </div>

      {showAddModal && (
        <AddProductModal
          onClose={() => setShowAddModal(false)}
          onAdd={handleAddProduct}
        />
      )}

      {showUpdateModal && selectedProduct && (
        <UpdateQuantityModal
          product={selectedProduct}
          onClose={() => {
            setShowUpdateModal(false);
            setSelectedProduct(null);
          }}
          onUpdate={handleUpdateQuantity}
        />
      )}
    </div>
  );
}

export default Dashboard; 