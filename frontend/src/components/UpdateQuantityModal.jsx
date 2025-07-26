import { useState } from 'react';
import './Modal.css';

function UpdateQuantityModal({ product, onClose, onUpdate }) {
  const [quantity, setQuantity] = useState(product.quantity);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (quantity < 0) {
      setError('Quantity cannot be negative');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      await onUpdate(product._id, quantity);
    } catch (error) {
      setError('Failed to update quantity. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleQuickUpdate = (change) => {
    const newQuantity = Math.max(0, quantity + change);
    setQuantity(newQuantity);
    setError('');
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div className="modal-title">
            <h2>Update Quantity</h2>
          </div>
          <button onClick={onClose} className="modal-close">
            ✕
          </button>
        </div>

        <div className="product-summary">
          <div className="product-info">
            <h3>{product.name}</h3>
            <p className="product-sku">SKU: {product.sku}</p>
            <p className="product-type">{product.type}</p>
          </div>
          <div className="current-quantity">
            <span className="label">Current Quantity:</span>
            <span className="value">{product.quantity}</span>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="modal-form">
          <div className="form-group">
            <label htmlFor="new-quantity">New Quantity</label>
            <div className="quantity-input-container">
              <button
                type="button"
                onClick={() => handleQuickUpdate(-1)}
                className="quantity-btn"
                disabled={quantity <= 0}
              >
                -
              </button>
              
              <input
                type="number"
                id="new-quantity"
                value={quantity}
                onChange={(e) => {
                  setQuantity(parseInt(e.target.value) || 0);
                  setError('');
                }}
                min="0"
                className={error ? 'error' : ''}
              />
              
              <button
                type="button"
                onClick={() => handleQuickUpdate(1)}
                className="quantity-btn"
              >
                +
              </button>
            </div>
            {error && <span className="error-message">{error}</span>}
          </div>

          <div className="quantity-change-info">
            <div className="change-indicator">
              <span className="label">Change:</span>
              <span className={`value ${quantity - product.quantity >= 0 ? 'positive' : 'negative'}`}>
                {quantity - product.quantity >= 0 ? '+' : ''}{quantity - product.quantity}
              </span>
            </div>
            
            {product.price && (
              <div className="value-change">
                <span className="label">Value Change:</span>
                <span className={`value ${quantity - product.quantity >= 0 ? 'positive' : 'negative'}`}>
                  ${((quantity - product.quantity) * product.price).toFixed(2)}
                </span>
              </div>
            )}
          </div>

          <div className="modal-actions">
            <button
              type="button"
              onClick={onClose}
              className="cancel-button"
              disabled={loading}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="submit-button"
              disabled={loading || quantity === product.quantity}
            >
              {loading ? (
                <div className="spinner"></div>
              ) : (
                'Update Quantity'
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default UpdateQuantityModal; 