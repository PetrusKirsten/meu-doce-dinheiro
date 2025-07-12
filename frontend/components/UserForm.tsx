// frontend/components/UserForm.tsx
import React from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createUser } from "../lib/api";
import type { User } from "../lib/api";

export default function UserForm() {
  const queryClient = useQueryClient();

  const mutation = useMutation<User, Error, { name: string; email: string; password: string }>({
    mutationFn : createUser,
    onSuccess  : () => {queryClient.invalidateQueries({ queryKey: ["users"] });},
  });

  const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();
    const form    = e.currentTarget;
    const payload = {
      name     : (form.elements.namedItem("name")     as HTMLInputElement).value,
      email    : (form.elements.namedItem("email")    as HTMLInputElement).value,
      password : (form.elements.namedItem("password") as HTMLInputElement).value,
    };
    mutation.mutate(payload);
    form.reset();
  };

  return (
    <section className="mb-8">
      
      <h2 className="text-xl font-semibold mb-2">
        Novo Usuário
      </h2>
      
      <form 
        onSubmit  = {handleSubmit}
        className = "grid gap-2 max-w-md">
        
        <input
            name        = "name"
            placeholder = "Nome"
            required 
            className   = "border p-1"
        />
        
        <input 
            name        = "email"
            type        = "email"
            placeholder = "Email"
            required 
            className   = "border p-1"
        />
        
        <input
          name        = "password"
          type        = "password"
          placeholder = "Senha"
          required
          className   = "border p-1"
        />
        
        <button
          type      = "submit"
          disabled  = {mutation.status === "pending"}
          className = "bg-green-600 text-white p-2 rounded disabled:opacity-50">

          {mutation.status === "pending" ? "Enviando…" : "Criar Usuário"}

        </button>
        
        {mutation.status === "error" && (
          <p className="text-red-600">
            Erro ao criar usuário.
          </p>
        )}
      
      </form>

    </section>

  );
}
