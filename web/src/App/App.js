import React from 'react'
import './App.css'
import Brand from '../Brand/Brand'
import Context from '../Context/Context'
import Header from '../Header/Header'

const App = () => {
  return (
    <div className="home">
      <Header />
      <Brand />
      <Context />
    </div>
  )
}

export default App
