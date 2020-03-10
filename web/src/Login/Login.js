import React from 'react'
import './Login.css'

class LoginForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      email: '',
      password: ''
    }
  }

  handleSubmit(event) {
    event.preventDefault()
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Email:
          <input type="email" value={this.state.email} onChange={
            (event, newValue) => this.setState({ email: newValue })
          } />
        </label>
        <label>
          Password:
          <input type="password" value={this.state.password} onChange={
            (event, newValue) => this.setState({password: newValue})
          } />
        </label>
      </form>
    )
  }
}

export default LoginForm
