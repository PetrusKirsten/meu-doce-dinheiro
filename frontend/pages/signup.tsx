import { useState }  from 'react'
import { useRouter } from 'next/router'

import { createUser } from '../lib/api'

export default function SignUpPage() {
  const router = useRouter()

  const [name, setName]         = useState('')
  const [email, setEmail]       = useState('')
  const [password, setPassword] = useState('')

  const [error, setError] = useState<string | null>(null)

  const [loading, setLoading] = useState(false)

  const handle = async (e: React.FormEvent) => {
    e.preventDefault()
    setError(null)
    setLoading(true)

    try {
      const newUser = await createUser({ name, email, password })
      console.log('Usuário criado:', newUser)
    
      router.replace('/login')

    } catch (err: any) {
      setError(err.message)
      
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-md mx-auto mt-20 p-6 shadow-lg bg-white rounded-lg">
      <h1 className="text-2xl font-bold mb-4">Cadastro</h1>
      <form onSubmit={handle} className="space-y-4">
        <div>
          <label className="block mb-1">Nome</label>

          <input
            type="text"
            value={name}
            onChange={e => setName(e.target.value)}
            className="w-full border px-3 py-2 rounded"
            required
          />

        </div>
        <div>
          <label className="block mb-1">Email</label>

          <input
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            className="w-full border px-3 py-2 rounded"
            required
          />

        </div>
        <div>
          <label className="block mb-1">Senha</label>

          <input
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            className="w-full border px-3 py-2 rounded"
            required
          />

        </div>
        {error && <p className="text-red-500">{error}</p>}

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded">
          {loading ? 'Cadastrando…' : 'Criar Conta'}
        </button>
      </form>

      <p className="mt-4 text-sm text-center">
        Já tem conta?{' '}
        <span
          onClick={() => router.push('/login')}
          className="text-blue-600 hover:underline cursor-pointer">
          Entrar
        </span>
      </p>
    </div>
  )
}
