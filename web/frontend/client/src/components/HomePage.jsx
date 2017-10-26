import React, { Component } from 'react';
import { Card, CardTitle, CardHeader, CardText } from 'material-ui/Card';
import TopBar from './TopBar.jsx'
import Auth from '../../modules/Auth.js'
import { Tabs, Tab } from 'material-ui/Tabs';
import 'whatwg-fetch'

const HomePage = React.createClass ({
	getInitialState: function() {
    return {
			filterText: '',
			value: 'a',
			items: []
    };
	},
	
	handleChange: function(value){
    this.setState({
      value: value,
    });
	},
	componentDidMount(){
		fetch('http://localhost:8000/api/items/all',{
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
	render() {
		return(
			<div>
				<TopBar auth={Auth.isUserAuthenticated()}/>
				<div style={{width: '50%', margin: 'auto'}}>
					<SearchBar
						filterText={this.state.filterText}
						inStockOnly={this.state.inStockOnly}
						onUserInput={this.handleUserInput}
					/>
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
				style={{ marginTop: '20px'}}
				tabItemContainerStyle={{ backgroundColor: '#757575' }}
				inkBarStyle={{ backgroundColor: '#212121' }}
			>
				<Tab label="Random" value="a">
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
				<Tab label="Best" value="b">
				<div style={{marginTop: '20px'}}>
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
      <form>
        <input
          type="text"
          placeholder="Search..."
          value={this.props.filterText}
          ref="filterTextInput"
					onChange={this.handleChange}
					style={inputStyle}
        />
      </form>
    );
  }
});

const inputStyle = {
    width: '100%',
    padding: '12px 20px',
    margin: '8px 0',
    display: 'inline-block',
    border: '2px solid #ccc',
    borderRadius: '10px',
    boxSizing: 'border-box'
}
const tabStyles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
  },
};


export default HomePage;
