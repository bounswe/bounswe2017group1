import React from 'react'
import { Link, NavLink } from 'react-router-dom'
import Auth from '../../modules/Auth.js'

class TopBar extends React.Component {
  render(){
    return(
      <nav className="navbar navbar-expand-lg navbar-dark bar-blue fixed-top">
        <a className="navbar-brand" href="/" style={{paddingTop: 0}}>
          <img style={{width: '48px', height: '48px'}} src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Unesco_Cultural_Heritage_logo.svg/2000px-Unesco_Cultural_Heritage_logo.svg.png"/>
        </a>
          {this.props.auth ? (
          <div className=" navbar-collapse top-bar-right">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item ">
                <a className="nav-link">{Auth.getUsername()}</a>
              </li>
              <li className="nav-item ">
                <a className="nav-link" href="/itemAdd">New Item</a>
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