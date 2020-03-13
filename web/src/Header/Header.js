import React from 'react'
import './Header.css'
import { NavLink } from 'react-router-dom'

const HeaderButton = (props) => {
  return (
    <NavLink exact to={props.destination.link} className="normal" activeClassName="selected">{props.destination.name}</NavLink>
  )
}

const Header = () => {
  const destinations = [
    { name: 'Home', link: '/' },
    { name: 'Books', link: '/books' },
    { name: 'Login', link: '/login' },
    { name: 'Sign up', link: '/signup' }
  ]
  return (
    <nav className="header">
      {destinations.map(
        (destination) => <HeaderButton key={destination.name} destination={destination} />
      )}
    </nav>
  )
}

export default Header
