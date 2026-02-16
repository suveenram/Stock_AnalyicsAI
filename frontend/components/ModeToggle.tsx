'use client'

import { useState } from 'react'

export default function ModeToggle() {
  const [mode, setMode] = useState<'beginner'|'pro'>('beginner')
  return (
    <div className='flex items-center gap-2'>
      <span className='text-sm text-slate-400'>Mode</span>
      <button className='badge' onClick={() => setMode(mode === 'beginner' ? 'pro' : 'beginner')}>
        {mode === 'beginner' ? 'Beginner Mode' : 'Pro Mode'}
      </button>
    </div>
  )
}
