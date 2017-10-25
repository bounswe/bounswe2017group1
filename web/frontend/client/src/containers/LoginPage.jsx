import React from 'react';
import PropTypes from 'prop-types'
import Auth from '../../modules/Auth.js';
import LoginForm from '../components/LoginForm.jsx';
import { Redirect } from 'react-router-dom'
import { withRouter } from 'react-router-dom'
import TopBar from '../components/TopBar.jsx'
import 'whatwg-fetch'

class LoginPage extends React.Component {

  /**
   * Class constructor.
   */
  constructor(props, context) {
    super(props, context);

    const storedMessage = localStorage.getItem('successMessage');
    let successMessage = '';

    if (storedMessage) {
      successMessage = storedMessage;
      localStorage.removeItem('successMessage');
    }

    // set the initial component state
    this.state = {
      errors: {},
      successMessage,
      user: {
        email: '',
        password: ''
      },
      redirect: false
    };

    this.processForm = this.processForm.bind(this);
    this.changeUser = this.changeUser.bind(this);
  }

  /**
   * Process the form.
   *
   * @param {object} event - the JavaScript event object
   */
  processForm(event) {
    // prevent default action. in this case, action is the form submission event
    event.preventDefault();

    // create a string for an HTTP body message
    const username = this.state.user.email;
    const password = this.state.user.password;
    const data = { username, password };

    fetch('http://localhost:8000/api/users/signin',{
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json"
      },
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        console.log('sadasd');
        this.setState({
          errors: {}
        });
        // save the token
        let token;
        response.json().then(res=>{
          /* res.heritage */
          Auth.authenticateUser(res.token);
          this.setState({
            redirect: true
          })
        });
      } else {
        // failure
        errors.summary = 'please check form';
        this.setState({
          errors
        });
      }
    });
  }

  /**
   * Change the user object.
   *
   * @param {object} event - the JavaScript event object
   */
  changeUser(event) {
    const field = event.target.name;
    const user = this.state.user;
    user[field] = event.target.value;

    this.setState({
      user
    });
  }

  /**
   * Render the component.
   */
  render() {
    const {redirect} = this.state;

    if(redirect){
      
      return (<Redirect to='/' push/>)
    }

    return (
      <div>
        <TopBar auth={false}/>
        
        <LoginForm
          onSubmit={this.processForm}
          onChange={this.changeUser}
          errors={this.state.errors}
          successMessage={this.state.successMessage}
          user={this.state.user}
        />
      </div>
    );
  }

}

LoginPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default LoginPage;
