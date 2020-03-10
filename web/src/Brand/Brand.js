import React from 'react'
import './Brand.css'

const Brand = () => {
  return (
    <div className="usa-prose brand homeitem">
      <h1>Phoenix Spark</h1>
      <h2>Travis AFB, CA</h2>
      <img alt='phoenix with spread wings' src={`${process.env.PUBLIC_URL}/spark-logo-crop.png`}/>
      <h2>Lending Library</h2>
    </div>
  )
}

export default Brand
