// frontend/pages/index.tsx

import React from "react";
import { 
  useQuery,
  useMutation,
  useQueryClient 
} from "@tanstack/react-query";

import {
  getUsers,        deleteUser,
  getCategories,   deleteCategory,
  getTransactions, deleteTransaction,
  getMonthlyBalance,
} from "../lib/api";

import type {
  User,
  Category,
  Transaction,
  MonthlyBalance,
} from "../lib/api";

import UserForm            from "../components/UserForm";
import CategoryForm        from "../components/CategoryForm";
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
    data      : categories = [],
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

  const qc = useQueryClient();

  const delUser = useMutation<void, Error, number>({
    mutationFn : deleteUser,
    onSuccess  : () => qc.invalidateQueries({ queryKey: ["users"] }),
  });

  const delCat = useMutation<void, Error, number>({
    mutationFn : deleteCategory,
    onSuccess  : () => qc.invalidateQueries({ queryKey: ["categories"] }),
  });

  const delTx = useMutation<void, Error, number>({
    mutationFn : deleteTransaction,
    onSuccess  : () => qc.invalidateQueries({ queryKey: ["transactions"] }),
  });


  const isLoading = uLoading || cLoading || tLoading || bLoading;
  const isError   = uError   || cError   || tError   || bError;

  // 2️⃣ Estados de loading / erro
  if (isLoading) return <p>Carregando dados...</p>;
  if (isError)   return <p>Ocorreu um erro ao buscar os dados.</p>;

  // 3️⃣ Render
  return (
    <main className="p-4">

      <h1 className="text-3xl font-bold mb-6">
        Meu Doce Dinheiro
      </h1>

      {/* Lista de Usuários */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-2">Usuários</h2>
        <ul className="list-disc pl-6">
          {users.map(u => (
            <li key={u.id} className="flex items-center justify-between">
              <span>{u.name} ({u.email})</span>
              <button
                onClick   = {() => delUser.mutate(u.id)}
                disabled  = {delUser.status === "pending"}
                className = "text-red-600 hover:opacity-75"
                title     = "Excluir usuário">
                🗑️
              </button>
            </li>
          ))}
        </ul>
      </section>

      {/* Formulário de Usuário */}
      <UserForm />

      {/* Lista de Categorias */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-2">Categorias</h2>
        <ul className="list-disc pl-6">
          {categories.map(c => (
            <li key={c.id} className="flex items-center justify-between">
              <span>{c.name}</span>
              <button
                onClick   = {() => delCat.mutate(c.id)}
                disabled  = {delCat.status === "pending"}
                className = "text-red-600 hover:opacity-75"
                title     = "Excluir categoria">
                🗑️
              </button>
            </li>
          ))}
        </ul>
      </section>

      {/* Formulário de Categoria */}
      <CategoryForm />

      {/* Lista de Transações */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-2">Transações</h2>
        <ul className="list-disc pl-6">
          {transactions.map(tx => (
            <li key={tx.id} className="flex items-center justify-between">
              <span>
                {new Date(tx.date).toLocaleDateString()} –{" "}
                {tx.description ?? "(sem descrição)"}: R${" "}
                {tx.amount.toFixed(2)}
              </span>
              <button
                onClick   = {() => delTx.mutate(tx.id)}
                disabled  = {delTx.status === "pending"}
                className = "text-red-600 hover:opacity-75"
                title     = "Excluir transação">
                🗑️
              </button>
            </li>
          ))}
        </ul>
      </section>

      {/* Formulário de Transação */}
      <TransactionForm 
        users      = {users!}
        categories = {categories!} 
      />

      {/* Gráfico de Pizza */}
      <section className="mb-8">

        <h2 className="text-2xl font-semibold mb-4">
          Despesas por Categoria
        </h2>

        <CategoryPieChart
          transactions = {transactions!}
          categories   = {categories!}
        />

      </section>

      {/* Gráfico de Linha */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">
          Saldo Mensal ({new Date().getFullYear()})
        </h2>
        
        <MonthlyBalanceChart 
          year = {new Date().getFullYear()}
        />

      </section>
    </main>
  );
}
