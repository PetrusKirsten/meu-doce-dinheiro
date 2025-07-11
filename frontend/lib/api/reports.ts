// frontend/lib/api/reports.ts
import { fetcher } from "./client";
import type { MonthlyBalance } from "./types";

/** GET /reports/monthly-balance/{year} */
export function getMonthlyBalance(year: number): Promise<MonthlyBalance[]> {
  return fetcher(`/reports/monthly-balance/${year}`);
}
