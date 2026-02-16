import './globals.css'
import ModeToggle from '../components/ModeToggle'
import DisclaimerBanner from '../components/DisclaimerBanner'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang='en'>
      <body>
        <header className='sticky top-0 z-30 border-b border-slate-800 bg-slate-950/95 p-4 backdrop-blur'>
          <div className='mx-auto flex max-w-6xl items-center justify-between'>
            <a href='/' className='text-lg font-semibold'>Stock Analytics AI</a>
            <ModeToggle />
          </div>
        </header>
        <main className='mx-auto max-w-6xl p-4 space-y-4'>
          <DisclaimerBanner />
          {children}
        </main>
      </body>
    </html>
  )
}
