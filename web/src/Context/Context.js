import React from 'react'
import './Context.css'

class Context extends React.Component {
  state = {
    display: 'context'
  }
  render() {
    return (
      <div className="context homeitem" >
        {this.state.display === 'mission' ? (
          <Mission />
        ) : (
            'hello context'
          )}
      </div>
    )
  }

}

const Mission = () => {
  return (
    <div>
      <h3>Mission</h3>
      <p>Ut molestie, neque quis varius dapibus, dolor odio commodo magna, eget accumsan nulla eros in nisl. Proin non luctus ex, eget fermentum quam. Donec pretium orci nibh, nec consectetur libero aliquet quis. Aenean tempus lorem ut nisi pharetra pellentesque. Vestibulum non urna vel leo aliquet facilisis. Proin non eleifend turpis, vitae blandit ex. Maecenas laoreet augue quis ante sagittis commodo. Ut consequat quam eu massa tincidunt, a pellentesque turpis venenatis. Pellentesque luctus ultricies tellus et egestas. In diam ex, iaculis eu ante quis, pharetra lobortis dolor. Praesent quis odio vitae lacus porta pharetra. Sed id posuere dui. </p>
      <h3>Resources</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sollicitudin ante tincidunt rhoncus rhoncus. Phasellus dignissim dolor id nisl consequat, ut malesuada nisl hendrerit. Sed molestie, orci eu auctor sodales, quam tortor dictum felis, et aliquet erat tellus in tortor. Sed vel libero suscipit, tincidunt turpis vestibulum, vestibulum tellus. Phasellus ultrices enim id libero bibendum, et molestie arcu consequat. Proin eget risus eu justo pulvinar mollis nec ut risus. Maecenas quis ex ex</p>
    </div>
  )
}

export default Context
