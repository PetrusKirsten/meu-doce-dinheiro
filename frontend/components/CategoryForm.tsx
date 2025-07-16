// frontend/components/CategoryForm.tsx

import React, { useState } from 'react';

interface Props {
  onSubmit: (values: { name: string }) => void;
}

const CategoryForm: React.FC<Props> = ({ onSubmit }) => {
  const [name, setName] = useState('');

  const handle = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;
    onSubmit({ name: name.trim() });
    setName('');
  };

  return (
    <form onSubmit={handle} className="w-full max-w-sm">
      <label className="block mb-2 font-medium">Nome da categoria</label>
      <input
        type="text"
        value={name}
        onChange={e => setName(e.target.value)}
        className="w-full border px-3 py-2 rounded mb-4"
        placeholder="Ex: Alimentação"
      />
      <button
        type="submit"
        className="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded"
      >
        Criar categoria
      </button>
    </form>
  );
};

export default CategoryForm;
