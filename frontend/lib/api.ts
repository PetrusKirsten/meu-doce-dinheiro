// frontend/lib/api.ts

// Puxa a URL base da API das variáveis de ambiente
const API_URL = process.env.NEXT_PUBLIC_API_URL;

// Define o shape dos dados (espelhando seus schemas Pydantic)
export interface User {
  id    : number;
  name  : string;
  email : string;
}

export interface Category {
  id   : number;
  name : string;
}

// Função para listar usuários (GET /users/)
export async function getUsers(): Promise<User[]> {
  const res = await fetch(`${API_URL}/users/`);
  if (!res.ok) {
    throw new Error(`Erro ao buscar usuários: ${res.status} ${res.statusText}`);
  }
  return res.json();
}

// Função para listar categorias (GET /categories/)
export async function getCategories(): Promise<Category[]> {
  const res = await fetch(`${API_URL}/categories/`);
  if (!res.ok) {
    throw new Error(`Erro ao buscar categorias: ${res.status} ${res.statusText}`);
  }
  return res.json();
}
