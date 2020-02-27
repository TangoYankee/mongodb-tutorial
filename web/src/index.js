import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'


const Welcome = (props) => {
  return <h1>Hello, {props.name}</h1>

}

// const Avatar = (props) => {
//   return (
//     <img className="Avatar"
//     src = {props.user.avatarUrl}
//     alt = {props.user.name}
//     />
//   )
// }

// const Comment = (props) => {
//   return (
//     <div className="Comment">
//       <div className="UserInfo">
//         <Avatar user={props.author} />
//         <div className="UserInfo-name">
//           {props.author.name}
//         </div>
//       </div>
//       <div className="Comment-text">
//         {props.text}
//       </div>
//       <div>
//         {props.date}
//       </div>
//     </div>
//   )
// }

const Comment = (props) => {
  return (
    <div>

<p>{props.text}</p>
    </div>
  )
}

const App = () => {
  return (
    <div>
      <Welcome name="Sara"/>
      <Welcome name="Cahal"/>
      <Welcome name="Edite"/>
      <Comment text="What a strange world"/>
    </div>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
