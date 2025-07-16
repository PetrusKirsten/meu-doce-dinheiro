// frontend/middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl
  const token        = req.cookies.get('token')?.value

  // libera tudo que começar com /onboarding e a página de login
  if (pathname.startsWith('/onboarding') || pathname === '/login') {
    return NextResponse.next()
  }

  // se não tiver token, manda pro login
  if (!token) {
    const loginUrl = req.nextUrl.clone()
    loginUrl.pathname = '/login'
    return NextResponse.redirect(loginUrl)
  }

  // caso contrário, segue normal
  return NextResponse.next()
}

// define quais rotas a gente quer rodar o middleware
export const config = {
  matcher: [
    /*
      roda em todas exceto:
      - api (prefixo)
      - _next (arquivos estáticos)
      - favicon.ico
    */
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
}
