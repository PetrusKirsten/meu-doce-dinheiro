// frontend/pages/onboarding/category.tsx

import { useState, useEffect } from 'react';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { useRouter } from 'next/router';

import { createCategory } from '../../lib/api';
import { useAuth }        from '../../contexts/AuthContext'
import CategoryForm       from '../../components/CategoryForm';

// no topo do componente

export default function CategorySetup() {

  const router  = useRouter();
  const { user } = useAuth();

  useEffect(() => {
    if (user?.onboarded) router.replace('/dashboard')
  }, [user, router])

  if (user === null) return <p>Carregando...</p>

  const queryClient       = useQueryClient();
  const [error, setError] = useState<string | null>(null);

  const mutation = useMutation<{ name: string }, unknown, { name: string }>({
    mutationFn: createCategory,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categories'] });
      router.push('/onboarding/transaction');
    },
    onError: () => setError('Erro ao criar categoria'),
  });

  const handleSubmit = (values: { name: string }) => {
    setError(null);
    mutation.mutate(values);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-50">
      <h2 className="text-2xl font-bold mb-4">Crie suas categorias iniciais</h2>

      <CategoryForm onSubmit={handleSubmit} />
      {error && <p className="text-red-500 mt-2">{error}</p>}

    </div>
  );
}
