<script setup>
import { ref, computed } from "vue";
import { useTransactionStore } from "@/stores/transactionStore";

const store = useTransactionStore();

const goalname_input = ref("");
const goalsum_input = ref("");
const error = ref("");
const isOpen = ref(false);

function toggle() {
  isOpen.value = !isOpen.value;
}

function addGoal() {
  if (
    goalname_input.value &&
    goalsum_input.value &&
    !isNaN(goalsum_input.value)
  ) {
    store.addGoal(goalname_input.value, goalsum_input.value);
    goalname_input.value = "";
    goalsum_input.value = "";
  } else {
    showError();
  }
}

function removeGoal(id) {
  store.removeTransaction(id);
}
</script>


<template>
<button id = "goal-show-button" @click="toggle">{{ $t('goals.toggle') }}</button>

  <div v-if="isOpen">
<input class = "goal-selector" v-model="goalname_input" :placeholder="$t('goals.namePlaceholder')" />
<input class = "goal-selector" v-model="goalsum_input" :placeholder="$t('goals.valuePlaceholder')" />

<button id = "addGoal" @click="addGoal">{{ $t('goals.add') }}</button>

    <table>
      <tr
        v-for="goal in store.list.filter(t => t.type === 'goal')"
        :key="goal.id"
      >
        <td><p class = "goal-indicator">{{ goal.name }}</p></td>
        <td><p class = "goal-indicator">{{ goal.amount }} €</p></td>
        <td>
         <button id = "removeGoal" @click="removeGoal(goal.id)">{{ $t('goals.remove') }}</button>
        </td>
      </tr>
    </table>

    <h3>
      {{ $t('goals.total') }}:
      {{
        store.list
          .filter(t => t.type === 'goal')
          .reduce((sum, g) => sum + g.amount, 0)
      }} €
    </h3>
  </div>
</template>


<style scoped></style>
