import React from 'react'
import axios from 'axios'
import './Login.css'

// Test User ID = 5e373f0db04a5d80b7025168


class Auth {
  constructor(email, password) {
    this.baseUrl = 'http://localhost:8080/api/v1'
    this.email = email
    this.password = password
  }

  get _payload() {
    return {
      "email": this.email,
      "password": this.password
    }
  }

  async _auth ()  {
    return axios.get(`${this.baseUrl}/users/${this.email}`, this._payload)
    .then(response => {  
      console.log(response)
      return response
    })
    .catch(error => {
      console.log(error)
      return(error)
    })
  }
}

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

  async handleSubmit (event) {
    event.preventDefault()    
    var auth = new Auth(this.state.email, this.state.password)
    var response = await auth._auth()
    alert(`login by: ${response.data.username}`) 
  }

  render() {
    return (
      <div className="loginForm">
        <form onSubmit={this.handleSubmit} >
          <div className="loginText">
            <label htmlFor='loginEmail'>
              Email:
          <input id='loginEmail'
                name='email'
                // type='email'
                type="text"
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
          </div>
        </form>
      </div>
    )
  }
}

export default LoginForm
