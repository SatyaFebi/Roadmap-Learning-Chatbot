<script setup>
const emit = defineEmits(['select'])

const suggestions = [
  { icon: '🍽️', label: 'Lihat Menu', prompt: 'Tampilkan semua menu yang tersedia' },
  { icon: '🥗', label: 'Menu Vegetarian', prompt: 'Apa saja menu vegetarian yang tersedia?' },
  { icon: '🍰', label: 'Desserts', prompt: 'Rekomendasikan dessert yang paling populer' },
  { icon: '🔥', label: 'Rekomendasi Chef', prompt: 'Apa rekomendasi chef hari ini?' },
]
</script>

<template>
  <div class="suggestions">
    <button
      v-for="s in suggestions"
      :key="s.label"
      class="chip"
      @click="emit('select', s.prompt)"
    >
      <span class="chip-icon">{{ s.icon }}</span>
      <span>{{ s.label }}</span>
    </button>
  </div>
</template>

<style scoped>
.suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
}
.chip {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 16px;
  background: var(--bg-glass);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  color: var(--text-primary);
  font-size: 0.82rem;
  font-family: inherit;
  cursor: pointer;
  transition: all var(--transition);
  white-space: nowrap;
}
.chip:hover {
  background: var(--bg-glass-hover);
  border-color: var(--border-focus);
  transform: translateY(-1px);
}
.chip-icon {
  font-size: 1rem;
}
</style>
