<template>
  <div class="calendar-wrapper">
    <VCalendar
      :attributes="calendarAttributes"
      is-expanded
    />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useTransactionStore } from '../stores/transactionStore';

const store = useTransactionStore();

// Muuntaa Pinia-storen tapahtumalistan V-Calendarin ymmärtämään muotoon (attributes)
const calendarAttributes = computed(() => {
  return store.list.map(t => {
    // Tapahtumat on tallennettu storeen YYYY-MM-DD muodossa, joka kelpaa V-Calendarille
    const dateString = t.date;

    // Määritellään väri tyypin mukaan (positiivinen = tulo, negatiivinen = meno)
    const color = t.amount > 0 ? 'green' : 'red';

    return {
      key: t.id,
      dates: dateString,
      dot: {
        color: color, // Piste päivän kohdalle
      },
      popover: {
        label: `${t.description} (${t.amount.toFixed(2)} €)`, // Tiedot hiiren päällä
      },
    };
  });
});
</script>

<style scoped>
.calendar-wrapper {
  margin-top: 20px;
  padding: 10px;
}
</style>
