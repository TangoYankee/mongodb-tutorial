import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'


const Welcome = (props) => {
  return <h2 className="usa-heading heading-margin-alt">Hello, {props.name}</h2>

}

// https://reactjs.org/docs/state-and-lifecycle.html

const Comment = (props) => {
  return <p className="site-text-intro">{props.text}</p>
}

const App = () => {
  return (
    <div className="usa-prose site-prose">
      <h6 className="usa-heading-alt">Spacing</h6>
      <h1>Page heading</h1>
      <Welcome name="Sara"/>
      <Comment text="What a strange world"/>
    </div>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
