// frontend/utils/jwt.ts

export function parseJwt(token: string): { sub: string; [key: string]: any } {
  // separa header.payload.signature
  const [, payloadBase64] = token.split('.')

  // ajustar padding Base64 e trocar URL-safe chars
  const base64 = payloadBase64.replace(/-/g, '+').replace(/_/g, '/')
  
  // decode Base64 ➔ string JSON
  const json = decodeURIComponent(
    atob(base64)
      .split('')
      .map(c => {
        const code = c.charCodeAt(0).toString(16).padStart(2, '0')
        return '%' + code
      })
      .join('')
  )
  return JSON.parse(json)
}
