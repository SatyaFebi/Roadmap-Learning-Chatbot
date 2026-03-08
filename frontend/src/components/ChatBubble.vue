<script setup>
const props = defineProps({
  msg: Object,
})

const isUser = props.msg.role === 'user'
</script>

<template>
  <div class="bubble-row" :class="{ 'is-user': isUser }">
    <!-- Avatar -->
    <div v-if="!isUser" class="avatar bot-avatar">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2a4 4 0 0 1 4 4v2a4 4 0 0 1-8 0V6a4 4 0 0 1 4-4z"/>
        <path d="M16 14H8a4 4 0 0 0-4 4v2h16v-2a4 4 0 0 0-4-4z"/>
        <circle cx="12" cy="6" r="1.5" fill="currentColor" stroke="none"/>
      </svg>
    </div>

    <!-- Message bubble -->
    <div class="bubble" :class="isUser ? 'user-bubble' : 'bot-bubble'">
      <p v-for="(line, i) in msg.text.split('\n')" :key="i">
        {{ line }}<br v-if="i < msg.text.split('\n').length - 1" />
      </p>
    </div>
  </div>
</template>

<style scoped>
.bubble-row {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  max-width: 80%;
  animation: fadeInUp 0.3s ease both;
}
.bubble-row.is-user {
  margin-left: auto;
  flex-direction: row-reverse;
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

.bubble {
  padding: 12px 16px;
  border-radius: var(--radius-md);
  line-height: 1.6;
  font-size: 0.9rem;
  word-break: break-word;
}
.user-bubble {
  background: var(--bg-user-msg);
  color: #fff;
  border-bottom-right-radius: 4px;
}
.bot-bubble {
  background: var(--bg-bot-msg);
  color: var(--text-primary);
  border: 1px solid var(--border);
  border-bottom-left-radius: 4px;
}
</style>
