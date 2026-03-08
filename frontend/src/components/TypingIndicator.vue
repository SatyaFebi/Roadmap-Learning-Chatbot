<template>
  <div class="typing-indicator">
    <span></span><span></span><span></span>
  </div>
</template>

<style scoped>
.typing-indicator {
  display: flex;
  gap: 5px;
  padding: 14px 18px;
  background: var(--bg-bot-msg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  border-bottom-left-radius: 4px;
  width: fit-content;
  animation: fadeInUp 0.3s ease both;
}
.typing-indicator span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  animation: pulse 1.4s ease-in-out infinite;
}
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
</style>
