import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Authentication disabled - public access for Aspelin Ramm Vulkan Portfolio
export function middleware(_request: NextRequest) {
  // Allow all requests without authentication
  return NextResponse.next();
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
};
