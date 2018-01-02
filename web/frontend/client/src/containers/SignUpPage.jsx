import React from 'react';
import PropTypes from 'prop-types'
import SignUpForm from '../components/SignUpForm.jsx';
import { Redirect } from 'react-router-dom'
import { withRouter } from 'react-router-dom'
import TopBar from '../components/TopBar.jsx'
import appConstants from '../../modules/appConstants.js'

var baseUrl = appConstants.baseUrl;
/**
  * Signup page rendering class
  */
class SignUpPage extends React.Component {

  /**
   * Class constructor.
   */
  constructor(props, context) {
    super(props, context);

    // set the initial component state
    this.state = {
      errors: {},
      user: {
        email: '',
        name: '',
        location: '',
        gender: 'Empty',
        password: '',
        passwordagain: ''
      },
      redirect : false
    };

    this.processForm = this.processForm.bind(this);
    this.changeUser = this.changeUser.bind(this);
    this.handleDropDownChange = this.handleDropDownChange.bind(this);
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
    const username = this.state.user.name;
    const email = this.state.user.email;
    const location = this.state.user.location;
    const gender = this.state.user.gender;
    const password = this.state.user.password;
    const passwordagain = this.state.user.passwordagain;
    if (password !== passwordagain) {
      this.setState({
        errors: {
          password: 'Passwords do not match'
        }
      })
      return;
    }
    const data = {username, email, location, gender, password};
    fetch(baseUrl+'/api/users/signup',{
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json"
      }
    }).then(response=>{
      if(response.ok){
        // success
        this.setState({
          errors: {}
        });
        localStorage.setItem('successMessage', 'You have successfully registered');
        this.setState({redirect : true})
      } else {
        if(response.status === 401) {
          const errors = {summary: ''}
          errors.summary = 'This username has already been used';
          this.setState({
            errors
          });
        } else {
          const errors = {summary: ''}
          errors.summary = 'Please check your form';
          this.setState({
            errors
          });
        }
      }
    });
  }
  handleDropDownChange(event, index, value) {
    const user = this.state.user;
    user.gender = value;
    this.setState({user});
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
    const {redirect}  = this.state;
    if(redirect) {
      return <Redirect to='/login'/>
    }
    return (
      <div>
        <TopBar auth={false}/>
        <SignUpForm
          onSubmit={this.processForm}
          onChange={this.changeUser}
          handleDropDownChange={this.handleDropDownChange}
          errors={this.state.errors}
          user={this.state.user}
        />
      </div>
    );
  }

}

SignUpPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default SignUpPage;
