import React, { useState, useEffect } from 'react'

const Home = () => {
  const [data, setData] = useState([{
    symbol: '',
    price: '',
    volume: ''
  }])
  console.log(data);
  

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => {
        setData([{
          symbol: data.symbol,
          price: data.price,
          volume: data.volume
        }])
        console.log(data);
      })
  }, [])

  return (
    <div className='flex items-center justify-center overscroll-x-contain'
      style={{
        backgroundImage: `url("https://cdn.dribbble.com/users/172256/screenshots/12099950/media/d6a355b4196e342b23a07655591abf4b.jpg")`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        height: '100vh',
        width: '100vw',
        imageRendering: 'crisp-edges',
        zIndex: -1,
        overflow: 'hidden'
        
      }}
    >
      {/* <video className='z-10 bg-cover no-repeat bg-center h-100vh ' autoPlay loop muted>
        <source src={Robinhood} type='video/mp4' />
      </video> */}
    </div>
  )
}

export default Home