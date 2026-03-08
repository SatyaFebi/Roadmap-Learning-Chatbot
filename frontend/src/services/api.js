const API_BASE = '/api'
const APP_NAME = 'restaurant_concierge'

export function generateUserId() {
  const stored = localStorage.getItem('ck_user_id')
  if (stored) return stored
  const id = crypto.randomUUID()
  localStorage.setItem('ck_user_id', id)
  return id
}

export async function createSession(userId) {
  const res = await fetch(`${API_BASE}/apps/${APP_NAME}/users/${userId}/sessions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ state: {} }),
  })
  if (!res.ok) throw new Error('Failed to create session')
  return res.json()
}

export async function runAgent(userId, sessionId, message) {
  const res = await fetch(`${API_BASE}/run`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      appName: APP_NAME,
      userId: userId,
      sessionId: sessionId,
      newMessage: {
        role: 'user',
        parts: [{ text: message }],
      },
      streaming: false,
    }),
  })
  if (!res.ok) throw new Error('Failed to run agent')
  return res.json()
}
