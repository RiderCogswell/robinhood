import React from 'react'
import { footerList1, footerList2 } from '../utils/constants'

export const List = ({ items } : { items: string[] }) => ( 
  <div className='flex flex-wrap gap-2 mt-3'>
    {items.map((item) => (
      <p key={item} className="text-gray-400 text-sm hover:underline cursor-pointer">
        {item}
      </p>
    ))}
  </div>
)

const Footer = () => {
  return (
    <footer className='w-full flex justify-between border-t border-gray-200 py-2 px-4'>
      <div className=''>
        <p className='text-gray-300 text-sm mt-5'>&copy;2022 Rider&apos;s Robinhood</p>
      </div>
      <div className=''>
        <List items={footerList1} />
        <List items={footerList2} />
      </div>
    </footer>
  )
}

export default Footer