import React from 'react'
import './Header.css'

const HeaderButton = (props) => {
  return(
  <button>{props.destination}</button>
  )
}

const Header = () => {
  const destinations = ['Home', 'Books', 'Sign In', 'Create Account']
  return(
    <nav className="header">
        {destinations.map(
          (destination) => <HeaderButton destination={destination}/>
        )}
    </nav>
  )
}

export default Header
