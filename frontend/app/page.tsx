import Link from 'next/link'

export default function HomePage() {
  return (
    <div className='space-y-4'>
      <section className='card'>
        <h1 className='text-2xl font-bold'>Dual-market stock intelligence (India + US)</h1>
        <p className='text-slate-300'>Search NSE/BSE and NYSE/NASDAQ stocks for fundamentals, technicals, AI insights, and allocation guidance.</p>
        <div className='mt-3 flex flex-wrap gap-2'>
          <Link href='/stock/AAPL' className='badge'>AAPL Demo</Link>
          <Link href='/stock/RELIANCE.NS' className='badge'>RELIANCE.NS Demo</Link>
          <Link href='/compare' className='badge'>Compare</Link>
          <Link href='/portfolio' className='badge'>Portfolio</Link>
        </div>
      </section>
    </div>
  )
}
