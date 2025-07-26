import { useState } from 'react';
import './ProductList.css';

function ProductList({ products, onUpdateQuantity, onRefresh }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('name');

  const filteredProducts = products
    .filter(product =>
      product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      product.sku.toLowerCase().includes(searchTerm.toLowerCase()) ||
      product.type.toLowerCase().includes(searchTerm.toLowerCase())
    )
    .sort((a, b) => {
      switch (sortBy) {
        case 'name':
          return a.name.localeCompare(b.name);
        case 'quantity':
          return a.quantity - b.quantity;
        case 'price':
          return a.price - b.price;
        case 'type':
          return a.type.localeCompare(b.type);
        default:
          return 0;
      }
    });

  const getStockStatus = (quantity) => {
    if (quantity === 0) return { status: 'out-of-stock', label: 'Out of Stock' };
    if (quantity < 10) return { status: 'low-stock', label: 'Low Stock' };
    return { status: 'in-stock', label: 'In Stock' };
  };

  return (
    <div className="product-list-container">
      <div className="product-list-header">
        <div className="search-container">
          <input
            type="text"
            placeholder="Search products by name, SKU, or type..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>

        <div className="sort-container">
          <label htmlFor="sort-select">Sort by:</label>
          <select
            id="sort-select"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="sort-select"
          >
            <option value="name">Name</option>
            <option value="quantity">Quantity</option>
            <option value="price">Price</option>
            <option value="type">Type</option>
          </select>
        </div>
      </div>

      {filteredProducts.length === 0 ? (
        <div className="empty-state">
          <h3>No products found</h3>
          <p>
            {searchTerm
              ? `No products match "${searchTerm}"`
              : 'Start by adding your first product'}
          </p>
        </div>
      ) : (
        <div className="product-grid">
          {filteredProducts.map((product) => {
            const stockStatus = getStockStatus(product.quantity);
            return (
              <div key={product._id} className="product-card">
                <div className="product-image">
                  {product.image_url ? (
                    <img src={product.image_url} alt={product.name} />
                  ) : (
                    <div className="product-placeholder">
                      📦
                    </div>
                  )}
                  <div className={`stock-badge ${stockStatus.status}`}>
                    {stockStatus.label}
                  </div>
                </div>

                <div className="product-info">
                  <h3 className="product-name">{product.name}</h3>
                  <p className="product-sku">SKU: {product.sku}</p>
                  <p className="product-type">{product.type}</p>
                  
                  {product.description && (
                    <p className="product-description">{product.description}</p>
                  )}

                  <div className="product-details">
                    <div className="detail-item">
                      <span className="detail-label">Quantity:</span>
                      <span className={`detail-value ${stockStatus.status}`}>
                        {product.quantity}
                      </span>
                    </div>
                    <div className="detail-item">
                      <span className="detail-label">Price:</span>
                      <span className="detail-value price">${product.price.toFixed(2)}</span>
                    </div>
                    <div className="detail-item">
                      <span className="detail-label">Total Value:</span>
                      <span className="detail-value">
                        ${(product.price * product.quantity).toFixed(2)}
                      </span>
                    </div>
                  </div>

                  <button
                    onClick={() => onUpdateQuantity(product)}
                    className="update-button"
                  >
                    Update Quantity
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      <div className="product-list-footer">
        <p>Showing {filteredProducts.length} of {products.length} products</p>
      </div>
    </div>
  );
}

export default ProductList; 