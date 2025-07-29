// frontend/components/DashboardSummaryCard.tsx

import React from "react"

interface Props {
    title : string;
    value : number;
}

export default function DashSummaryCard({ title, value }: Props) {

    const formatted = new Intl.NumberFormat('pt-BR', {
        style   : 'currency',
        currency: 'BRL',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    }).format(value);

  return (
    <div className="flex-1 bg-white shadow-lg rounded-2xl p-6 flex flex-col justify-between">

      <h3 className="text-lg font-medium text-gray-700 mb-2">{title}</h3>
      <p className="text-2xl font-semibold text-gray-900">{formatted}</p>

    </div>
  );
}