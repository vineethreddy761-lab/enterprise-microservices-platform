const express = require('express');
const app = express();
const port = 8080;

app.get('/', (req, res) => {
  res.send('Hello from Custom Enterprise Backend');
});

app.listen(port, () => {
  console.log(`Backend running on port ${port}`);
});
