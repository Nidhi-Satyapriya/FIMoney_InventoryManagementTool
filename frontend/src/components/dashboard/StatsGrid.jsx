import './StatsGrid.css';

function StatsGrid({ stats }) {
  return (
    <div className="stats-grid">
      <div className="stat-card">
        <div className="stat-content">
          <h3>{stats.totalProducts}</h3>
          <p>Total Products</p>
        </div>
      </div>

      <div className="stat-card">
        <div className="stat-content">
          <h3>${stats.totalValue.toFixed(2)}</h3>
          <p>Total Value</p>
        </div>
      </div>

      <div className="stat-card">
        <div className="stat-content">
          <h3>{stats.lowStock}</h3>
          <p>Low Stock Items</p>
        </div>
      </div>

      <div className="stat-card">
        <div className="stat-content">
          <h3>{stats.totalProducts > 0 ? (stats.totalValue / stats.totalProducts).toFixed(2) : 0}</h3>
          <p>Avg. Value</p>
        </div>
      </div>
    </div>
  );
}

export default StatsGrid; 