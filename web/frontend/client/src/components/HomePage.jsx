import React, { Component } from 'react';
import { Card, CardTitle, CardHeader, CardText } from 'material-ui/Card'
import TopBar from './TopBar.jsx'
import Auth from '../../modules/Auth.js'
import { Tabs, Tab } from 'material-ui/Tabs'
import 'whatwg-fetch'
import appConstants from '../../modules/appConstants.js'
import { Button, Form, FormGroup, InputGroup, ControlLabel, FormControl, Col } from 'react-bootstrap';

var baseUrl = appConstants.baseUrl;
const HomePage = React.createClass ({
	getInitialState: function() {
    return {
			filterText: '',
			extrafilter: {
				location: '',
				creator: ''
			},
			value: 'a',
			items: [],
			hideAdvanced: true
    };
	},

	onAdvancedSearchChange(e){
		const extrafilter = this.state.extrafilter;
		extrafilter[e.target.name] = e.target.value;
		this.setState({ extrafilter });
	},
	
	handleChange: function(value){
    this.setState({
      value: value,
    });
	},
	componentDidMount(){
		fetch(baseUrl+'/api/items',{
      method: "GET",
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json"
      },
      credentials: "same-origin"
    }).then(response=>{
      if(response.ok){
        response.json().then(res=>{
          this.setState({items: res});
          console.log(res);
        });
      }
    });
	},
  handleUserInput: function(filterText, inStockOnly) {
    this.setState({
      filterText: filterText
    });
	},
	onSearch(event){
		event.preventDefault();
		console.log('here');
		const extrafilter = this.state.extrafilter;
		if(extrafilter.location === '') delete extrafilter.location;
		if(extrafilter.creator === '') delete extrafilter.creator;
		console.log(this.state.filterText);
		fetch(baseUrl+'/api/search',{
      method: "POST",
      headers: {
        "Access-Control-Allow-Origin" : "*",
        "Content-Type": "application/json"
      },
			credentials: "same-origin",
			body: JSON.stringify({
				query: this.state.filterText,
				filters: extrafilter
			})
    }).then(response=>{
      if(response.ok){
        response.json().then(res=>{
          this.setState({items: res});
          console.log(res);
        });
      }
    });
	},
	onToggle (event) {
		event.preventDefault();
		this.setState({
			hideAdvanced: !this.state.hideAdvanced,
			extrafilter: {
				location: '',
				creator: ''
			}
		})
	},
	render() {
		return(
			<div>
				<TopBar auth={Auth.isUserAuthenticated()}/>
				<div style={{width: '50%', margin: 'auto'}}>
					<SearchBar
						filterText={this.state.filterText}
						inStockOnly={this.state.inStockOnly}
						onUserInput={this.handleUserInput}
						onSubmit={this.onSearch}
						onToggle={this.onToggle}
					/>
					<div>
						<Form inline style={this.state.hideAdvanced? {display: 'none'}: {}}>
							<Col sm={5} style={{padding: '4px'}}>
								<FormGroup bsSize="small" style={{display: '-webkit-inline-box'}}>
									<ControlLabel>Location</ControlLabel>
									{' '}
									<FormControl
										type="text"
										placeholder="Location..."
										style={{marginLeft: '4px'}}
										name="location"
										value={this.state.extrafilter.location}
										onChange={this.onAdvancedSearchChange}
										/>
								</FormGroup>
							</Col>
							{' '}
							<Col sm={5} style={{padding: '4px'}}>
								<FormGroup bsSize="small" style={{display: '-webkit-inline-box'}}>
									<ControlLabel>Creator</ControlLabel>
									{' '}
									<FormControl
										type="text"
										placeholder="Creator name.."
										style={{marginLeft: '4px'}}
										name="creator"
										onChange={this.onAdvancedSearchChange}
										/>
								</FormGroup>
							</Col>
							{' '}
							<Col sm={2} style={{paddingLeft: '5px', paddingRight: '5px'}}>
								<FormGroup style={{display: '-webkit-inline-box'}}>
									<Button type="submit" bsStyle="primary" bsSize="small" onClick={this.onSearch}>Search</Button>
								</FormGroup>
							</Col>
							
						</Form>
					</div>
					{this.renderTabs()}
				</div>
  		</div>
		);
	},
	renderTabs(){
		return(
			<Tabs
				value={this.state.value}
				onChange={this.handleChange}
				style={{ marginTop: '5px'}}
				tabItemContainerStyle={{ backgroundColor: '#757575' }}
				inkBarStyle={{ backgroundColor: '#212121' }}
			>
				<Tab label="Random" value="a">
					{this.state.items.map((item, index)=>(
						<div style={{marginTop: '20px'}}>
							<Card style={{ backgroundColor: '#E0E0E0' }}>
								<a className="nav-link" href={'/item/'+item.id}>
								<CardHeader
									title={item.creator_username}
									subtitle={item.creation_date.substring(0, 10)}
									avatar={baseUrl+item.creator_image_path}
									/>
								</a>
								<CardTitle title={item.title}/>
								<CardText>{ item.description} </CardText>
								{Auth.getUsername() === item.creator_username ? (
									<div style={{float: 'right', marginTop: '-32px', display: 'inline'}}>
										<button style={buttonStyle}>
											<i className={"material-icons md-24"}>mode_edit</i>
										</button>
										<button style={buttonStyle}>
											<i className={"material-icons md-24"}>delete</i>
										</button>
									</div>
								):(<br/>)}
							</Card>
						</div>
					))}
				</Tab>
				<Tab label="Best" value="b">
				<div style={{marginTop: '20px'}}>
					{this.state.items.map((item, index)=>(
						<div style={{marginTop: '20px'}}>
							<Card style={{ backgroundColor: '#E0E0E0' }}>
								<CardHeader
									title={item.title}
									titleStyle={{fontWeight: 'bold'}}
								/>
								<CardText expandable={true}>{ item.description} </CardText>
							</Card>
						</div>
					))}
				</div>
				</Tab>
				<Tab label="Trended" value="c">
					{this.state.items.map((item, index)=>(
							<div style={{marginTop: '20px'}}>
								<Card style={{ backgroundColor: '#E0E0E0' }}>
									<CardHeader
										title={item.title}
										titleStyle={{fontWeight: 'bold'}}
									/>
									<CardText>{ item.description} </CardText>
								</Card>
							</div>
						))}
				</Tab>
				<Tab label="New" value="d">
					{this.state.items.map((item, index)=>(
							<div style={{marginTop: '20px'}}>
								<Card style={{ backgroundColor: '#E0E0E0' }}>
									<CardHeader
										title={item.title}
										titleStyle={{fontWeight: 'bold'}}
									/>
									<CardText>{ item.description} </CardText>
								</Card>
							</div>
						))}
				</Tab>
			</Tabs>
		);
	}
});


