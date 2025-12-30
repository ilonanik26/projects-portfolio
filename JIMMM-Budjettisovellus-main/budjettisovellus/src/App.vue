<script setup>
import { defineAsyncComponent } from 'vue'

const TransactionChart = defineAsyncComponent(() =>
  import('./components/TransactionChart.vue')
)

const TransactionCalendar = defineAsyncComponent(() =>
  import('./components/TransactionCalendar.vue')
)

import TransactionForm from "./components/TransactionForm.vue";
import TransactionList from "./components/TransactionList.vue";
import TransactionGoals from "./components/TransactionGoals.vue";
import Darkmode from "./components/Darkmode.vue";
import LocaleSwitcher from "./components/LocaleSwitcher.vue";
</script>

<template>
  <main>
   <h1>{{ $t('app.title') }}</h1>
    <Darkmode />
    <LocaleSwitcher />
    <hr />
    <div class="summary-area">
        <TransactionCalendar />
    </div>

    <TransactionForm />

    <hr />

    <TransactionList />

    <hr />

    <TransactionChart />

    <hr />

    <TransactionGoals />

  </main>
</template>

<style>
main {
  max-width: 1000px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

.summary-area {
    display: flex;
    justify-content: space-around;
    gap: 20px;
    flex-wrap: wrap;
}
</style>
