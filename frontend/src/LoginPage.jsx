import { useState } from 'react';
import { login } from './api';

export default function LoginPage({ onAuth }) {
  const [form, setForm] = useState({ username: '', password: '' });
  const [error, setError] = useState('');
  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);

  const handleChange = e => setForm(f => ({ ...f, [e.target.name]: e.target.value }));

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      let data;
      if (isLogin) {
        data = await login(form.username, form.password);
      } else {
        // signup endpoint assumed as /signup, returns { token }
        const res = await fetch('/api/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(form)
        });
        if (!res.ok) throw new Error(await res.text());
        data = await res.json();
      }
      onAuth(data.token);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="auth-illustration-bg">
      <div className="auth-illustration">
        <div className="auth-card">
          <div className="auth-header">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="User" className="auth-avatar" />
            <h2>{isLogin ? 'Login' : 'Sign Up'}</h2>
          </div>
          <form onSubmit={handleSubmit} className="auth-form">
            <input name="username" placeholder="Username" value={form.username} onChange={handleChange} required autoFocus />
            <input name="password" type="password" placeholder="Password" value={form.password} onChange={handleChange} required />
            <button type="submit" disabled={loading}>{loading ? (isLogin ? 'Logging in...' : 'Signing up...') : (isLogin ? 'Login' : 'Sign Up')}</button>
          </form>
          <button className="auth-switch" onClick={() => setIsLogin(l => !l)} type="button">
            {isLogin ? 'Need an account? Sign Up' : 'Have an account? Login'}
          </button>
          {error && <div className="error">{error}</div>}
        </div>
      </div>
    </div>
  );
}
