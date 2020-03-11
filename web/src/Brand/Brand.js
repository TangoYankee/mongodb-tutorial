import React from 'react'
import './Brand.css'

class Brand extends React.Component {
  render() {
    return (
      <main className="brand homeitem">
        <h1>Phoenix Spark</h1>
        <h2>Travis AFB, CA</h2>
        <img alt='phoenix with spread wings' src={`${process.env.PUBLIC_URL}/spark-logo-crop.png`} />
        <h2>Lending Library</h2>
      </main>
    )
  }
}

export default Brand
