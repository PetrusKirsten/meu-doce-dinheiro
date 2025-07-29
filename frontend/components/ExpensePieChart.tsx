// frontend/components/ExpensePieChart.tsx

import React from 'react'
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { useQuery } from '@tanstack/react-query'

const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

// Interface para os dados de despesa por categoria retornados pela API
interface CategoryExpense {
  category : string
  total    : number
}

export default function ExpensePieChart() {
  
    const { data, isLoading, error } = useQuery<CategoryExpense[], Error>({
    queryKey: ['expensesByCategory'],
    queryFn: async () => {
      const res = await fetch(`${API}/reports/expenses-by-category`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      })
      if (!res.ok) throw new Error('Erro ao buscar despesas por categoria')
      return res.json()
    },
    retry: false,
  })

  if (isLoading) return <p>Carregando gráfico de despesas...</p>
  if (error) return <p className="text-red-500">Erro: {error.message}</p>

  // Cores para as fatias do gráfico
  const COLORS = ['#8884d8', '#82ca9d', '#ffc658', '#ff7300', '#0088FE', '#00C49F']

  return (
    <div className="w-full h-64">
      <ResponsiveContainer>
        <PieChart>

          <Pie
            data={data!}
            dataKey="total"
            nameKey="category"
            cx="50%"
            cy="50%"
            outerRadius={80}
            label>

            {data!.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}

          </Pie>
          
          <Tooltip
            formatter={(value: number) =>
              new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)
            }/>
          
          <Legend verticalAlign="bottom" height={36}/>
        
        </PieChart>
      </ResponsiveContainer>
    </div>
  )
}
