// frontend/pages/index.tsx

import { 
  useQuery,
  useQueryClient,
  useMutation,
} from "@tanstack/react-query";

import type {
  User,
  Category,
  Transaction,
  MonthlyBalance,
  TransactionCreate,
} from "../lib/api";

import {
  getUsers,
  getCategories,
  getTransactions,
  getMonthlyBalance,
} from "../lib/api";

import CategoryPieChart     from "../components/CategoryPieChart";
import MonthlyBalanceChart  from "../components/MonthlyBalanceChart";
import TransactionForm      from "../components/TransactionForm";

export default function Home() {
  
  const {
    data: users,
    isLoading: uLoading,
    isError: uError,
  } = useQuery<User[], Error>({
    queryKey: ["users"],
    queryFn: getUsers,
  });

  const {
    data: categories,
    isLoading: cLoading,
    isError: cError,
  } = useQuery<Category[], Error>({
    queryKey: ["categories"],
    queryFn: getCategories,
  });

  const {
    data: transactions,
    isLoading: tLoading,
    isError: tError,
  } = useQuery<Transaction[], Error>({
    queryKey: ["transactions"],
    queryFn: getTransactions,
  });

  const {
    data: balance,
    isLoading: bLoading,
    isError: bError,
  } = useQuery<MonthlyBalance[], Error>({
    queryKey: ["monthly-balance", 2025],
    queryFn: () => getMonthlyBalance(2025),
  });

  const isLoading = uLoading || cLoading || tLoading || bLoading;
  const isError = uError || cError || tError || bError;

  if (isLoading) return <p>Carregando dados...</p>;
  if (isError)   return <p>Erro ao carregar dados.</p>;

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-6">Meu Doce Dinheiro</h1>

     {/* Formulário modularizado */}
     <TransactionForm
        users      = {users!}
        categories = {categories!} 
        onSubmit   = {function (data: TransactionCreate):
          void {throw new Error("Function not implemented.");}}
      />

      {/* Usuários */}
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Usuários</h2>
        <ul className="list-disc pl-6">
          {users!.map(u => (
            <li key={u.id}>
              {u.name} ({u.email})
            </li>
          ))}
        </ul>
      </section>

      {/* Categorias */}
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Categorias</h2>
        <ul className="list-disc pl-6">
          {categories!.map(c => (
            <li key={c.id}>{c.name}</li>
          ))}
        </ul>
      </section>

      {/* Transações */}
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Transações</h2>
        <ul className="list-disc pl-6">
          {transactions!.map(tx => (
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
        <h2 className="text-xl font-semibold mb-4">
          Despesas por Categoria
        </h2>
        <CategoryPieChart
          transactions={transactions!}
          categories={categories!}
        />
      </section>

      {/* Gráfico de Linha */}
      <section>
        <h2 className="text-xl font-semibold mb-4">
          Saldo Mensal (2025)
        </h2>
        <MonthlyBalanceChart year={2025} />
      </section>
    </main>
  );
}
