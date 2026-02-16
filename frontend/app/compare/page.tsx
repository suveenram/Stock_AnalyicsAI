import { apiPost } from '../../lib/api'

export default async function ComparePage() {
  const data = await apiPost('/compare', { symbols: ['AAPL', 'RELIANCE.NS'] })
  return (
    <section className='card'>
      <h1 className='text-xl font-semibold'>Compare (up to 4 stocks)</h1>
      <table className='mt-3 w-full text-sm'>
        <thead><tr><th>Symbol</th><th>P/E</th><th>ROE</th><th>D/E</th><th>Trend</th></tr></thead>
        <tbody>
          {data.rows.map((r: any) => (
            <tr key={r.symbol} className='border-t border-slate-800'>
              <td>{r.symbol}</td><td>{r.pe_ttm}</td><td>{r.roe}</td><td>{r.debt_equity}</td><td>{r.trend}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
