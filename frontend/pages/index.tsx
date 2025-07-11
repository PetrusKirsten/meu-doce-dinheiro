// frontend/pages/index.tsx
import { useEffect, useState } from "react";
import {
  getUsers,
  getCategories,
  getTransactions,
  getMonthlyBalance,
  User,
  Category,
  Transaction,
  MonthlyBalance
} from "../lib/api";
import CategoryPieChart from "../components/CategoryPieChart";


export default function Home() {
  const [loading, setLoading]           = useState(true);
  const [users, setUsers]               = useState<User[]>([]);
  const [categories, setCategories]     = useState<Category[]>([]);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [error, setError]               = useState<string | null>(null);

  useEffect(() => {
    Promise.all([getUsers(), getCategories(), getTransactions()])
      .then(([u, c, txs]) => {
        setUsers(u);
        setCategories(c);
        setTransactions(txs);
      })
      .catch(err => {
        console.error(err);
        setError(err.message);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Carregando dados...</p>;
  if (error)   return <p>Erro: {error}</p>;

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard Básico</h1>

      <section className="mb-6">
        <h2 className="text-xl font-semibold">Usuários</h2>
        <ul className="list-disc pl-6">
          {users.map(u => (
            <li key={u.id}>{u.name} ({u.email})</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold">Categorias</h2>
        <ul className="list-disc pl-6">
          {categories.map(c => (
            <li key={c.id}>{c.name}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold">Transações</h2>
        <ul className="list-disc pl-6">
          {transactions.map(tx => (
            <li key={tx.id}>
              {new Date(tx.date).toLocaleDateString()} – 
              {tx.description ?? "(sem descrição)"}: 
              R$ {tx.amount.toFixed(2)}
            </li>
          ))}
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-xl font-semibold mb-2">Despesas por Categoria</h2>
        <CategoryPieChart
          transactions = {transactions}
          categories   = {categories}
        />
      </section>

    </main>
  );
}
