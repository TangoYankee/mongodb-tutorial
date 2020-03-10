import React from 'react'
import './Login.css'

class LoginForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      email: '',
      password: ''
    }
    this.handleInputChange = this.handleInputChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleInputChange(event) {
    this.setState({ [event.target.name]: event.target.value })
  }

  handleSubmit(event) {
    alert(`attempt to login by: ${this.state.email}`)
    event.preventDefault()
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label htmlFor='loginEmail'>
          Email:
          <input id='loginEmail'
            name='email'
            type="email"
            value={this.state.email}
            onChange={this.handleInputChange} />
        </label>
        <label htmlFor='loginPassword'>
          Password:
          <input id='loginPassword'
          name='password'
            type="password"
            value={this.state.password}
            onChange={this.handleInputChange} />
        </label>
        <button type="submit">
          Submit
        </button>
      </form>
    )
  }
}

export default LoginForm
