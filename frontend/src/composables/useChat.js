import { ref, nextTick } from 'vue'
import { createSession, runAgent, generateUserId } from '@/services/api'

export function useChat() {
  const messages = ref([])
  const input = ref('')
  const loading = ref(false)
  const userId = generateUserId()
  const sessionId = ref(null)
  const error = ref(null)

  async function ensureSession() {
    if (sessionId.value) return
    const data = await createSession(userId)
    sessionId.value = data.id
  }

  async function send() {
    const text = input.value.trim()
    if (!text || loading.value) return

    error.value = null
    input.value = ''
    messages.value.push({ role: 'user', text, id: Date.now() })
    loading.value = true

    try {
      await ensureSession()
      const events = await runAgent(userId, sessionId.value, text)

      // Extract text from the last model response event
      let reply = ''
      if (Array.isArray(events)) {
        for (const event of events) {
          const parts = event?.content?.parts
          if (parts && event?.author !== 'user') {
            for (const p of parts) {
              if (p.text && !p.thought) reply = p.text // take last non-thought text
            }
          }
        }
      }

      messages.value.push({
        role: 'assistant',
        text: reply || 'Maaf, saya tidak bisa menjawab saat ini.',
        id: Date.now() + 1,
      })
    } catch (e) {
      console.error(e)
      error.value = 'Gagal mengirim pesan. Silakan coba lagi.'
      messages.value.push({
        role: 'assistant',
        text: '⚠️ Terjadi kesalahan. Pastikan server AI sudah aktif di port 8080.',
        id: Date.now() + 1,
      })
    } finally {
      loading.value = false
    }
  }

  function clearChat() {
    messages.value = []
    sessionId.value = null
    error.value = null
  }

  return { messages, input, loading, error, send, clearChat }
}
