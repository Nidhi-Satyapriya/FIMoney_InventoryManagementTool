import { useAuth } from '../../contexts/AuthContext';
import './Header.css';

function Header() {
  const { logout } = useAuth();

  return (
    <header className="dashboard-header">
      <div className="header-left">
        <h1>FIMoney Inventory Dashboard</h1>
      </div>
      <button onClick={logout} className="logout-button">
        Logout
      </button>
    </header>
  );
}

export default Header; 