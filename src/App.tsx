import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({
    symbol: '',
    price: '',
    volume: ''
  })

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => {
        setData({
          symbol: data.symbol,
          price: data.price,
          volume: data.volume
        })
        console.log(data);
      })
  }, [])

  return (
    <div>
      <p>{data.symbol}</p>
      <p>{data.price}</p>
      <p>{data.volume}</p>
      <button>Buy</button>
    </div>
  );
}

export default App;