const express = require('express');
const { Pool } = require('pg');
const app = express();
const port = 8080;

const pool = new Pool({
  host: process.env.DB_HOST || 'enterprise-database-svc',
  port: process.env.DB_PORT || 5432,
  database: process.env.DB_NAME || 'enterprise',
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'postgres',
  connectionTimeoutMillis: 5000,
});

app.get('/', async (req, res) => {
  try {
    console.log('Attempting database query...');
    const result = await pool.query('SELECT NOW()');
    console.log('Database query successful.');
    res.send(`Hello from Custom Enterprise Backend! DB Time: ${result.rows[0].now}`);
  } catch (err) {
    console.error('Database query error:', err.message);
    res.status(500).send(`Database connection error: ${err.message}`);
  }
});

app.listen(port, () => {
  console.log(`Backend running on port ${port}`);
});
