// frontend/lib/api/categories.ts
import { fetcher } from "./client";
import type { Category } from "./types";

/** GET /categories/ */
export function getCategories(): 

Promise<Category[]> {
  return fetcher("/categories/");
}

/** POST /categories/ */
export function createCategory(payload: { name: string }): 

Promise<Category> {
  return fetcher("/categories/", {
    method  : "POST",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}

/** PUT /categories/:id */
export function updateCategory(
  id: number,
  payload: Partial<Pick<Category, "name">>):
  
  Promise<Category> {
  return fetcher(`/categories/${id}`, {
    method  : "PUT",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}

/** DELETE /categories/:id */
export function deleteCategory(id: number):

Promise<void> {
  return fetcher(`/categories/${id}`, { method: "DELETE" });
}

/** Fetch categories from the API */
export async function fetchCategories(): Promise<Category[]> {
  const res = await fetch('/api/categories');
  if (!res.ok) throw new Error('Erro ao buscar categorias');
  return res.json();
}

