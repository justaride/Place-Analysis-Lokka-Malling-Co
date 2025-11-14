import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Header from '@/components/layout/Header';
import Footer from '@/components/layout/Footer';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });

export const metadata: Metadata = {
  title: {
    default: 'Eiendomsanalyse - Malling&Co',
    template: '%s | Malling&Co',
  },
  description: 'Placeanalyser og eiendomsinformasjon for Malling&Co sin portefølje på Grünerløkka, Oslo',
  keywords: ['Oslo', 'Grünerløkka', 'eiendom', 'placeanalyse', 'Malling&Co'],
  authors: [{ name: 'Natural State' }, { name: 'Malling&Co' }],
  openGraph: {
    type: 'website',
    locale: 'nb_NO',
    siteName: 'Eiendomsanalyse - Malling&Co',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="nb" className={inter.variable}>
      <body className="flex min-h-screen flex-col bg-lokka-light text-lokka-neutral antialiased">
        <Header />
        <main className="flex-1 pt-20">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
