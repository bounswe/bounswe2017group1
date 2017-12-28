import React from 'react';
import TopBar from '../components/TopBar.jsx';
import PropTypes from 'prop-types';
import appConstants from '../../modules/appConstants.js'
import Auth from '../../modules/Auth.js'
import Carousel from 'react-bootstrap/lib/Carousel';
import Vote from '../components/Vote.jsx'
import Rector from '../components/Rector.jsx'
import { Image } from 'react-bootstrap';
import CommentForm from '../components/CommentForm.jsx';
import { ListGroup,ListGroupItem,Panel, Form, FormGroup, Col, FieldGroup, FormControl, Button, PageHeader  } from 'react-bootstrap'
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
import Dialog from 'material-ui/Dialog';
import ReactDOM from 'react-dom'
import Modal from 'react-bootstrap/lib/Modal';
import OverlayTrigger from 'react-bootstrap/lib/OverlayTrigger';
import Popover from 'react-bootstrap/lib/Popover';
import index from 'material-ui/Dialog';
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
        is_owner: false,
        video: null
      },
      mediacontainer : {
        index: 0,
        direction: null
      },
      comments:[],
      commentFormText:'',
      hideCommentDiv:[],
      recommendedHeritages:[],
      dialogOpen: false,
      canvas: {
        selected: false,
        x: -1,
        y: -1,
        w: -1,
        h: -1
      },
      isAnnotationActive: false,
      showAnnotationPopup: false,
      rectangle: {},
      annotDescription: '',
      mediaAnnots: [],
      commentAnnots: [],
      descAnnots: [],
      annotationType: 0,
      annotIndex: [],
      currCommAnnot: 0
    };
    this.mc = {
      left: 0
    }
    this.im = {
      left: 0,
      width: 0,
      height: 0
    },
    
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
    this.onCanvasSelected = this.onCanvasSelected.bind(this);
    this.onAnnotationClicked = this.onAnnotationClicked.bind(this);
    this.closeAnnotationPopup = this.closeAnnotationPopup.bind(this);
    this.openAnnotationPopup = this.openAnnotationPopup.bind(this);
    this.submitImageAnnotation = this.submitImageAnnotation.bind(this);
    this.handleAnnotDescriptionChange = this.handleAnnotDescriptionChange.bind(this);
    this.onDescSelected = this.onDescSelected.bind(this);
    this.onCommSelected = this.onCommSelected.bind(this);
  }

  handleAnnotDescriptionChange(e){
    this.setState({
      annotDescription: e.target.value
    })
  }

  onDescSelected() {
    if(!this.state.isAnnotationActive) return;
    const selected = window.getSelection().toString();
    const start = this.state.heritage.description.indexOf(selected);
    const end = start + selected.length;
    if(end == start) return;
    for (var i = 0;i < this.state.descAnnots.length;i ++) {
      const coordinates = this.state.descAnnots[i].coordinates;
      if((start > coordinates[0] && start < coordinates[1]) || (end > coordinates[0] && end < coordinates[1])) {
        alert('You can not annotate a substring more than one!!');
        return;
      }
    }
    this.setState({annotationType: 1, annotIndex: [start, end]});
    this.openAnnotationPopup();
  }

  onCommSelected(id,index) {
    if(!this.state.isAnnotationActive) return;
    console.log(index);
    const selected = window.getSelection().toString();
    const comm = this.state.comments[index].text;
    const ann = this.state.commentAnnots[index]
    const start = comm.indexOf(selected);
    const end = start + selected.length;
    if(end == start) return;
    for (var i = 0;i < ann.length;i ++) {
      const coordinates = ann[i].coordinates;
      if((start > coordinates[0] && start < coordinates[1]) || (end > coordinates[0] && end < coordinates[1])) {
        alert('You can not annotate a substring more than one!!');
        return;
      }
    }
    this.setState({annotationType: 2, annotIndex: [start, end], currCommAnnot: id});
    this.openAnnotationPopup();
  }

  submitImageAnnotation() {
    switch(this.state.annotationType) {
      case 0:
        const rect = this.state.rectangle;
        fetch(baseUrl+'/api/annotation/heritage/'+this.state.heritage.id+'/media/'+this.state.heritage.medias[this.state.mediacontainer.index].id,{
          method: "POST",
          headers: {
            "Access-Control-Allow-Origin" : "*",
            "Content-Type": "application/json",
            "authorization": "token "+Auth.getToken()
          },
          credentials: "same-origin",
          body: JSON.stringify({
            text: this.state.annotDescription,
            coordinates: [rect.x,rect.y, rect.w, rect.h]
          })
        }).then(response=>{
          if(response.ok){
            window.location.replace('/item/'+this.props.match.params.heritageId);
          }
        });
        break;
      case 1:
        fetch(baseUrl+'/api/annotation/heritage/'+this.state.heritage.id,{
          method: "POST",
          headers: {
            "Access-Control-Allow-Origin" : "*",
            "Content-Type": "application/json",
            "authorization": "token "+Auth.getToken()
          },
          credentials: "same-origin",
          body: JSON.stringify({
            text: this.state.annotDescription,
            coordinates: this.state.annotIndex
          })
        }).then(response=>{
          if(response.ok){
            window.location.replace('/item/'+this.props.match.params.heritageId);
          }
        });;
        break;
      case 2:
        fetch(baseUrl+'/api/annotation/heritage/'+this.state.heritage.id+'/comment/'+this.state.currCommAnnot,{
          method: "POST",
          headers: {
            "Access-Control-Allow-Origin" : "*",
            "Content-Type": "application/json",
            "authorization": "token "+Auth.getToken()
          },
          credentials: "same-origin",
          body: JSON.stringify({
            text: this.state.annotDescription,
            coordinates: this.state.annotIndex
          })
        }).then(response=>{
          if(response.ok){
            window.location.replace('/item/'+this.props.match.params.heritageId);
          }
        });;
        break;
      default:
        break;
    }
    
  }

  closeAnnotationPopup() {
    this.setState({ showAnnotationPopup: false });
  }

  openAnnotationPopup() {
    this.setState({ showAnnotationPopup: true });
  }

  handleDialogOpen(){
    this.setState({dialogOpen: true});
  }

  onCanvasSelected(rect){
    this.setState(({
      selected: true
    }, rect));
    console.log('asds',rect);
    this.setState({rectangle: rect})
    this.setState({annotationType: 0})
    this.openAnnotationPopup();
  };

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

  onAnnotationClicked(e) {
    var mc = ReactDOM.findDOMNode(this.mcelement).getBoundingClientRect();
    var im = ReactDOM.findDOMNode(this.imelement).getBoundingClientRect();
    this.mc = {
      left: mc.left
    };
    this.im = {
      left: im.left,
      width: im.width,
      height: im.height
    };
    this.setState({isAnnotationActive: !this.state.isAnnotationActive });
    console.log('commAnnots:',this.state.commentAnnots)
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
          var arr = [];
          res.medias.map((m)=>{
            arr.push([]);
          })
          this.setState({heritage: res, mediaAnnots: arr});
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
          var arr = [];
          res.map((m)=>{
            arr.push([]);
          })
          this.setState({commentAnnots: arr});
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

    fetch(baseUrl+'/api/annotation/heritage/'+this.props.match.params.heritageId,{
      method: "GET",
      headers: headerTmp,
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        response.json().then(res=>{
          console.log('annots', res );
          var mediaAnnots = this.state.mediaAnnots;
          var descAnnots = this.state.descAnnots;
          var commentAnnots = this.state.commentAnnots;
          res.map((ann)=>{
            console.log(ann);
            var target = ann.target;
            if(target.includes('media')) {
              var re = /[0-9]*#/g;
              var start = target.search(re);
              var end = target.indexOf('#');
              var id = target.substring(start,end);
              var coordinates = target.substring(end+6,target.length).split(",").map(Number);
              console.log('asdsa',id, coordinates);
              this.state.heritage.medias.map((med,index)=>{
                if(id == med.id) {
                  mediaAnnots[index].push({desc: ann.body, coordinates: coordinates});
                }
              })
            } else if(target.includes('description')) {
                var start = target.indexOf('#');
                var coordinates = target.substring(start+6,target.length).split(",").map(Number);
                console.log('asdsa',coordinates);
                descAnnots.push({description: ann.body, coordinates: coordinates});
            } else {
              var re = /[0-9]*#/g;
              var start = target.search(re);
              var end = target.indexOf('#');
              var id = target.substring(start,end);
              var coordinates = target.substring(end+6,target.length).split(",").map(Number);
              //console.log('asdsa',id, coordinates);
              this.state.comments.map((com,index)=>{
                if(id == com.id) {
                  commentAnnots[index].push({description: ann.body, coordinates: coordinates});
                }
              })
            } 
          })
          this.setState({mediaAnnots, descAnnots, commentAnnots});
          this.onAnnotationClicked();
          this.onAnnotationClicked();
        });

      } else {
        errors.summary = 'please check form';
        this.setState({
          errors
        });
      }
    });
    window.addEventListener("resize", ()=>{
      this.onAnnotationClicked();
      this.onAnnotationClicked();
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
    console.log(selectedIndex);
    this.setState({
      mediacontainer: {
        index: selectedIndex,
        direction: e.direction
      },
      isAnnotationActive: false
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
          <div className="col-xs-2 col-sm-2 col-lg-2 text-center">
          	<h2 className="my-4">{this.state.heritage.title}</h2>
      			<button type="button" className="btn btn-success" onClick={this.onAnnotationClicked}>Add Annotation</button>
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
          <Modal show={this.state.showAnnotationPopup} onHide={this.close}>
            <Modal.Header>
              <Modal.Title>Add Annotation</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <FormControl
                type="text"
                value={this.state.annotDescription}
                placeholder="Enter annotation description"
                onChange={this.handleAnnotDescriptionChange}
              />
            </Modal.Body>
            <Modal.Footer>
              <Button onClick={this.submitImageAnnotation}>Save</Button>
              <Button onClick={this.closeAnnotationPopup}>Close</Button>
            </Modal.Footer>
          </Modal>
          <div className="col-xs-6 col-sm-6 col-lg-6">
            <div className="card mt-4">
              <div className="relative">
                <Carousel 
                  activeIndex={this.state.mediacontainer.index}
                  direction={this.state.mediacontainer.direction}
                  onSelect={this.handleMediaSelect}
                  
                  ref={(c) => {this.mcelement = c}}
                  >
                  {this.state.heritage.medias.map((url,index)=>{
                    return (
                      <Carousel.Item>
                        <div className="relative">
                          <Image
                            style={{margin: 'auto'}}
                            src={baseUrl+url.image}
                            responsive
                            ref={(c) => {if(this.state.mediacontainer.index === index){this.imelement = c}}}/>
                            {this.state.mediaAnnots[index].map((annot)=>(
                              <OverlayTrigger
                                overlay={(
                                  <Popover title="annotation">
                                    {annot.desc}
                                  </Popover>
                                  )}
                                >
                                <canvas
                                width={annot.coordinates[2]}
                                height={annot.coordinates[3]}
                                style={{
                                  border: '2px solid #F44336',
                                  position:'absolute',
                                  left: Math.floor(this.im.left - this.mc.left) + annot.coordinates[0],
                                  top: annot.coordinates[1],
                                  zIndex: 1
                                }}/>
                              </OverlayTrigger>
                              
                            ))}
                        </div>
                        
                        {/* <img style={{margin: 'auto'}} alt="900x500" src={baseUrl+url.image} /> */}
                      </Carousel.Item>
                    )
                    })}
                    {this.state.heritage.video !== null ? (
                    <Carousel.Item>  
                      <iframe
                        width="920"
                        height="520"
                        src={getEmbedURL(this.state.heritage.video.video_url)}
                        frameborder="0"
                        gesture="media"
                        allow="encrypted-media"
                      >
                      </iframe>
                    </Carousel.Item>
                    ): null }
                </Carousel>
                {this.state.isAnnotationActive ? (
                      <Rector
                        style={{
                          left: Math.floor(this.im.left - this.mc.left) 
                        }}
                        width={this.im.width}
                        height={this.im.height}
                        onSelected={this.onCanvasSelected}
                      />
                    ) : null}
              </div>
              <div className="card-body">
                <br/>
                <div >
                  <h3>
                  <div style={{display: 'inline-flex', flexWrap: 'wrap'}}>
                    {this.state.heritage.tags.map((tag, index)=>(
                    <div className="d-inline"  style={{ padding: '10px'}}>
                      <span className="label label-info">{tag.name}</span>
                    </div>
                    
                  ))}
                  </div>
                  </h3>
                </div>
                
                <br/>
                <p className="card-text"
                  style={{paddingBottom: '20px'}}
                  onMouseUp={this.onDescSelected}>
                  {getAnnotatedText(this.state.descAnnots, this.state.heritage.description)}</p>
              </div>
              <div style={{marginTop: '80px', padding: '5px'}}>
                <div className="col-xs-4 col-sm-4 col-lg-4">
                  <div>
                    <large className="text-muted">Location: {this.state.heritage.location}</large>
                  </div>
                  <div>
                    <large className="text-muted">Posted by {this.state.heritage.creator_username} on {this.state.heritage.creation_date.substring(0,10)}</large>
                  </div>
                </div>
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
                      <p onMouseUp={()=>this.onCommSelected(comment.id, index)}>
                        { this.state.commentAnnots[index] ? getAnnotatedText(this.state.commentAnnots[index], comment.text) : comment.text}
                        {/* comment.text */}
                      </p>
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
              {
                Auth.isUserAuthenticated()? (
                  <Panel header="Add a Comment">
                    <CommentForm
                      onSubmit={(e)=>{this.processCommentForm(e,null)}}
                      onChange={this.setComment}
                      comment={this.state.commentFormText}/>
                  </Panel>
                ):(<div></div>)
              }

            </div>
          </div>
          <div className="col-xs-3 col-sm-3 col-lg-3">
             <ListGroup>
                {this.state.recommendedHeritages.map((recHeritage, index)=>(
                  <ListGroupItem style={{marginBottom:'10px', overflow: 'hidden'}} header={recHeritage.title} href={"/item/"+recHeritage.id}>
                    <div style={{display: 'inline-flex', flexWrap: 'wrap'}}>
                      {recHeritage.tags.slice(0,3).map((tag, index)=>(
                        <div className="d-inline"  style={{ padding: '3%'}}>
                          <span className="label label-info">{tag.name}</span>
                        </div>
                        
                      ))}
                    </div> 
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

function getAnnotatedText(annots,desc) {
  if(annots.length === 0) return desc;
  const temp = desc;
  for (var i = 0;i < annots.length;i ++) {
    var str = temp.substring(annots[i].coordinates[0], annots[i].coordinates[1]);
    desc = desc.replace(str, '<span class="mytooltip">' + str +'<span class="mytooltiptext">'+annots[i].description+'</span></span>')
  }
  return <span dangerouslySetInnerHTML={{__html: desc}}></span>;
}

function getEmbedURL(url){
  url = url.replace("watch?v=","");
  var index = url.indexOf('.com') + 5;
  url = [url.slice(0,index), 'embed/', url.slice(index)].join('');
  return url;
}

const buttonStyle = {
	background: 'transparent',
	borderWidth: 0,
	outline: 'none'
}



/* fetch('http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com:3000/api/annotation/heritage/92',{
      method: "POST",
      headers: {
        "Access-Control-Allow-Origin" : "*",
				"Content-Type": "application/json",
				"authorization": "token 46864da369f0c855adae9858332f17e9a280061e"
      },
      credentials: "same-origin",
      body: JSON.stringify({
        text: "text annotation",
        coordinates: [10,20]
      })
    }); */


export default HeritagePage;
