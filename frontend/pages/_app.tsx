// frontend/pages/_app.tsx

import { AppProps } from "next/app";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
// import "../styles/globals.css"; // ou seu CSS/Tailwind

// Cria um client só uma vez
const queryClient = new QueryClient();

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  );
}
