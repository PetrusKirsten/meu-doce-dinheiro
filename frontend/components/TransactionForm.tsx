// frontend/components/TransactionForm.tsx

import React, { useState, useEffect } from 'react';
import { fetchCategories, Category } from '../lib/api';

interface Props {
  onSubmit: (values: {
    amount: number;
    categoryId: string;
    date: string;
    description?: string;
  }) => void;
}

const TransactionForm: React.FC<Props> = ({ onSubmit }) => {
  const [cats, setCats]       = useState<Category[]>([]);
  const [error, setError]     = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  const [date, setDate]               = useState(new Date().toISOString().slice(0, 10));
  const [amount, setAmount]           = useState('');
  const [categoryId, setCategoryId]   = useState('');
  const [description, setDescription] = useState('');

  useEffect(() => {
    fetchCategories()
      .then(setCats)
      .catch(() => setError('Falha ao carregar categorias'))
      .finally(() => setLoading(false));
  }, []);

  const handle = (e: React.FormEvent) => {
    e.preventDefault();
    if (!amount || !categoryId) return;
    onSubmit({
      amount: Number(amount),
      categoryId,
      date,
      description: description.trim() || undefined,
    });
  };

  if (loading) return <p>Carregando categorias...</p>;
  if (error) return <p className="text-red-500">{error}</p>;

  return (
    <form onSubmit={handle} className="w-full max-w-md space-y-4">
      <div>
        <label className="block mb-1">Valor</label>
        <input
          type="number"
          value={amount}
          onChange={e => setAmount(e.target.value)}
          className="w-full border px-3 py-2 rounded"
          placeholder="123.45"
        />
      </div>
      <div>
        <label className="block mb-1">Categoria</label>
        <select
          value={categoryId}
          onChange={e => setCategoryId(e.target.value)}
          className="w-full border px-3 py-2 rounded"
        >
          <option value="">Selecione...</option>
          {cats.map(c => (
            <option key={c.id} value={c.id}>
              {c.name}
            </option>
          ))}
        </select>
      </div>
      <div>
        <label className="block mb-1">Data</label>
        <input
          type="date"
          value={date}
          onChange={e => setDate(e.target.value)}
          className="w-full border px-3 py-2 rounded"
        />
      </div>
      <div>
        <label className="block mb-1">Descrição</label>
        <input
          type="text"
          value={description}
          onChange={e => setDescription(e.target.value)}
          className="w-full border px-3 py-2 rounded"
          placeholder="Opcional"
        />
      </div>
      <button
        type="submit"
        className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded"
      >
        Criar transação
      </button>
    </form>
  );
};

export default TransactionForm;
