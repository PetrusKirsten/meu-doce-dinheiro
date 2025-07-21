// frontend/contexts/AuthContext.tsx
import React, { createContext, useContext, useState, ReactNode, useEffect } from 'react'

const jwtDecode = require('jwt-decode') as (token: string) => any;
export interface User {
  id: number
  name: string
  email: string
  onboarded: boolean
}

interface AuthContextType {
  user: User | null
  token: string | null
  login: (token: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  token: null,
  login: async () => {},
  logout: () => {},
})

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(null)
  const [user, setUser] = useState<User | null>(null)

  // ao montar, tenta recuperar o token
  useEffect(() => {
    const stored = localStorage.getItem('token')
    if (stored) {
      login(stored)
    }
  }, [])

  // login agora busca o perfil completo
  async function login(newToken: string) {
    localStorage.setItem('token', newToken)
    setToken(newToken)

    // opcional: decodifica só pra ter id/email rápido
    const { sub: id } = jwtDecode(newToken) as { sub: number }
    // const { sub: id } = jwtDecode(newToken) as { sub: number; email: string }
        
    // busca o usuário inteiro (incluindo onboarded)
    const res = await fetch('/api/users/me', {
      headers: { Authorization: `Bearer ${newToken}` },
    })
    if (!res.ok) throw new Error('Falha ao buscar perfil')
    const fullUser = (await res.json()) as User
    setUser(fullUser)
  }

  function logout() {
    localStorage.removeItem('token')
    setToken(null)
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
