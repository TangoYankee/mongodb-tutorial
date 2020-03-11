import React from 'react'
import './Header.css'
import {Link} from 'react-router-dom'

const HeaderButton = (props) => {
  return(
  <button>
    {props.destination}
    <Link to="/"></Link>
    </button>
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
