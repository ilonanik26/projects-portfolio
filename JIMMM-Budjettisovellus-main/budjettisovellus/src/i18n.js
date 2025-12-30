import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import fi from './locales/fi.json'

const savedLocale = localStorage.getItem('locale') || 'fi'

export const i18n = createI18n({
    legacy: false,
    locale: savedLocale,
    fallbackLocale: 'en',
    messages: { en, fi }
})
