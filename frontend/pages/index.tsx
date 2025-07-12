// frontend/pages/index.tsx
import React from "react";
import { useQuery } from "@tanstack/react-query";

import {
  getUsers,
  getCategories,
  getTransactions,
  getMonthlyBalance,
} from "../lib/api";

import type {
  User,
  Category,
  Transaction,
  MonthlyBalance,
} from "../lib/api";

import TransactionForm     from "../components/TransactionForm";
import CategoryPieChart    from "../components/CategoryPieChart";
import MonthlyBalanceChart from "../components/MonthlyBalanceChart";

export default function Home() {
  // 1️⃣ Queries
  const {
    data      : users,
    isLoading : uLoading,
    isError   : uError,
  } = useQuery<User[], Error>({
    queryKey : ["users"],
    queryFn  : getUsers,
  });

  const {
    data      : categories,
    isLoading : cLoading,
    isError   : cError,
  } = useQuery<Category[], Error>({
    queryKey : ["categories"],
    queryFn  : getCategories,
  });

  const {
    data      : transactions,
    isLoading : tLoading,
    isError   : tError,
  } = useQuery<Transaction[], Error>({
    queryKey : ["transactions"],
    queryFn  : getTransactions,
  });

  const {
    data      : balance,
    isLoading : bLoading,
    isError   : bError,
  } = useQuery<MonthlyBalance[], Error>({
    queryKey : ["monthly-balance", new Date().getFullYear()],
    queryFn  : () => getMonthlyBalance(new Date().getFullYear()),
  });

  const isLoading = uLoading || cLoading || tLoading || bLoading;
  const isError   = uError   || cError   || tError   || bError;

  // 2️⃣ Estados de loading / erro
  if (isLoading) return <p>Carregando dados...</p>;
  if (isError)   return <p>Ocorreu um erro ao buscar os dados.</p>;

  // 3️⃣ Render
  return (
    <main className="p-4">
      <h1 className="text-3xl font-bold mb-6">Meu Doce Dinheiro</h1>

      {/* Formulário separado */}
      <TransactionForm users={users!} categories={categories!} />

      {/* Lista de Transações */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-2">Transações</h2>
        <ul className="list-disc pl-6">
          {transactions!.map((tx) => (
            <li key={tx.id}>
              {new Date(tx.date).toLocaleDateString()} –{" "}
              {tx.description ?? "(sem descrição)"}: R${" "}
              {tx.amount.toFixed(2)}
            </li>
          ))}
        </ul>
      </section>

      {/* Gráfico de Pizza */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">
          Despesas por Categoria
        </h2>
        <CategoryPieChart
          transactions={transactions!}
          categories={categories!}
        />
      </section>

      {/* Gráfico de Linha */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">
          Saldo Mensal ({new Date().getFullYear()})
        </h2>
        <MonthlyBalanceChart year={new Date().getFullYear()} />
      </section>
    </main>
  );
}
