// frontend/lib/api/users.ts
import { fetcher } from "./client";
import type { User } from "./types";

/** GET /users/ */
export function getUsers(): Promise<User[]> {
  return fetcher("/users/");
}

/** GET /users/{id} */
export function getUser(id: number): Promise<User> {
  return fetcher(`/users/${id}`);
}

/** POST /users/ */
export function createUser(payload: { name: string; email: string; password: string; }): Promise<User> {
  return fetcher("/users/", {
    method  : "POST",
    headers : { "Content-Type": "application/json" },
    body    : JSON.stringify(payload),
  });
}
