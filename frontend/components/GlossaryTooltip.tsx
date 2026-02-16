'use client'

import { useState } from 'react'

export default function GlossaryTooltip({ term, detail }: { term: string; detail: string }) {
  const [open, setOpen] = useState(false)
  return (
    <span className='relative inline-block'>
      <button className='underline decoration-dotted' onMouseEnter={() => setOpen(true)} onMouseLeave={() => setOpen(false)}>
        {term}
      </button>
      {open && <span className='absolute z-20 mt-2 w-72 rounded-lg border border-slate-700 bg-slate-900 p-2 text-xs'>{detail}</span>}
    </span>
  )
}
