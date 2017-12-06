import React from 'react';
import TopBar from '../components/TopBar.jsx';
import PropTypes from 'prop-types';
import appConstants from '../../modules/appConstants.js'
import Auth from '../../modules/Auth.js'
import Carousel from 'react-bootstrap/lib/Carousel';
import Vote from '../components/Vote.jsx'
import { Image } from 'react-bootstrap';
import CommentForm from '../components/CommentForm.jsx';
import { ListGroup,ListGroupItem,Panel, Form, FormGroup, Col, FieldGroup, FormControl, Button, PageHeader  } from 'react-bootstrap'
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
import Dialog from 'material-ui/Dialog';

var Upvote = require('react-upvote');


var baseUrl = appConstants.baseUrl;
class HeritagePage extends React.Component {


	constructor(props, context) {
	    super(props, context);

	    this.state = {
	      heritage:{
          id: 1,
          title: "Title",
          description: "Description",
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
        mediacontainer : {
          index: 0,
          direction: null
        },
        comments:[],
        commentFormText:'',
        hideCommentDiv:[],
        recommendedHeritages:[],
        dialogOpen: false
      };
      this.onUpVote = this.onUpVote.bind(this);
      this.onDownVote = this.onDownVote.bind(this);
      this.processCommentForm = this.processCommentForm.bind(this);
      this.setComment = this.setComment.bind(this);
      this.toggleComment = this.toggleComment.bind(this);
      this.deleteComment = this.deleteComment.bind(this);
      this.handleDialogOpen = this.handleDialogOpen.bind(this);
      this.handleDialogClose = this.handleDialogClose.bind(this);
      this.onItemDelete = this.onItemDelete.bind(this);
      this.handleMediaSelect = this.handleMediaSelect.bind(this);
    }

  handleDialogOpen(){
    this.setState({dialogOpen: true});
  }

  handleDialogClose() {
    this.setState({dialogOpen: false});
  }
  onItemDelete(){
		fetch(baseUrl+'/api/items/'+this.state.heritage.id,{
      method: "DELETE",
      headers: {
        "Access-Control-Allow-Origin" : "*",
				"Content-Type": "application/json",
				"authorization": "token "+Auth.getToken()
      },
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
				window.location.replace("/");
			}
    });
		
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
    var headerTmp;
    if (Auth.isUserAuthenticated()) {
      headerTmp = {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token " + Auth.getToken()
      };
    }else{
      headerTmp = {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
      };
    }

    fetch(baseUrl+'/api/items/'+this.props.match.params.heritageId,{
      method: "GET",
      headers: headerTmp,
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
      headers: headerTmp,
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        response.json().then(res=>{
          this.setState({comments: res});
          var rows = [];
          for (var i = 0; i < res.length; i++) {
              rows.push(false);
          }
          this.setState({hideCommentDiv: rows});
        });

      } else {
        // failure
        errors.summary = 'please check form';
        this.setState({
          errors
        });
      }
    });
    
