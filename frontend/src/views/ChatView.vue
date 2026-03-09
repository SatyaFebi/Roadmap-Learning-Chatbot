<script setup>
import { ref, nextTick, watch } from 'vue'
import { useChat } from '@/composables/useChat'
import ChatBubble from '@/components/ChatBubble.vue'
import TypingIndicator from '@/components/TypingIndicator.vue'
import QuickSuggestions from '@/components/QuickSuggestions.vue'

const { messages, input, loading, error, send, clearChat } = useChat()
const chatArea = ref(null)
const inputRef = ref(null)

// Auto-scroll on new messages
watch(
  () => messages.value.length,
  async () => {
    await nextTick()
    if (chatArea.value) {
      chatArea.value.scrollTo({ top: chatArea.value.scrollHeight, behavior: 'smooth' })
    }
  },
)

function handleSuggestion(prompt) {
  input.value = prompt
  send()
}

function handleKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    send()
  }
}
</script>

<template>
  <div class="chat-layout">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-brand">
        <div class="brand-icon">🍳</div>
        <div>
          <h1 class="brand-title">Roadmap Architect AI</h1>
          <p class="brand-sub">AI Concierge</p>
        </div>
      </div>

      <nav class="sidebar-nav">
        <button class="nav-btn active" @click="clearChat">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
          <span>Chat Baru</span>
        </button>
      </nav>

      <div class="sidebar-footer">
        <div class="status-dot"></div>
        <span class="status-text">Gemini 2.5 Flash</span>
      </div>
    </aside>

    <!-- Main chat -->
    <main class="chat-main">
      <!-- Header -->
      <header class="chat-header">
        <div class="header-info">
          <h2>Roadmap Architect AI</h2>
          <span class="header-badge">AI-Powered</span>
        </div>
        <button class="icon-btn" title="Chat baru" @click="clearChat">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="1 4 1 10 7 10"/>
            <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>
          </svg>
        </button>
      </header>

      <!-- Messages area -->
      <div ref="chatArea" class="chat-area">
        <!-- Empty state -->
        <div v-if="messages.length === 0" class="empty-state">
          <div class="empty-icon">🤖</div>
          <h3>Welcome!</h3>
          <p>Saya asisten roadmap AI Anda. Tanya saya tentang kebutuhan dan keinginan belajar Anda.</p>
          <QuickSuggestions @select="handleSuggestion" />
        </div>

        <!-- Messages -->
        <template v-else>
          <ChatBubble v-for="msg in messages" :key="msg.id" :msg="msg" />
          <div v-if="loading" class="bubble-row">
            <div class="avatar bot-avatar">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 2a4 4 0 0 1 4 4v2a4 4 0 0 1-8 0V6a4 4 0 0 1 4-4z"/>
                <path d="M16 14H8a4 4 0 0 0-4 4v2h16v-2a4 4 0 0 0-4-4z"/>
              </svg>
            </div>
            <TypingIndicator />
          </div>
        </template>
      </div>

      <!-- Error banner -->
      <div v-if="error" class="error-banner">
        <span>⚠️ {{ error }}</span>
        <button @click="error = null">✕</button>
      </div>

      <!-- Input bar -->
      <div class="input-bar">
        <div class="input-wrapper">
          <textarea
            ref="inputRef"
            v-model="input"
            rows="1"
            placeholder="Ketik pesan Anda..."
            @keydown="handleKeydown"
            :disabled="loading"
          ></textarea>
          <button
            class="send-btn"
            :disabled="!input.trim() || loading"
            @click="send"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"/>
              <polygon points="22 2 15 22 11 13 2 9 22 2"/>
            </svg>
          </button>
        </div>
        <p class="input-hint">Powered by Google ADK & Gemini</p>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* ===== LAYOUT ===== */
.chat-layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* ===== SIDEBAR ===== */
.sidebar {
  width: 260px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: 20px 14px;
  flex-shrink: 0;
}
.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 6px 20px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
}
.brand-icon {
  font-size: 1.8rem;
}
.brand-title {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}
.brand-sub {
  font-size: 0.72rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.sidebar-nav {
  flex: 1;
}
.nav-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  padding: 10px 12px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 0.85rem;
  font-family: inherit;
  cursor: pointer;
  transition: all var(--transition);
}
.nav-btn:hover, .nav-btn.active {
  background: var(--bg-glass);
  border-color: var(--border);
  color: var(--text-primary);
}

.sidebar-footer {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 14px 6px 0;
  border-top: 1px solid var(--border);
}
.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 6px rgba(34, 197, 94, 0.5);
}
.status-text {
  font-size: 0.75rem;
  color: var(--text-muted);
}

/* ===== MAIN ===== */
.chat-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

/* Header */
.chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-secondary);
  backdrop-filter: blur(12px);
}
.header-info {
  display: flex;
  align-items: center;
  gap: 10px;
}
.header-info h2 {
  font-size: 1rem;
  font-weight: 600;
}
.header-badge {
  font-size: 0.65rem;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(139,92,246,0.15));
  color: var(--accent);
  font-weight: 600;
  letter-spacing: 0.04em;
}
.icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: transparent;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all var(--transition);
}
.icon-btn:hover {
  background: var(--bg-glass);
  color: var(--text-primary);
}

/* Chat area */
.chat-area {
  flex: 1;
  overflow-y: auto;
  padding: 24px 24px 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* Empty state */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: 1;
  gap: 14px;
  text-align: center;
  animation: fadeInUp 0.5s ease both;
}
.empty-icon {
  font-size: 3.5rem;
  margin-bottom: 4px;
}
.empty-state h3 {
  font-size: 1.3rem;
  font-weight: 600;
  background: linear-gradient(135deg, var(--text-primary), var(--accent));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
.empty-state p {
  color: var(--text-secondary);
  font-size: 0.88rem;
  max-width: 420px;
  line-height: 1.6;
}

/* Loading row inside chat */
.bubble-row {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  max-width: 80%;
}
.avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.bot-avatar {
  background: var(--bg-glass);
  color: var(--accent);
  border: 1px solid var(--border);
}

/* Error banner */
.error-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 24px;
  background: rgba(239, 68, 68, 0.1);
  border-top: 1px solid rgba(239, 68, 68, 0.2);
  color: #fca5a5;
  font-size: 0.82rem;
}
.error-banner button {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
  font-size: 1rem;
}

/* Input bar */
.input-bar {
  padding: 16px 24px 12px;
  border-top: 1px solid var(--border);
  background: var(--bg-secondary);
}
.input-wrapper {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  background: var(--bg-glass);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 6px 6px 6px 16px;
  transition: border-color var(--transition);
}
.input-wrapper:focus-within {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px var(--accent-glow);
}
.input-wrapper textarea {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-family: inherit;
  font-size: 0.9rem;
  resize: none;
  line-height: 1.5;
  padding: 8px 0;
  max-height: 120px;
}
.input-wrapper textarea::placeholder {
  color: var(--text-muted);
}
.send-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  border: none;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  cursor: pointer;
  flex-shrink: 0;
  transition: all var(--transition);
}
.send-btn:hover:not(:disabled) {
  transform: scale(1.05);
  box-shadow: 0 4px 16px var(--accent-glow);
}
.send-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.input-hint {
  text-align: center;
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-top: 8px;
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
  .sidebar {
    display: none;
  }
  .chat-area {
    padding: 16px;
  }
  .input-bar {
    padding: 12px 16px 8px;
  }
  .bubble-row {
    max-width: 92%;
  }
}
</style>
