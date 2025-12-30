<template>
  <select id="localetoggle" :value="locale" @change="changeLocale">
    <option value="fi">Suomi</option>
    <option value="en">English</option>
  </select>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()

const changeLocale = (e) => {
  locale.value = e.target.value
  localStorage.setItem('locale', e.target.value)
}
</script>

<style scoped>
select {
  margin-left: 10px;
  padding: 4px 8px;
}
</style>

