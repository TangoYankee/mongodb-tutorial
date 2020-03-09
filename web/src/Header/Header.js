import React from 'react'
import './Header.css'

const HeaderButton = (props) => {
  return(
  <button>{props.destination}</button>
  )
}

const Header = () => {
  return(
    <div className="header">
        <HeaderButton destination='Home'/>
        <HeaderButton destination='Books'/>
        <HeaderButton destination='Profile'/>
    </div>
  )
}

export default Header
