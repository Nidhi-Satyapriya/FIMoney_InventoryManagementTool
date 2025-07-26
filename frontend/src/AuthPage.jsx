import { useState } from 'react';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';

export default function AuthPage({ onAuth }) {
  const [showLogin, setShowLogin] = useState(true);
  const [signupSuccess, setSignupSuccess] = useState(false);

  return (
    <div className="auth-illustration-bg">
      <div className="auth-illustration">
        <div className="auth-card">
          <div className="auth-header">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="User" className="auth-avatar" />
            <h2>{showLogin ? 'Login' : 'Sign Up'}</h2>
          </div>
          {signupSuccess && (
            <div className="success-msg">Signup successful! Please login.</div>
          )}
          {showLogin ? (
            <LoginForm onAuth={onAuth} />
          ) : (
            <SignupForm onSignup={() => { setSignupSuccess(true); setShowLogin(true); }} />
          )}
          <button className="auth-switch" onClick={() => { setShowLogin(l => !l); setSignupSuccess(false); }} type="button">
            {showLogin ? 'Need an account? Sign Up' : 'Have an account? Login'}
          </button>
        </div>
      </div>
    </div>
  );
}
