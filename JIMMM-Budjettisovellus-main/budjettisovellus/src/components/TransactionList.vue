<script setup>
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { useTransactionStore } from "../stores/transactionStore";
import { useI18n } from "vue-i18n";


const store = useTransactionStore();
const { list: transactions } = storeToRefs(store);
const { t } = useI18n();
// Ei näytä tavoitteita muitten tapahtumien kanssa
const visibleTransactions = computed(() =>
  transactions.value.filter(t => t.type === "income" || t.type === "expense")
);

// Poistaa transaction
function handleDelete(id) {
  if (confirm(t('list.confirmDelete'))) {
    store.removeTransaction(id);
  }
}
</script>

<template>
  <div>
  <h2>{{ $t('list.title') }} ({{ visibleTransactions.length }})</h2>


    <ul class="transaction-list">
      <li
        v-for="t in visibleTransactions"
        :key="t.id"
        :class="t.type"
      >
        <div class="transaction-info">
          <span class="amount">{{ t.amount.toFixed(2) }} €</span>
          <span class="description">
            {{ t.description }} ({{ t.date }})
          </span>
          <button class="delete-btn" @click="handleDelete(t.id)">
         {{ $t('list.delete') }}
        </button>
        </div>
      </li>
    </ul>

    <p v-if="!visibleTransactions.length">{{ $t('list.empty') }}</p>
  </div>
</template>

<style scoped>
/* tyyli oman maun mukaan */
</style>
