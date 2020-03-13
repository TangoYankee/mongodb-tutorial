import React from 'react'
import './App.css'
import routes from '../Routes/Routes'
import Header from '../Header/Header'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <div className="content">
        <Switch>
          {routes.map((route, index) => (
            <Route key={index} exact={route.exact} path={route.path}>
              {<route.main />}
              {<route.context />}
            </Route>
          ))}
        </Switch>
      </div>
    </BrowserRouter>
  )
}

export default App
