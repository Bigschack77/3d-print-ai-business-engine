import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: '3D Print AI Business Engine',
  description: 'Business intelligence and product discovery for a 3D printing shop',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
