import request from 'supertest';
import app from '../../src/server';

describe('server endpoints', () => {
  it('registers and logs in', async () => {
    const reg = await request(app).post('/register').send({ username: 'bob', password: 'pass' });
    expect(reg.status).toBe(201);
    const loginOk = await request(app).post('/login').send({ username: 'bob', password: 'pass' });
    expect(loginOk.status).toBe(200);
    const loginFail = await request(app).post('/login').send({ username: 'bob', password: 'bad' });
    expect(loginFail.status).toBe(401);
  });
});
