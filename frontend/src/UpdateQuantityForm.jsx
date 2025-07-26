import { useState } from 'react';
import { updateProductQuantity } from './api';

export default function UpdateQuantityForm({ id, current, onUpdate }) {
  const [quantity, setQuantity] = useState(current);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await updateProductQuantity(id, Number(quantity));
      onUpdate && onUpdate();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form className="update-qty-form" onSubmit={handleSubmit} style={{ display: 'inline' }}>
      <input type="number" value={quantity} onChange={e => setQuantity(e.target.value)} style={{ width: 60 }} />
      <button type="submit" disabled={loading}>Update</button>
      {error && <span className="error">{error}</span>}
    </form>
  );
}
