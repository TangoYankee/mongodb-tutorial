import React from 'react'
import Brand from '../Brand/Brand'
import Context from '../Context/Context'
import Login from '../Login/Login'

const routes = [
  {
    path: "/",
    exact: true,
    main: () => <Brand />,
    context: () => <Context />
  }, {
    path: "/users",
    exact: true,
    main: () => <Login />,
    context: () => <Context />
  }
]

export default routes
