import React from 'react'
import PropTypes from 'prop-types'
import { Redirect } from 'react-router-dom'
import Auth from '../../modules/Auth.js'
/**
  * Logout page rendering class
  */
class LogoutPage extends React.Component {

  render() {
    Auth.deauthenticateUser()
    return <Redirect to='/'/>
  }

}

LogoutPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default LogoutPage
