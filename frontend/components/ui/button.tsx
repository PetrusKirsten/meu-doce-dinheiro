// frontend/components/ui/button.tsx

import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({ children, ...props }) => (
  <button
    className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition"
    {...props}
    >
    {children}
  </button>
);
