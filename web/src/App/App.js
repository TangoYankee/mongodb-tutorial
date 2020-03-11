import React from 'react'
import './App.css'
import Brand from '../Brand/Brand'
import Context from '../Context/Context'
import Header from '../Header/Header'
import Login from '../Login/Login'
import { render } from 'react-dom'
import { BrowserRouter, Route } from 'react-router-dom'


const routes = [
  {
    path: "/",
    exact: true,
    main: () => <Brand />
  }, {
    path: "/login",
    exact: true,
    main: () => <Login />
  }
]

const App = () => {
  return (
    <div class="site">
      <Header />
      <div className="content">
        <Brand />
        <Context />
      </div>
        <Login />
    </div>
  )
}


// render(
//   <Router>
//     <Route exact path="/" component={Brand} />
//   </Router>
// )



export default App
