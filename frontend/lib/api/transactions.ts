// frontend/lib/api/transactions.ts
import { fetcher } from "./client";
import type { Transaction, TransactionCreate } from "./types";

/** GET /transactions/ */
export function getTransactions():

Promise<Transaction[]> {
  return fetcher("/transactions/");
}

/** GET /transactions/{id} */
export function getTransaction(id: number):

Promise<Transaction> {
  return fetcher(`/transactions/${id}`);
}

/** POST /transactions/ */
export function createTransaction(payload: TransactionCreate):

Promise<Transaction> {
  return fetcher("/transactions/", {
    method  : "POST",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}

/** PUT /transactions/{id} */
export function updateTransaction(
  id      : number,
  payload : Partial<Omit<Transaction, "id">>): 
  
  Promise<Transaction> {
  return fetcher(`/transactions/${id}`, {
    method  : "PUT",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}

/** DELETE /transactions/{id} */
export function deleteTransaction(id: number):

Promise<void> {
  return fetcher(`/transactions/${id}`, { method: "DELETE" });
}
