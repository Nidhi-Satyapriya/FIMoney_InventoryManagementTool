import { useEffect, useState } from 'react';
import { apiRequest } from './api';

export default function TestimonialPage({ user, onLogout }) {
  const [testimonials, setTestimonials] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    apiRequest('testimonials')
      .then(setTestimonials)
      .catch(e => setError(e.message));
  }, []);

  return (
    <div className="testimonial-container">
      <div className="header">
        <h2>API Testimonials</h2>
        <button onClick={onLogout}>Logout</button>
      </div>
      {error && <div className="error">{error}</div>}
      <ul>
        {testimonials.map((t, i) => (
          <li key={i}>
            <strong>{t.author}</strong>: {t.message}
          </li>
        ))}
      </ul>
    </div>
  );
}
