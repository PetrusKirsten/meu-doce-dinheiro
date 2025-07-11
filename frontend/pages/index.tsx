// frontend/pages/index.tsx
import { useEffect, useState } from "react";
import { getUsers, getCategories, User, Category } from "../lib/api";

export default function Home() {
  const [users, setUsers]           = useState<User[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading]       = useState(true);
  const [error, setError]           = useState<string | null>(null);

  useEffect(() => {
    Promise.all([getUsers(), getCategories()])
      .then(([u, c]) => {
        setUsers(u);
        setCategories(c);
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
    </main>
  );
}
