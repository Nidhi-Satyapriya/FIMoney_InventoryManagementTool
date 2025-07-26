import { useState } from 'react';
import { addProduct } from './api';

export default function AddProductForm({ onAdd }) {
  const [form, setForm] = useState({
    name: '', type: '', sku: '', image_url: '', description: '', quantity: '', price: ''
  });
  const [error, setError] = useState('');

  const handleChange = e => setForm(f => ({ ...f, [e.target.name]: e.target.value }));

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    try {
      const product = { ...form, quantity: Number(form.quantity), price: Number(form.price) };
      await addProduct(product);
      setForm({ name: '', type: '', sku: '', image_url: '', description: '', quantity: '', price: '' });
      onAdd && onAdd();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form className="add-product-form" onSubmit={handleSubmit}>
      <h3>Add Product</h3>
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} required />
      <input name="type" placeholder="Type" value={form.type} onChange={handleChange} required />
      <input name="sku" placeholder="SKU" value={form.sku} onChange={handleChange} required />
      <input name="image_url" placeholder="Image URL" value={form.image_url} onChange={handleChange} />
      <input name="description" placeholder="Description" value={form.description} onChange={handleChange} />
      <input name="quantity" type="number" placeholder="Quantity" value={form.quantity} onChange={handleChange} required />
      <input name="price" type="number" step="0.01" placeholder="Price" value={form.price} onChange={handleChange} required />
      <button type="submit">Add</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
}
