import React from 'react';
import PropTypes from 'prop-types'
import Auth from '../../modules/Auth.js';
import HeritageAdd from '../components/HeritageAdd.jsx';
import { Redirect } from 'react-router-dom'
import { withRouter } from 'react-router-dom'
import TopBar from '../components/TopBar.jsx'
import appConstants from '../../modules/appConstants.js'

var baseUrl = appConstants.baseUrl;
class HeritageEditPage extends React.Component {

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
      locationOK: true,
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

  componentDidMount() {
    fetch(baseUrl+'/api/items/'+this.props.match.params.heritageId,{
        method: "GET",
        headers: {
          "Access-Control-Allow-Origin" : "*",
          "Content-Type": "application/json",
          "authorization": "token " + Auth.getToken()
        },
        credentials: "same-origin"
      }).then(response=>{
        if(response.ok){
          response.json().then(res=>{
            console.log(res);
            const temp = res.tags;
            const tags = temp.map((x)=>{
                return {
                    id: x.id,
                    label: x.name
                };
            });
            res.tags = tags;
            this.setState({heritage: res,
              video: res.video === null ? '' : res.video.video_url 
            });
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

  onImageChange(e){
    this.setState({pictures: e.target.files});
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
      locationOK: true
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

    if(!this.state.locationOK) {
      alert('Please select location from dropdown menu');
      return;
    }

    // create a string for an HTTP body message
    const title = this.state.heritage.title;
    const description = this.state.heritage.description;
    const location = this.state.heritage.location;
    const tags = this.state.heritage.tags.map((x)=>{return {name: x.label}});
    const creator = 1;
    //const data = `title=${title}&description=${description}&location=${location}&creator=1`;

    const data = { title, description, location, creator,tags, creation_date: new Date(2017, 11, 20, 12, 0), event_date: new Date(2017, 11, 20, 12, 0)};
    console.log(Auth.getToken())
    fetch(baseUrl+'/api/items/'+this.props.match.params.heritageId,{
      method: "PUT",
      body: JSON.stringify(data),
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token "+Auth.getToken()
      },
      credentials: "same-origin"
    }).then(response=>{
        console.log('respok : ', response.ok)
        console.log('video : ',this.state.video)
        if(response.ok) {
          if (this.state.video !== '') {
            const video_url = this.state.video;
            const heritage = this.props.match.params.heritageId;
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
            }).then(resp=> {
              if(resp.ok) {
                this.setState({redirect: true});
              }
            });
          }
          this.setState({redirect: true});
        }
    })
    
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
        
        return (<Redirect to={'/item/'+this.props.match.params.heritageId} push/>)
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
          isEdit={false}
          video={this.state.video}
          onVideoChange={this.onVideoChange}
        />
      </div>
    );
  }

}

HeritageEditPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default HeritageEditPage;
