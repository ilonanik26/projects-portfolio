<script setup>
import { ref } from "vue";
import { useTransactionStore } from "../stores/transactionStore";

const store = useTransactionStore();

// Otetaan nykyinen päivä oletusarvoksi YYYY-MM-DD muodossa
const today = new Date().toISOString().split("T")[0];
//matiaksen lisäämä


// Lomakkeen tilan määrittely
const type = ref("expense"); // 'expense' tai 'income'
const amount = ref(0);
const description = ref("");
const date = ref(today); // UUSI: Päivämäärä tila (matias)

function handleSubmit() {
  if (amount.value <= 0) {
    alert("Summan on oltava positiivinen luku!");
    return;
  }

  let finalAmount = parseFloat(amount.value);

  if (type.value === "expense") {
    // Jos meno, tallenna negatiivisena
    finalAmount = -Math.abs(finalAmount);
  } else {
    // Jos tulo, tallenna positiivisena
    finalAmount = Math.abs(finalAmount);
  }

  // Kutsutaan Pinia Store -toimintoa datan tallentamiseksi
  store.addTransaction({
    type: type.value,
    amount: finalAmount,
    description: description.value,
    date: date.value, // LISÄTTY: Päivämäärä lähetetään storeen
  });

  // Nollaa lomakkeen kentät lähetettyä
  amount.value = 0;
  description.value = "";
  date.value = today; // Asetetaan takaisin tähän päivään
}
</script>

<template>
  <div class="form-container">
    <h3 id = "formTitle">{{ $t('form.title') }}</h3>
    <form @submit.prevent="handleSubmit">

      <div class="form-group">
          <label class="form-label" for="date">{{ $t('form.date') }}:</label>
          <input
            class="expence-selector"
            id="date"
            type="date"
            v-model="date"
            required
          />
      </div>

      <div class="form-group">
      <label class="form-label" for="type">{{ $t('form.type') }}:</label>
        <select class="expence-selector" id="type" v-model="type">
        <option value="expense">{{ $t('form.expense') }}</option>
        <option value="income">{{ $t('form.income') }}</option>
        </select>
      </div>

      <div class="form-group">
        <label class="form-label" for="description">{{ $t('form.description') }}:</label>
        <input
          class="expence-selector"
          id="description"
          type="text"
          v-model="description"
          required
       :placeholder="$t('form.placeholder')"
      />
      </div>

      <div class="form-group">
       <label class="form-label" for="amount">{{ $t('form.amount') }}</label>

        <input
          class="expence-selector"
          id="amount"
          type="number"
          v-model.number="amount"
          min="0"
          step="0.01"
          required
        />
      </div>

      <button
      id="submitter"
  type="submit"
  :class="{
    'btn-expense': type === 'expense',
    'btn-income': type === 'income',
  }"
>
 {{ type === "expense" ? $t('form.submitExpense') : $t('form.submitIncome') }}
</button>
    </form>
  </div>
</template>
