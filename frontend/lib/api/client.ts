// frontend/lib/api/client.ts

const API_URL = process.env.NEXT_PUBLIC_API_URL;
if (!API_URL) {
  throw new Error("NEXT_PUBLIC_API_URL não está definida");
}

/**
 * fetcher genérico: faz fetch, trata HTTP errors e converte JSON.
 * @param path   caminho da API (ex: "/users/")
 * @param init   RequestInit opcional para POST, PUT, DELETE…
 */
export async function fetcher<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, init);
  if (!res.ok) {
    throw new Error(`${res.status} ${res.statusText}`);
  }
  return res.json();
}
