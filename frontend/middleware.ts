// frontend/middleware.ts

import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl
  const token        = req.cookies.get('token')?.value

  // 1) Rotas que NÃO precisam de auth
  const publicPaths = [
    '/login',
    '/signup',]

  const isPublicPath = 
    publicPaths.includes(pathname) ||
    pathname.startsWith('/onboarding') ||
    pathname.startsWith('/_next') ||
    pathname.startsWith('/favicon.ico')

  if (isPublicPath) {
    return NextResponse.next()
  }

  // 2) Se não tiver token, redireciona pro login
  if (!token) {
    const loginUrl = req.nextUrl.clone()
    loginUrl.pathname = '/login'
    return NextResponse.redirect(loginUrl)
  }

  // 3) Se tiver token, deixa passar
  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)',],
}
