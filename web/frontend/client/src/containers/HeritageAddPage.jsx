import React from 'react';
import PropTypes from 'prop-types'
import Auth from '../../modules/Auth.js';
import HeritageAdd from '../components/HeritageAdd.jsx';
import { Redirect } from 'react-router-dom'
import { withRouter } from 'react-router-dom'
import TopBar from '../components/TopBar.jsx'
import appConstants from '../../modules/appConstants.js'

var baseUrl = appConstants.baseUrl;
class HeritageAddPage extends React.Component {

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
      heritage: {
        title: '',
        description: '',
        location: '',
        tags:[]
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
    const title = this.state.heritage.title;
    const description = this.state.heritage.description;
    const location = this.state.heritage.location;
    const tags = this.state.heritage.tags;
    const creator = 1;
    //const data = `title=${title}&description=${description}&location=${location}&creator=1`;

    const data = { title, description, location, creator,tags, creation_date: new Date(2017, 11, 20, 12, 0), event_date: new Date(2017, 11, 20, 12, 0)};

    fetch(baseUrl+'/api/items',{
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token "+Auth.getToken()
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
        console.log(this.state.heritage);
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
    const heritage = this.state.heritage;
    heritage[field] = event.target.value;
    this.setState({
      heritage
    });
  }

  /**
   * Render the component.
   */
  render() {
    return (
      <div>
        <TopBar auth={false}/>
        
        <HeritageAdd
          onSubmit={this.processForm}
          onChange={this.changeUser}
          errors={this.state.errors}
          successMessage={this.state.successMessage}
          heritage={this.state.heritage}
        />
      </div>
    );
  }

}

HeritageAddPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default HeritageAddPage;
