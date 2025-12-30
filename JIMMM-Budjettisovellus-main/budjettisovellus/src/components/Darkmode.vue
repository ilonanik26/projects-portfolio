<template>
  <div>
    <button id = "darkmodetoggle" @click="toggleDarkMode">
      {{ isDark ? $t('theme.light') : $t('theme.dark') }}

    </button>

  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const isDark = ref(false)

const toggleDarkMode = () => {
  isDark.value = !isDark.value
}

watch(isDark, (val) => {
  if (val) {
    document.body.classList.add('dark-mode')
  } else {
    document.body.classList.remove('dark-mode')
    }
})
</script>

<style>

body {
  background-color: #ffffff;
  color: #000000;
}


body.dark-mode {
  background-color: #121212;
  color: #ffffff;
}
</style>
