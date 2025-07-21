// frontend/lib/api/index.ts

export * from "./types";
export * from "./users";
export * from "./client";
export * from "./reports";
export * from "./categories";
export * from "./transactions";

const API = process.env.NEXT_PUBLIC_API_URL

export async function createUser(data: { name: string, email: string, password: string }) {
  const res = await fetch(`${API}/users`, {
    method  : 'POST',
    headers : { 'Content-Type': 'application/json' },
    body    : JSON.stringify(data),
  })
  
  if (!res.ok) throw new Error('Erro no cadastro')
    
  return res.json()
}
