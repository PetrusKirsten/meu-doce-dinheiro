// frontend/lib/api/categories.ts
import { fetcher } from "./client";
import type { Category } from "./types";

/** GET /categories/ */
export function getCategories(): Promise<Category[]> {
  return fetcher("/categories/");
}

/** POST /categories/ */
export function createCategory(payload: { name: string }): Promise<Category> {
  return fetcher("/categories/", {
    method  : "POST",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}