    fetch(baseUrl+'/api/recommendation/heritage/'+this.props.match.params.heritageId,{
      method: "GET",
      headers: headerTmp,
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        response.json().then(res=>{
          this.setState({recommendedHeritages: res});
        });

      } else {
        errors.summary = 'please check form';
        this.setState({
          errors
        });
      }
    });
  }

  /**
   * Process the form.
   *
   * @param {object} event - the JavaScript event object
   */
  processCommentForm(event,parent_id) {
    // prevent default action. in this case, action is the form submission event
    event.preventDefault();
    
    const text = this.state.commentFormText;
    const heritage = this.state.heritage.id;
    var data;
    if(parent_id !== null){
      const parent_comment = parent_id;
      data = {text,heritage,parent_comment};
    }else{
      data = {text, heritage};  
    }
    
    fetch(baseUrl+'/api/comments',{
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token " + Auth.getToken()
      },
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        this.setState({
          errors: {}
        });
        window.location.reload();
      } else {
        // failure
        errors.summary = 'please check form';
        this.setState({
          errors
        });
      }
    });
  }

  handleMediaSelect(selectedIndex, e) {
    this.setState({
      mediacontainer: {
        index: selectedIndex,
        direction: e.direction
      }
    });
  }

  setComment(event) {
    event.preventDefault();
    this.setState({commentFormText:event.target.value});

  }
  toggleComment(index) {
    const hideCommentDiv = this.state.hideCommentDiv;
    hideCommentDiv[index] = !hideCommentDiv[index];
    this.setState({hideCommentDiv});
  }

  deleteComment(comment_id){
    fetch(baseUrl+'/api/comments/'+comment_id,{
      method: "DELETE",
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json",
        "authorization": "token " + Auth.getToken()
      },
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        this.setState({
          errors: {}
        });
        window.location.reload();
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
    const actions = [
      <FlatButton
        label="Cancel"
        primary={true}
        onClick={this.handleDialogClose}
      />,
      <FlatButton
        label="Delete"
       	secondary={true}
        onClick={this.onItemDelete}
      />,
    ];
    console.log(this.state.recommendedHeritages.length);
    let voteStatus = 0;
    if(this.state.heritage.is_upvoted) voteStatus = 1;
    else if (this.state.heritage.is_downvoted) voteStatus = -1;
    const voteCount = this.state.heritage.upvote_count - this.state.heritage.downvote_count;
		return (
    <div>
      <TopBar auth={Auth.isUserAuthenticated()}/>
  		  <div className="row fill-parent">
          <div className="col-md-2 text-center">
          	<h2 className="my-4">{this.state.heritage.title}</h2>
      			<button type="button" className="btn btn-success">Add Annotation</button>
            <Vote
              voteStatus={voteStatus}
              voteCount={voteCount}
              onUpVote={this.onUpVote}
              onDownVote={this.onDownVote}/>
          </div>
          <Dialog
            actions={actions}
            modal={false}
            open={this.state.dialogOpen}
            onRequestClose={this.handleDialogClose}
            >
            Remove Your Cultural Heritage?
          </Dialog>
          <div className="col-md-6">
            <div className="card mt-4">
              <Carousel 
                activeIndex={this.state.mediacontainer.index}
                direction={this.state.mediacontainer.direction}
                onSelect={this.handleMediaSelect}
                >
                {this.state.heritage.medias.map((url)=>{
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
                <div style={{overflow: 'auto'}}>
                  <h3>
                    {this.state.heritage.tags.map((tag, index)=>(
                    <div className="d-inline"  style={{ paddingRight: '10px'}}>
                      <span className="label label-info">{tag.name}</span>
                    </div>
                    
                  ))}
                  </h3>
                </div>
                
                <br/>
                <p className="card-text" style={{paddingBottom: '20px'}}>{this.state.heritage.description}</p>
                {Auth.getUsername() === this.state.heritage.creator_username ? (
									<div style={{float: 'right', marginTop: '-32px', display: 'inline'}}>
										<a href={"/item/edit/"+this.state.heritage.id}>
											<i className={"material-icons md-24"}>mode_edit</i>
										</a>
										<button style={buttonStyle} onClick={()=>{this.handleDialogOpen()}} >
											<i className={"material-icons md-24 red800"}>delete</i>
										</button>
									</div>
								):(<br/>)}
              </div>
            </div>

            <div className="card card-outline-secondary my-4">

              <div className="card-header">
                <h3 className="my-4">Comments</h3>
              </div>
              {this.state.comments.map((comment, index)=>{
                console.log(comment);
                  return(
                    <div className="card-body" style={comment.parent_comment !== null? {marginLeft: '40px'}: {}}>
                    {Auth.isUserAuthenticated()? (
                      <div>
                        <button type="button" style={comment.parent_comment !== null? {marginLeft: '10px',display:'none'}: {marginLeft: '10px'}} onClick={()=>{this.toggleComment(index)}} className="btn btn-primary pull-right hover reply">Reply</button>
                        <button type="button" style={(!comment.is_owner)? {display:'none'}: {}} onClick={()=>{this.deleteComment(comment.id)}} className="btn btn-danger pull-right hover">Delete</button>
                      </div>
                      ):(<div></div>)
                    }
                      <p>{comment.text}</p>
                      <small className="text-muted">Posted by {comment.creator_username} on {comment.creation_date.substring(0,10)}</small>
                      <Panel collapsible expanded={this.state.hideCommentDiv[index]}>
                        <CommentForm 
                          onSubmit={(e)=>{this.processCommentForm(e,comment.id)}}
                          onChange={this.setComment}
                          comment={this.state.commentFormText}
                          />
                      </Panel>
                    </div>  
                  );
              })}
              {Auth.isUserAuthenticated()? (
                <Panel header="Add a Comment">
                  <CommentForm
                    onSubmit={(e)=>{this.processCommentForm(e,null)}}
                    onChange={this.setComment}
                    comment={this.state.commentFormText}/>
                </Panel>
                ):(<div></div>)}

            </div>
          </div>
          <div className="col-md-3">
             <ListGroup>
                {this.state.recommendedHeritages.map((recHeritage, index)=>(
                  <ListGroupItem style={{marginBottom:'10px', overflow: 'hidden'}} header={recHeritage.title} href={"/item/"+recHeritage.id}>
                    {recHeritage.tags.slice(0,3).map((tag, index)=>(
                      <div className="d-inline"  style={{ paddingRight: '10px'}}>
                        <span className="label label-info">{tag.name}</span>
                      </div>
                      
                    ))} 
                    <br/>      
                    {(recHeritage.description.length > 100)? 
                        recHeritage.description.substring(0,100)+"...": recHeritage.description
                    }
                  </ListGroupItem>
                ))} 
            </ListGroup>
          </div>
      </div>
    </div>
    
		);
	}
}

const buttonStyle = {
	background: 'transparent',
	borderWidth: 0,
	outline: 'none'
}

export default HeritagePage;
