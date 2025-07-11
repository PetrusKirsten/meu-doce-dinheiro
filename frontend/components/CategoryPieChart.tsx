// frontend/components/CategoryPieChart.tsx
import React from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import type { Transaction, Category } from "../lib/api";

interface Props {
  transactions : Transaction[];
  categories   : Category[];
}

// paleta simples; o Recharts vai repetir se faltar
const COLORS = ["#8884D8", "#82CA9d", "#FFC658", "#D0ED57", "#A4DE6C"];

export default function CategoryPieChart({ transactions, categories }: Props) {
  
  // 1) Filtra só despesas (supondo type “despesa” no seu schema)
  const expenses = transactions;  

  // 2) Agrupa soma absoluta por categoria
  const data = categories.map((cat) => {
    const total = expenses
      .filter(tx => tx.category_id === cat.id)
      .reduce((sum, tx) => sum + Math.abs(tx.amount), 0);
    return { name: cat.name, value: total };
  }).filter(d => d.value > 0);

  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <PieChart>
          <Pie
            data        = {data}
            dataKey     = "value"
            nameKey     = "name"
            outerRadius = {100}
            label
          >
            {data.map((_, i) => (
              <Cell key={i} fill={COLORS[i % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip formatter={(value: number) => `R$ ${value.toFixed(2)}`} />
          <Legend verticalAlign="bottom" height={36}/>
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
