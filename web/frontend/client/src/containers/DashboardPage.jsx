import React from 'react';
import Auth from '../../modules/Auth.js';
import Dashboard from '../components/Dashboard.jsx';
import { withRouter } from 'react-router-dom'
import TopBar from '../components/TopBar.jsx'
/**
  * Dashboard page rendering class
  */
class DashboardPage extends React.Component {

  /**
   * Class constructor.
   */
  constructor(props) {
    super(props);

    this.state = {
      secretData: ''
    };
  }

  /**
   * This method will be executed after initial rendering.
   */
  componentDidMount() {
    console.log('hello there');
    const xhr = new XMLHttpRequest();
    xhr.open('get', '/api/dashboard');
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    // set the authorization HTTP header
    xhr.setRequestHeader('Authorization', `bearer ${Auth.getToken()}`);
    xhr.responseType = 'json';
    xhr.addEventListener('load', () => {
      if (xhr.status === 200) {
        this.setState({
          secretData: xhr.response.message
        });
      }
    });
    console.log('hello2');
    xhr.send();
    console.log('hello3');
  }

  /**
   * Render the component.
   */
  render() {
    
    return (
      <div>
        <TopBar auth={true}/>
        <Dashboard secretData={this.state.secretData} />
      </div>)
  }

}
export default DashboardPage;
