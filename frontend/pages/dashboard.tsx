// frontend/pages/dashboard.tsx

import React, { useEffect } from 'react'
import { useQuery } from '@tanstack/react-query'
import { useRouter } from 'next/router'
import { useAuth } from '../contexts/AuthContext'
import DashboardSummaryCard from '../components/DashboardSummaryCard'
import { Button } from '../components/ui/button'

const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface Summary {
  balance      : number
  monthExpense : number
  dailyAvg     : number
}

export default function DashboardPage() {
  const router   = useRouter()
  const { user } = useAuth()

  // Redireciona não autenticados para login
  useEffect(() => {
    if (user === null) {
      router.replace('/login')
    }
  }, [user, router])

  // Redireciona para onboarding se não tiver completado
  useEffect(() => {
    if (user && !user.onboarded) {
      router.replace('/onboarding')
    }
  }, [user, router])

  const { data, error, isLoading } = useQuery<Summary, Error>({
    
    queryKey: ['summary'],
    
    queryFn: async () => {
      const res = await fetch(`${API}/reports/summary`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      })
      if (!res.ok) {
        throw new Error('Erro ao buscar resumo de conta')
      }
      return res.json()
    },
    retry: false,
  })

  if (user === null) return <p>Carregando usuário...</p>
  if (isLoading) return <p>Carregando resumo...</p>
  if (error) return <p className="text-red-500">Erro: {error.message}</p>

  return (
    <div className="p-4 space-y-6">
    
      <h1 className="text-3xl font-bold">Dashboard</h1>
    
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <DashboardSummaryCard title="Saldo Total" value={data.balance} />
        <DashboardSummaryCard title="Despesa do Mês" value={data.monthExpense} />
        <DashboardSummaryCard title="Média Diária" value={data.dailyAvg} />
    
      </div>
    
      <div className="flex space-x-4 mt-6">
        <Button onClick={() => router.push('/onboarding/transaction')}>Adicionar Transação</Button>
        <Button onClick={() => router.push('/reports/summary')}>Ver Relatórios</Button>
      </div>
    
    </div>
  )
}
