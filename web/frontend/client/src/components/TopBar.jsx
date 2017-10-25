import React from 'react'
import { Link, NavLink } from 'react-router-dom'

class TopBar extends React.Component {
  render(){
    return(
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a className="navbar-brand" href="/">CultureMania</a>
          {this.props.auth ? (
          <div className=" navbar-collapse top-bar-right">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item ">
                <a className="nav-link" href="/">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/logout">Logout</a>
              </li>
            </ul>
          </div>
          ) : (
          <div className="navbar-collapse top-bar-right">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <a className="nav-link" href="/">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/login">Login</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/signup">Sign Up</a>
              </li>
            </ul>
          </div>
          )}
      </nav>
  );
  }
}



export default TopBar