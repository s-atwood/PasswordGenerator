import React, { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState([{}])
  
  useEffect(() => {
    fetch("http://127.0.0.1:5000/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <>
      {Object.keys(data).map((key, index) => (
      <p key={index}>{`${key}: ${JSON.stringify(data[key])}`}</p>
    ))}
    </>
  )
}

export default App
