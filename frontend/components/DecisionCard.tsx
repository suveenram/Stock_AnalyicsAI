export default function DecisionCard() {
  return (
    <div className='card space-y-2'>
      <h3 className='text-lg font-semibold'>Decision Summary</h3>
      <p>Rating: <strong>Watchlist</strong></p>
      <p>Confidence: <strong>55-68%</strong> (medium)</p>
      <p>Horizon: 3-5 years | Risk grade: moderate</p>
      <p>Suggested allocation: 6% of investable amount</p>
      <p className='text-sm text-slate-400'>Explainability: P/E vs industry, debt trend, and technical trend score were used.</p>
    </div>
  )
}
