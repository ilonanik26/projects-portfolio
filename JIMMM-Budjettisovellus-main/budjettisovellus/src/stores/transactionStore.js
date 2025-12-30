import { defineStore } from "pinia";

export const useTransactionStore = defineStore("transactions", {
  state: () => ({
    list: [],
  }),

  getters: {
    totalIncome: state =>
      state.list
        .filter(t => t.type === "income")
        .reduce((sum, t) => sum + Math.abs(t.amount), 0),

    totalExpense: state =>
      state.list
        .filter(t => t.type === "expense")
        .reduce((sum, t) => sum + Math.abs(t.amount), 0),

    totalGoal: state =>
      state.list
        .filter(t => t.type === "goal")
        .reduce((sum, t) => sum + Math.abs(t.amount), 0),

    balance: state =>
      state.list.reduce((sum, t) => {
        if (t.type === "income") return sum + Math.abs(t.amount);
        if (t.type === "expense") return sum - Math.abs(t.amount);
        return sum;
      }, 0),
  },

actions: {
        addTransaction(transactionData) {
            const transaction = {
                id: Date.now(),
                // POISTETTU: date: new Date().toISOString().split("T")[0],
                // NYT KÄYTETÄÄN LOMAKKEELTA TULEVAA DATE-KENTTÄÄ:
                ...transactionData,
            };
      this.list.unshift(transaction);
    },

    addGoal(goalName, goalSum) {
      this.list.unshift({
        id: Date.now(),
        type: "goal",
        name: goalName,
        amount: Number(goalSum),
      });
    },

    removeTransaction(id) {
      this.list = this.list.filter(t => t.id !== Number(id));
    },

    updateTransaction(updatedTransaction) {
      const index = this.list.findIndex(t => t.id === updatedTransaction.id);
      if (index !== -1) {
        this.list[index] = updatedTransaction;
      }
    },
  },

  persist: true,
});