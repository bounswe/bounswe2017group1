import React, { PropTypes } from 'react';
import Auth from '../../modules/Auth.js';
import DashboardPage from './DashboardPage.jsx'
import HomePage from '../components/HomePage.jsx'



class HomeDash extends React.Component {

  constructor(props, context){
    super(props,context)
  }
  render() {
    console.log('laaaaaa2');
    if(Auth.isUserAuthenticated()){
      console.log('laaaaaa3');
      return (
        <DashboardPage />
      )
    }
    else{
      console.log('laaaaaa4');
      return (
        <HomePage />
      )
    }

  }

}

HomeDash.contextTypes = {
  router: PropTypes.object.isRequired
};

export default HomeDash;
