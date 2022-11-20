import React, { useState, useEffect } from 'react'

const Home = () => {
  const [data, setData] = useState([{
    symbol: '',
    price: '',
    volume: ''
  }])

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
    <div>
      {data.map((stock: any, index: number) => (
        <div key={index}>
          <p>{stock.symbol}</p>
          <p>{stock.price}</p>
          <p>{stock.volume}</p>
          <button>Buy</button>
        </div>
      ))}
    </div>
  )
}

export default Home