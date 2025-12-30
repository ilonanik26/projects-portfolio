<template>
  <apexchart
    type="donut"
    height="300"
    :options="chartOptions"
    :series="series"
  />
</template>

<script setup>
import ApexCharts from "vue3-apexcharts";
import { computed } from "vue";
import { useTransactionStore } from "../stores/transactionStore";
import { useI18n } from "vue-i18n";


const store = useTransactionStore();
const { t } = useI18n();


const totalIncome = computed(() => store.totalIncome);
const totalExpense = computed(() => store.totalExpense);
const totalGoal = computed(() => store.totalGoal);

const saved = computed(() => Math.max(0, totalIncome.value - totalExpense.value));
const overGoal = computed(() => Math.max(0, totalExpense.value - totalGoal.value));
const used = computed(() => Math.min(totalExpense.value, totalGoal.value));
const remainingGoal = computed(() => Math.max(0, totalGoal.value - totalExpense.value));

const series = computed(() => [
  Number(saved.value) || 0,
  Number(used.value) || 0,
  Number(remainingGoal.value) || 0,
  Number(overGoal.value) || 0
]);

const chartOptions = computed(() => ({
  labels: [
    t('chart.labels.saved'),
    t('chart.labels.expense'),
    t('chart.labels.remainingGoal'),
    t('chart.labels.overGoal')
  ],
  colors: ["#2ecc71", "#e74c3c", "#007fff", "#ff9900"],
  plotOptions: { pie: { donut: { size: "50%" } } }
}))

</script>
