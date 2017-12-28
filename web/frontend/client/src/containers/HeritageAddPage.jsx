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
        tags:[],
      },
      location: '',
      pictures: [],
      video:'',
      locationOK: false,
      redirect: false
    };

    this.processForm = this.processForm.bind(this);
    this.changeUser = this.changeUser.bind(this);
    this.onImageChange = this.onImageChange.bind(this);
    this.onLocationChane = this.onLocationChane.bind(this);
    this.onLocationSelect = this.onLocationSelect.bind(this);
    this.getTags = this.getTags.bind(this);
    this.onTagChange = this.onTagChange.bind(this);
    this.onVideoChange = this.onVideoChange.bind(this);
  }
  onImageChange(e){
    const pictures = this.state.pictures;
    pictures.push(e.target.files[0]);
    this.setState({pictures});
  }
  onLocationChane(location) {
    const heritage = this.state.heritage;
    heritage.location = location;
    this.setState({
      heritage,
      locationOK: false
    });
  }
  onLocationSelect(location) {
    const heritage = this.state.heritage;
    heritage.location = location;
    this.setState({
      heritage,
      locationOK: false
    });
  }
  getTags(input) {
    if (!input) {
        return Promise.resolve({ options: [] });
    }

    return fetch(`https://cors-anywhere.herokuapp.com/https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&limit=5&language=en&uselang=en&search=${input}&type=item`)
    .then((response) => response.json())
    .then((json) => {
        return { options: json.search };
    });
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
    const tags = this.state.heritage.tags.map((x)=>{return {name: x.label}});
    const creator = 1;
    //const data = `title=${title}&description=${description}&location=${location}&creator=1`;

    const data = { title, description, location, creator,tags, creation_date: new Date(2017, 11, 20, 12, 0), event_date: new Date(2017, 11, 20, 12, 0)};
    console.log(Auth.getToken())
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
          Promise.all(this.state.pictures.map((pic)=>{
            var formData = new FormData();
            formData.append('image',pic);
            formData.append('type','image');
            formData.append('heritage',res.id);
            formData.append('creation_date', '2017-11-21T15:37:03.905307Z');
            formData.append('update_date', '2017-11-21T15:37:03.905307Z');
            return fetch(baseUrl+'/api/medias', {
              method: 'POST',
              headers: {
                "Access-Control-Allow-Origin" : "*",
                "authorization": "token "+Auth.getToken()
              },
              credentials: "same-origin",
              body: formData
            }).then(resp=> resp.status);
          })).then(responses=>{
            console.log(responses)
            if(responses.every((x)=>(x === 200 || x === 201))){
              this.setState({
                redirect: true
              })
            }
          })

          if (this.state.video != '') {
            const video_url = this.state.video;
            const heritage = res.id;
            const videoFormData = {video_url, heritage};
            console.log(videoFormData);
            fetch(baseUrl+'/api/videos', {
              method: 'POST',
              headers: {
                "Access-Control-Allow-Origin" : "*",
                "Content-Type": "application/json",
                "authorization": "token "+Auth.getToken()
              },
              credentials: "same-origin",
              body: JSON.stringify(videoFormData),
            }).then(resp=> resp.status);
          };
          /* var formData = new FormData();
          formData.append('image',this.state.pictures[0]);
          formData.append('type','image');
          formData.append('heritage',res.id);
          formData.append('creation_date', '2017-11-21T15:37:03.905307Z');
          formData.append('update_date', '2017-11-21T15:37:03.905307Z');
          fetch(baseUrl+'/api/medias', {
            method: 'POST',
            headers: {
              "Access-Control-Allow-Origin" : "*",
              "authorization": "token "+Auth.getToken()
            },
            credentials: "same-origin",
            body: formData
          }).then(response=>{
            if(response.ok) {
              console.log('hell yeah')
            }
          })
          this.setState({
            redirect: true
          }) */
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

  onVideoChange(event){
    var video = event.target.value;
    this.setState({
      video
    });
  }

  onTagChange(value) {
    const heritage = this.state.heritage;
    heritage.tags = value;
    this.setState({ heritage });
  }

  /**
   * Render the component.
   */
  render() {
    const AutocompleteItem = ({ formattedSuggestion }) => (
      <div className="place-suggestion-item">
        <i className="material-icons md-dark place-icon">place</i>
        <span style={{verticalAlign: 'middle'}}>
          <strong>{formattedSuggestion.mainText}</strong>{' '}
          <small className="text-muted">{formattedSuggestion.secondaryText}</small>
        </span>
      </div>
    );
    const locationInputProps = {
      value: this.state.heritage.location,
      onChange: this.onLocationChane,
      autoFocus: true
    }
    const {redirect} = this.state;

      if(redirect){
        
        return (<Redirect to='/' push/>)
      }
    return (
      <div>
        <TopBar auth={Auth.isUserAuthenticated()}/>
        
        <HeritageAdd
          onSubmit={this.processForm}
          onChange={this.changeUser}
          errors={this.state.errors}
          successMessage={this.state.successMessage}
          heritage={this.state.heritage}
          onImageChange={this.onImageChange}
          locationInputProps={locationInputProps}
          handleLocationSelect={this.onLocationSelect}
          placesAutocompleteItem={AutocompleteItem}
          getTags={this.getTags}
          onTagChange={this.onTagChange}
          isEdit={true}
          onVideoChange={this.onVideoChange}
          video={this.state.video}
        />
      </div>
    );
  }

}

HeritageAddPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default HeritageAddPage;
