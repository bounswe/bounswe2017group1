import React from 'react';
import TopBar from '../components/TopBar.jsx';
import PropTypes from 'prop-types';
import appConstants from '../../modules/appConstants.js'
import Auth from '../../modules/Auth.js'
import Carousel from 'react-bootstrap/lib/Carousel';
import Vote from '../components/Vote.jsx'
import { Image } from 'react-bootstrap';
var Upvote = require('react-upvote');

var baseUrl = appConstants.baseUrl;
class HeritagePage extends React.Component {


	constructor(props, context) {
	    super(props, context);

	    this.state = {
	      heritage:{
          title: "Basri Title",
          description: "desc deneme",
          creation_date: "2017-10-25T19:01:46Z",
          event_date: "2017-10-25T19:01:48Z",
          location: "istanbul",
          creator: 1,
          tags: [],
          medias: [],
          upvote_count: 0,
          downvote_count: 0,
          is_upvoted: false,
          is_downvoted: false,
          is_owner: false
        },
        comments:[]
      };
      this.onUpVote = this.onUpVote.bind(this);
      this.onDownVote = this.onDownVote.bind(this);
  }

  onUpVote(event) {
    event.preventDefault();
    let body = {}
    let method = ''
    if(this.state.heritage.is_upvoted){
      method = 'DELETE';
    }else{
      method = 'POST';
    }
    fetch(baseUrl+'/api/votes/',{
      method,
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token " + Auth.getToken()
      },
      credentials: "same-origin",
      body: JSON.stringify({
        value: true,
        heritage: this.props.match.params.heritageId
      })
    }).then(resp=>{
      if(resp.status === 201 || resp.status == 200) {
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
              this.setState({heritage: res});
            });
    
          } else {
            this.setState({
              errors
            });
          }
        });
      }
    });
  }

  onDownVote(event) {
    event.preventDefault();
    let body = {}
    let method = ''
    if(this.state.heritage.is_downvoted){
      method = 'DELETE';
    }else{
      method = 'POST';
    }
    fetch(baseUrl+'/api/votes/',{
      method,
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token " + Auth.getToken()
      },
      credentials: "same-origin",
      body: JSON.stringify({
        value: false,
        heritage: this.props.match.params.heritageId
      })
    }).then(resp=>{
      if(resp.status === 201 || resp.status == 200) {
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
              this.setState({heritage: res});
            });
    
          } else {
            this.setState({
              errors
            });
          }
        });
      }
    });
  }

  componentDidMount(){
    
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
          this.setState({heritage: res});
        });

      } else {
        // failure
        errors.summary = 'please check form';
        this.setState({
          errors
        });
      }
    });
    fetch(baseUrl+'/api/items/'+this.props.match.params.heritageId+'/comments',{
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
          this.setState({comments: res});
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

	render() {
    let voteStatus = 0;
    if(this.state.heritage.is_upvoted) voteStatus = 1;
    else if (this.state.heritage.is_downvoted) voteStatus = -1;
    const voteCount = this.state.heritage.upvote_count - this.state.heritage.downvote_count;
		return (
    <div>
      <TopBar auth={Auth.isUserAuthenticated()}/>
      <div className="container-fluid">

  		<div className="row ">

          <div className="col-md-2 text-center">
          	<h2 className="my-4">{this.state.heritage.title}</h2>
      			<button type="button" className="btn btn-success">Add Annotation</button>
            <Vote
              voteStatus={voteStatus}
              voteCount={voteCount}
              onUpVote={this.onUpVote}
              onDownVote={this.onDownVote}/>
          </div>

          <div className="col-md-8">
            <div className="card mt-4">
              <Carousel>
                {this.state.heritage.medias.map((url)=>{
                  console.log(baseUrl+url.image);
                  return (
                    <Carousel.Item>
                      <Image  style={{margin: 'auto'}} src={baseUrl+url.image} responsive/>
                      {/* <img style={{margin: 'auto'}} alt="900x500" src={baseUrl+url.image} /> */}
                    </Carousel.Item>
                  )
                  })}
              </Carousel>
              <div className="card-body">
              <br/>
                <p className="card-text">{this.state.heritage.description}</p>
                <h3>
                  {this.state.heritage.tags.map((tag, index)=>(
                    <div className="d-inline"  style={{ paddingRight: '10px'}}>
                      <span className="label label-info">{tag.name}</span>
                    </div>
                    
                  ))}        
                </h3>
              </div>
            </div>

            <div className="card card-outline-secondary my-4">

              <div className="card-header">
                <h3 className="my-4">Comments</h3>
              </div>
              {this.state.comments.map((comment, index)=>{
                if (comment.parent_comment == null) { 
                  return(
                    <div className="card-body">
                      <button type="button" className="btn btn-success pull-right">Add Annotation</button>
                      <p>{comment.text}</p>
                      <small className="text-muted">Posted by {comment.creator} on {comment.creation_date.substring(0,10)}</small>

                      <hr/>
                    </div>  
                  );
                }else{
                  return(
                    <div className="card-body" style={{ marginLeft: '40px'}}>
                      <p>{comment.text}</p>
                      <small className="text-muted">Posted by {comment.creator} on {comment.creation_date.substring(0,10)}</small>
                      <hr/>
                    </div>  
                  ); 
                }
              })}
            </div>

          </div>

        </div>

      </div>

    </div>
    
		);
	}
}

export default HeritagePage;
