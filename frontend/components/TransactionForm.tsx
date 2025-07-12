// frontend/components/TransactionForm.tsx
import React from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createTransaction } from "../lib/api";
import type { Transaction, TransactionCreate, Category, User } from "../lib/api";

interface Props {
  users: User[];
  categories: Category[];
}

export default function TransactionForm({ users, categories }: Props) {
  const queryClient = useQueryClient();

    const mutation = useMutation<Transaction, Error, TransactionCreate>({
    mutationFn: (tx) => createTransaction(tx),
    onSuccess : ()   => {
        queryClient.invalidateQueries({ queryKey: ["transactions"] });
        queryClient.invalidateQueries({ queryKey: ["monthly-balance", new Date().getFullYear()] });
        },}
    );

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = e.currentTarget;
    const data: TransactionCreate = {
      amount      : Number((form.amount as HTMLInputElement).value),
      date        : (form.date as HTMLInputElement).value,
      description : (form.description as HTMLInputElement).value || undefined,
      category_id : Number((form.category_id as HTMLSelectElement).value),
      owner_id    : Number((form.owner_id as HTMLSelectElement).value),
    };
    mutation.mutate(data);
    form.reset();
  };

  return (
    <section className="mb-8">

      <h2 className="text-xl font-semibold mb-2">
        Nova Transação
      </h2>

      <form 
        onSubmit  = {handleSubmit}
        className = "grid gap-2 max-w-md">

        <input 
            name        = "amount"
            type        = "number" 
            step        = "0.01"
            placeholder = "Valor" 
            required
            className   = "border p-1"
        />
        
        <input 
            name      = "date"
            type      = "date"
            required  
            className = "border p-1"
        />
        
        <input 
            name        = "description" 
            placeholder = "Descrição" 
            className   = "border p-1"
        />
        
        <select 
            name      = "category_id" 
            required 
            className = "border p-1">
          <option value="">
            Categoria
          </option>
          {categories.map(c => (<option key={c.id} value={c.id}>{c.name}</option>))}
        </select>

        <select name="owner_id" required className="border p-1">
          <option value="">
            Usuário
          </option>
          {users.map(u => (<option key={u.id} value={u.id}>{u.name}</option>))}
        </select>
        
        <button disabled={mutation.status === "pending"}>
            {mutation.status === "pending" ? "Enviando…" : "Adicionar"}
        </button>
        
        {mutation.status === "error" && (
            <p className="text-red-600">Erro ao criar transação.</p>
        )}
        
        {mutation.isError && <p className="text-red-600">Erro ao criar transação.</p>}

      </form>
    </section>
  );
}
