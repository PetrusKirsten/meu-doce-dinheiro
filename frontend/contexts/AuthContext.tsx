// frontend/contexts/AuthContext.tsx
import React, { createContext, useContext, useState, ReactNode, useEffect } from 'react'

import { parseJwt } from '../utils/jwt'


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
    
    const { sub: id } = parseJwt(newToken)
    
    // busca o usuário inteiro (incluindo onboarded)
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/users/`, 
      {
        headers: { 
          Authorization : `Bearer ${newToken}`,
          Accept        : 'application/json'
        },
      }
    )

    if (!res.ok) {
      console.error('status:', res.status, 'body:', await res.text())
      throw new Error('Falha ao buscar perfil')
    }
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
