import React from 'react'
import './App.css'
import Brand from '../Brand/Brand'
import Context from '../Context/Context'
import Header from '../Header/Header'
import Login from '../Login/Login'

const App = () => {
  return (
    <div>
      <Header />
      <div className="home">
        <Brand />
        <Context />
      </div>
      <Login />
    </div>
  )
}

export default App
