// frontend/lib/api/transactions.ts
import { fetcher } from "./client";
import type { Transaction, TransactionCreate } from "./types";

/** GET /transactions/ */
export function getTransactions(): Promise<Transaction[]> {
  return fetcher("/transactions/");
}

/** GET /transactions/{id} */
export function getTransaction(id: number): Promise<Transaction> {
  return fetcher(`/transactions/${id}`);
}

/** POST /transactions/ */
export function createTransaction(payload: TransactionCreate): Promise<Transaction> {
  return fetcher("/transactions/", {
    method  : "POST",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}
