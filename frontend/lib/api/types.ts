// frontend/lib/api/types.ts

// shape dos dados (espelhando schemas Pydantic)

export interface User {
  id: number;
  name: string;
  email: string;
}

export interface Category {
  id: number;
  name: string;
}

export interface Transaction {
  id: number;
  amount: number;
  date: string;        // ISO string
  description?: string;
  category_id: number;
  owner_id: number;
}

export interface TransactionCreate {
  amount: number;
  date: string;
  description?: string;
  category_id: number;
  owner_id: number;
}

export interface MonthlyBalance {
  month: string;   // ex: "2025-07"
  balance: number; // receitas - despesas
}
