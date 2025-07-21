// frontend/pages/onboarding/index.tsx

import { useEffect } from 'react'
import { useRouter } from 'next/router'

import { useAuth } from '../../contexts/AuthContext'
import { Button }  from '../../components/ui/button'

export default function WelcomeScreen() {
  const router  = useRouter()
  const { user } = useAuth()

  useEffect(() => {
    if (user?.onboarded) {
      router.replace('/dashboard')
    }
  }, [user, router])

  // opcional: enquanto o user ainda é null (carregando), mostra um loader
  if (user === null) return <p>Carregando...</p>

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-50">
      <h1 className="text-3xl font-bold mb-4 text-center">
        Bem-vindo ao Meu Doce Dinheiro!
      </h1>
      <p className="mb-6 text-center max-w-md">
        Vamos te ajudar a organizar suas finanças de forma simples e visual. Bora criar suas categorias?
      </p>
      <Button onClick={() => router.push('/onboarding/category')}>
        Começar
      </Button>
    </div>
  )
}
