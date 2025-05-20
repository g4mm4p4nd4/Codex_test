import { registerUser, authenticateUser } from '../../../src/auth/service';

describe('auth service', () => {
  it('registers and authenticates a user', () => {
    expect(registerUser('alice', 'secret')).toBe(true);
    expect(registerUser('alice', 'secret')).toBe(false);
    expect(authenticateUser('alice', 'secret')).toBe(true);
    expect(authenticateUser('alice', 'wrong')).toBe(false);
  });
});
