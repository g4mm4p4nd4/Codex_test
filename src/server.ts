import express from 'express';
import { registerUser, authenticateUser } from './auth/service';

const app = express();
app.use(express.json());

app.post('/register', (req, res) => {
  const { username, password } = req.body || {};
  if (!username || !password) {
    return res.status(400).json({ error: 'missing_fields' });
  }
  if (registerUser(username, password)) {
    return res.status(201).json({ status: 'registered' });
  }
  return res.status(400).json({ error: 'user_exists' });
});

app.post('/login', (req, res) => {
  const { username, password } = req.body || {};
  if (authenticateUser(username, password)) {
    return res.json({ status: 'ok' });
  }
  return res.status(401).json({ error: 'invalid_credentials' });
});

export default app;

if (require.main === module) {
  const port = process.env.PORT || 3000;
  app.listen(port, () => console.log(`Server running on port ${port}`));
}
