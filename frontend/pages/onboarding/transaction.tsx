// frontend/pages/onboarding/transaction.tsx

// 1) Built-in / React
import { useState } from 'react'

// 2) Terceiros
import { useRouter } from 'next/router'
import { useMutation, useQueryClient } from '@tanstack/react-query'

// 3) Contextos / Hooks da app
import { useAuth } from '../../contexts/AuthContext'

// 4) Componentes
import TransactionForm from '../../components/TransactionForm'

// 5) Serviços / Tipos
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
  const router = useRouter();
  const queryClient = useQueryClient();
  const [error, setError] = useState<string | null>(null);

  const mutation = useMutation<Transaction, Error, TransactionInput>({
    // Aqui fazemos o mapeamento:
    mutationFn: (values) => {
      const { user } = useAuth()
      if (!user) throw new Error('Usuário não autenticado')
      
        const payload: TransactionCreate = {
        amount: values.amount,
        date: values.date,
        description: values.description,
        category_id: Number(values.categoryId),
        owner_id: user.id,
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