/* const HomePage = () => (	
  <div>
  	<TopBar auth={Auth.isUserAuthenticated()}/>
  	<div>
			<SearchBar/>
		</div>
  </div>
); */

const SearchBar = React.createClass({
  handleChange: function() {
    this.props.onUserInput(
      this.refs.filterTextInput.value
    );
  },
  render: function() {
    return (
      <FormGroup onSubmit={this.props.onSubmit} style={{marginBottom: '5px'}}>
				<InputGroup style={{display: 'flex'}}>
					<input
						type="text"
						placeholder="Search..."
						value={this.props.filterText}
						ref="filterTextInput"
						onChange={this.handleChange}
						style={inputStyle}
					/>
					<button style={buttonStyle} onClick={this.props.onToggle}>
						<img src="http://www.pvhc.net/img6/qelyglamexpdbblhacjf.png" style={{height: '32px', width: '32px', marginLeft: '-48px'}}/>
					</button>
					<input type="submit" style={{display: 'none'}}/>
				</InputGroup>
        
      </FormGroup>
    );
  }
});

const inputStyle = {
		width: 'calc(100% )',
		height: '36px',
    padding: '12px 20px',
    margin: '8px 0',
    display: 'inline-block',
    border: '2px solid #ccc',
    borderRadius: '10px',
		boxSizing: 'border-box',
		outline: 'none'
}
const tabStyles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
  },
};

const buttonStyle = {
	background: 'transparent',
	borderWidth: 0,
	outline: 'none'
}

export default HomePage;
