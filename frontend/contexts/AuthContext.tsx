import React, { createContext, useContext, useState, ReactNode, useEffect } from 'react'

const jwtDecode = require('jwt-decode') as (token: string) => any;

interface User {
  id    : number
  email : string
}

interface AuthContextType {
  user   :  User | null
  token  : string | null
  login  : (token: string) => void
  logout : () => void
}

const AuthContext = createContext<AuthContextType>({
  user   : null,
  token  : null,
  login  : () => {},
  logout : () => {},
})

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser]   = useState<User | null>(null)
  const [token, setToken] = useState<string | null>(null)

  // tenta recuperar do localStorage quando a app sobe
  useEffect(() => {
    const stored = localStorage.getItem('token')
    if (stored) login(stored)
  }, [])

  function login(newToken: string) {
    localStorage.setItem('token', newToken)
    setToken(newToken)
    const decoded = jwtDecode(newToken) as { sub: number; email: string }
    setUser({ id: decoded.sub, email: decoded.email })
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

// hook pra usar no resto da app
export const useAuth = () => useContext(AuthContext)
