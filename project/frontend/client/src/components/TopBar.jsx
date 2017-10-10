import React from 'react'
import { Link, NavLink } from 'react-router-dom'

class TopBar extends React.Component {
  render(){
    return(
      <div className="top-bar">
        <div className="top-bar-left">
          <NavLink to="/">
            <img
              style={{ width: '64px', height: '64px'}}  
              src="http://www.skchto.com/images/icons/cultural_heritage.png"/>
          </NavLink>
        </div>

        {this.props.auth ? (<div className="top-bar-right">
            <Link to="/logout">Logout</Link>
        </div>) : (<div className="top-bar-right">
            <Link to="/login">Log in</Link>
            <Link to="/signup">Sign up</Link>
        </div>)}
      </div>
  );
  }
}



export default TopBar