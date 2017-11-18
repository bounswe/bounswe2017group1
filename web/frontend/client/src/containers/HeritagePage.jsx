import React from 'react';
import TopBar from '../components/TopBar.jsx';
import PropTypes from 'prop-types';

class HeritagePage extends React.Component {


	constructor(props, context) {
	    super(props, context);

	    this.state = {
	      
    		title: "Basri Title",
    		description: "desc deneme",
    		creation_date: "2017-10-25T19:01:46Z",
    		event_date: "2017-10-25T19:01:48Z",
    		location: "istanbul",
    		creator: 1
	    };
  }

  componentDidMount(){
    console.log(this.props.match.params.heritageId);
    fetch('http://ec2-18-196-2-56.eu-central-1.compute.amazonaws.com/api/items/'+this.props.match.params.heritageId,{
      method: "GET",
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json"
      },
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        response.json().then(res=>{
          this.setState(res);
          console.log(res);
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
      <TopBar auth={false}/>
      <div className="container-fluid">

  		<div className="row ">

          <div className="col-md-2 text-center">
          	<h2 className="my-4">{this.state.title}</h2>
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
                <p className="card-text">{this.state.description}</p>
              </div>
            </div>

            <div className="card card-outline-secondary my-4">

              <div className="card-header">
                <h3 className="my-4">Comments</h3>
              </div>
              <div className="card-body">
                <p>This was so helpful. Thanks to you I got a chance to visit this awasome place! 10/10 would go again</p>
                <small className="text-muted">Posted by AhmetNecdetSezer	 on 3/10/17</small>
                <hr/>
                <p>Good job my friend.</p>
                <small className="text-muted">Posted by friendlyGuy on 12/9/17</small>
                <hr/>
                <p>Another way to advertise. Dont do it to this friendly awasome perfect website</p>
                <small className="text-muted">Posted by RagingRyan on 3/11/17</small>
                <hr/>
                <a href="#" className="btn btn-success">Leave a Review</a>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>
    
		);
	}
}

export default HeritagePage;
