// frontend/pages/login.tsx

import { useState }  from 'react'
import { useRouter } from 'next/router'

import { useAuth } from '../contexts/AuthContext'

export default function LoginPage() {
  const router    = useRouter()
  const { login } = useAuth()

  const [email, setEmail]       = useState('')
  const [password, setPassword] = useState('')

  const [error, setError]       = useState<string | null>(null)

  const handle = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
        
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      })

      if (!res.ok) throw new Error('Credenciais inválidas')
        
      const { access_token } = await res.json()
      await login(access_token)
      // após login, o AuthContext redireciona pro onboarding ou dashboard
      router.replace('/')
    } catch (e: any) {
      setError(e.message)
    }
  }

  return (
    <div className="max-w-md mx-auto mt-20 p-4 shadow-lg">
      <h1 className="text-2xl mb-4">Login</h1>
      <form onSubmit={handle} className="space-y-4">
        <div>
          <label className="block mb-1">Email</label>
          <input
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            className="w-full border px-3 py-2 rounded"
          />
        </div>
        <div>
          <label className="block mb-1">Senha</label>
          <input
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            className="w-full border px-3 py-2 rounded"
          />
        </div>
        {error && <p className="text-red-500">{error}</p>}
        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded"
        >
          Entrar
        </button>
      </form>
    </div>
  )
}
