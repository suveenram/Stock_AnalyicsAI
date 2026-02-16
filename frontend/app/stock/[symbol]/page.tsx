import DecisionCard from '../../../components/DecisionCard'
import GlossaryTooltip from '../../../components/GlossaryTooltip'
import { apiGet, apiPost } from '../../../lib/api'

export default async function StockPage({ params }: { params: { symbol: string } }) {
  const symbol = decodeURIComponent(params.symbol)
  const [overview, fundamentals, technicals] = await Promise.all([
    apiGet(`/stocks/${symbol}/overview`),
    apiGet(`/stocks/${symbol}/fundamentals`),
    apiGet(`/stocks/${symbol}/technicals`)
  ])

  const ai = await apiPost('/ai/insight', {
    symbol,
    metrics: {
      pe_ttm: overview.key_metrics.pe_ttm,
      industry_pe: 20,
      debt_equity: overview.key_metrics.debt_equity,
      volatility_grade: technicals?.risk_grade || 'medium'
    },
    user_profile: { risk_tolerance: 'medium', max_stock_allocation_pct: 10, investable_amount: 10000 }
  })

  return (
    <div className='space-y-4'>
      <section className='card'>
        <h1 className='text-2xl font-bold'>{overview.company_name} ({overview.symbol})</h1>
        <p>{overview.exchange} · {overview.sector} · {overview.industry}</p>
        <p className='text-xl mt-2'>{overview.quote.price} ({overview.quote.change_pct}%)</p>
      </section>

      <DecisionCard />

      <section className='card'>
        <div className='flex flex-wrap gap-2 text-xs'>
          {['Overview','Fundamentals','Financials','Valuation','Technicals','Peers & Industry','News + Sentiment','AI Insight & Recommendation','Events','Ownership'].map((t) => (
            <span key={t} className='badge'>{t}</span>
          ))}
        </div>
      </section>

      <section className='card'>
        <h2 className='font-semibold'>Fundamentals</h2>
        <p>ROE: {fundamentals.returns.roe}% · Debt/Equity: {fundamentals.health.debt_equity}</p>
        <p>
          <GlossaryTooltip term='P/E (TTM)' detail='Price divided by trailing 12-month EPS; compare with peers and history.' />: {overview.key_metrics.pe_ttm}
        </p>
      </section>

      <section className='card'>
        <h2 className='font-semibold'>Technicals</h2>
        <p>Trend: {technicals.trend} | Support: {technicals.support} | Resistance: {technicals.resistance}</p>
        <ul className='list-disc pl-5 text-sm text-slate-300'>
          {technicals.signals?.map((s: string) => <li key={s}>{s}</li>)}
        </ul>
      </section>

      <section className='card'>
        <h2 className='font-semibold'>AI Insight</h2>
        <p>{ai.summary}</p>
        <p className='text-sm text-slate-400'>Confidence: {ai.confidence_range}</p>
        <p className='text-sm text-slate-400'>Assumptions: {ai.assumptions.join('; ')}</p>
        <div className='mt-3 flex gap-2'>
          <button className='badge'>Export PDF</button>
          <button className='badge'>Export Excel</button>
          <button className='badge'>Explain this chart</button>
        </div>
      </section>
    </div>
  )
}
