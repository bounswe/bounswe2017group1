import React from 'react';
import TopBar from '../components/TopBar.jsx';
import PropTypes from 'prop-types';
import appConstants from '../../modules/appConstants.js'
import Auth from '../../modules/Auth.js'


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
          tags: []  
        },
        comments:[]
	    };
  }

  componentDidMount(){
    console.log(this.props.match.params.heritageId);
    fetch(baseUrl+'/api/items/'+this.props.match.params.heritageId,{
      method: "GET",
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json"
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
        "Content-Type": "application/json"
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
    
		return (
    <div>
      <TopBar auth={Auth.isUserAuthenticated()}/>
      <div className="container-fluid">

  		<div className="row ">

          <div className="col-md-2 text-center">
          	<h2 className="my-4">{this.state.heritage.title}</h2>
      			<button type="button" className="btn btn-success">Add Annotation</button>
            <div className="list-group">
        			<a href="#" className="list-group-item glyphicon glyphicon-chevron-up"></a>
        			<span className="list-group-item">123</span >
        			<a href="#" className="list-group-item glyphicon glyphicon-chevron-down"></a>
            </div>
          </div>

          <div className="col-md-8">
            <div className="card mt-4">
              <img className="card-img-top img-fluid" src="http://placehold.it/900x400" alt=""/>
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
