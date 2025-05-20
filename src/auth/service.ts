import crypto from 'crypto';

interface User {
  username: string;
  passwordHash: string;
  salt: string;
}

const users: Record<string, User> = {};

function hashPassword(password: string, salt: string): string {
  return crypto.pbkdf2Sync(password, salt, 100000, 64, 'sha512').toString('hex');
}

export function registerUser(username: string, password: string): boolean {
  if (users[username]) {
    return false;
  }
  const salt = crypto.randomBytes(16).toString('hex');
  const passwordHash = hashPassword(password, salt);
  users[username] = { username, passwordHash, salt };
  return true;
}

export function authenticateUser(username: string, password: string): boolean {
  const user = users[username];
  if (!user) return false;
  const attemptedHash = hashPassword(password, user.salt);
  return attemptedHash === user.passwordHash;
}
