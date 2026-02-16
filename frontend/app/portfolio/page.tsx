export default function PortfolioPage() {
  return (
    <div className='space-y-4'>
      <section className='card'>
        <h1 className='text-xl font-semibold'>Portfolio & Allocation Engine</h1>
        <p>Default model: Core-Satellite with max 10% stock cap and cash buffer guardrails.</p>
        <ul className='list-disc pl-5 text-sm text-slate-300'>
          <li>Sector allocation, India vs US split, market-cap diversification.</li>
          <li>Risk metrics: beta proxy, volatility grade, drawdown watch.</li>
          <li>SIP planning and monthly split suggestions.</li>
        </ul>
        <button className='badge mt-3'>Export Portfolio CSV</button>
      </section>
    </div>
  )
}
