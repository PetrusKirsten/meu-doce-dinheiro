// frontend/components/CategoryForm.tsx

import React from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createCategory } from "../lib/api";
import type { Category } from "../lib/api";

export default function CategoryForm() {
  const queryClient = useQueryClient();

  const mutation = useMutation<Category, Error, { name: string }>({
    mutationFn : createCategory,
    onSuccess  : () => {queryClient.invalidateQueries({ queryKey: ["categories"] });},
  });

  const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    const form    = e.currentTarget;
    const payload = {name: (form.elements.namedItem("name") as HTMLInputElement).value,};
    mutation.mutate(payload);
    form.reset();
  };

  return (
    <section className="mb-8">
      
      <h2 className="text-xl font-semibold mb-2">
        Nova Categoria
      </h2>
      
      <form 
        onSubmit  = {handleSubmit}
        className = "grid gap-2 max-w-xs">

        <input 
            name        = "name"
            placeholder = "Nome da categoria" 
            required 
            className   = "border p-1" />
        
        <button
          type      = "submit"
          disabled  = {mutation.status === "pending"}
          className = "bg-yellow-600 text-white p-2 rounded disabled:opacity-50">
          
          {mutation.status === "pending" ? "Enviando…" : "Criar Categoria"}

        </button>
        
        {mutation.status === "error" && (
          <p className="text-red-600">
            Erro ao criar categoria.
          </p>
        )}

      </form>

    </section>
    
  );
}
