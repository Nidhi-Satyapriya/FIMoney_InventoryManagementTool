import { useEffect, useState } from 'react';
import { getProducts } from './api';
import UpdateQuantityForm from './UpdateQuantityForm';

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);
  const [error, setError] = useState('');
  const limit = 10;

  function fetchProducts() {
    setError('');
    getProducts(page, limit)
      .then(res => {
        setProducts(res.products || res.data || []);
        setTotal(res.total || res.count || 0);
      })
      .catch(e => setError(e.message));
  }

  useEffect(() => {
    fetchProducts();
    // eslint-disable-next-line
  }, [page]);

  return (
    <div className="product-list">
      <h2>Products</h2>
      {error && <div className="error">{error}</div>}
      <table>
        <thead>
          <tr>
            <th>Name</th><th>Type</th><th>SKU</th><th>Qty</th><th>Price</th><th>Update Qty</th>
          </tr>
        </thead>
        <tbody>
          {products.map(p => (
            <tr key={p.id || p._id}>
              <td>{p.name}</td>
              <td>{p.type}</td>
              <td>{p.sku}</td>
              <td>{p.quantity}</td>
              <td>{p.price}</td>
              <td><UpdateQuantityForm id={p.id || p._id} current={p.quantity} onUpdate={fetchProducts} /></td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="pagination">
        <button onClick={() => setPage(p => Math.max(1, p - 1))} disabled={page === 1}>Prev</button>
        <span>Page {page}</span>
        <button onClick={() => setPage(p => p + 1)} disabled={products.length < limit}>Next</button>
      </div>
    </div>
  );
}
