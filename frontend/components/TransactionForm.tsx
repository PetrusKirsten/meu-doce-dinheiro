// frontend/components/TransactionForm.tsx

import React, { FormEvent } from "react";
import type { TransactionCreate, Category, User } from "../lib/api";

interface Props {
  users: User[];
  categories: Category[];
  onSubmit: (data: TransactionCreate) => void;
  isLoading?: boolean;
  error?: boolean;
}

export default function TransactionForm({
  users,
  categories,
  onSubmit,
  isLoading = false,
  error = false,
}: Props) {
  function handleSubmit(e: FormEvent<HTMLFormElement>) {

    e.preventDefault();

    const form = e.currentTarget;
    const data: TransactionCreate = {
      amount      : Number((form.amount as HTMLInputElement).value),
      date        : (form.date as HTMLInputElement).value,
      description : (form.description as HTMLInputElement).value,
      category_id : Number((form.category_id as HTMLSelectElement).value),
      owner_id    : Number((form.owner_id as HTMLSelectElement).value),
    };

    onSubmit(data);
    form.reset();
  }

  return (
    <form onSubmit={handleSubmit} className="grid grid-cols-1 gap-2 max-w-md">
      <input
        name="amount"
        type="number"
        step="0.01"
        placeholder="Valor"
        required
        className="border p-1"/>

      <input
        name="date"
        type="date"
        required
        className="border p-1"/>

      <input
        name="description"
        placeholder="Descrição"
        className="border p-1"/>

      <select
        name="category_id"
        required
        className="border p-1">
        <option value="">Categoria</option>
        {categories.map(c => (
          <option key={c.id} value={c.id}>{c.name}</option>
        ))}
      </select>

      <select
        name="owner_id"
        required
        className="border p-1">
        <option value="">Usuário</option>
        {users.map(u => (
          <option key={u.id} value={u.id}>{u.name}</option>
        ))}
      </select>

      <button
        type="submit"
        disabled={isLoading}
        className="bg-blue-600 text-white p-2 rounded disabled:opacity-50">
        {isLoading ? "Enviando..." : "Adicionar"}
      </button>

      {error && <p className="text-red-600">Erro ao criar!</p>}

    </form>
  );
}
