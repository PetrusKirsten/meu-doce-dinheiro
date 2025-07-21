// frontend/pages/onboarding/transaction.tsx

import { useState, useEffect } from 'react'

import { useRouter } from 'next/router'
import { useMutation, useQueryClient } from '@tanstack/react-query'

import { useAuth } from '../../contexts/AuthContext'

import TransactionForm from '../../components/TransactionForm'
import {
  createTransaction,
  Transaction,
  TransactionCreate,
} from '../../lib/api'


type TransactionInput = {
  amount       : number;
  categoryId   : string;
  date         : string;
  description? : string;
};

export default function FirstTransactionSetup() {
  const router   = useRouter()
  const { user } = useAuth()

  useEffect(() => {
    if (user?.onboarded) {
      router.replace('/dashboard')
    }
  }, [user, router])

  if (user === null) return <p>Carregando...</p>

  const queryClient       = useQueryClient()
  const [error, setError] = useState<string | null>(null)

  const mutation = useMutation<Transaction, Error, TransactionInput>({
    
    mutationFn: (values) => {
      const { user } = useAuth()
      if (!user) throw new Error('Usuário não autenticado')
      
        const payload: TransactionCreate = {
        amount      : values.amount,
        date        : values.date,
        description : values.description,
        category_id : Number(values.categoryId),
        owner_id    : user.id,
      };
      return createTransaction(payload);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['transactions'] });
      router.push('/dashboard');
    },
    onError: () => setError('Erro ao criar transação'),
  });

  const handleSubmit = (values: TransactionInput) => {
    setError(null);
    mutation.mutate(values);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-50">
      <h2 className="text-2xl font-bold mb-4">Insira sua primeira transação</h2>
      <TransactionForm onSubmit={handleSubmit} />
      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
}