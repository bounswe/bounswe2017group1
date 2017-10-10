import React, { Component } from 'react';
import { Card, CardTitle, CardHeader, CardText } from 'material-ui/Card';
import TopBar from './TopBar.jsx'
import Auth from '../../modules/Auth.js'
import { Tabs, Tab } from 'material-ui/Tabs';

const HomePage = React.createClass ({
	getInitialState: function() {
    return {
			filterText: '',
			value: 'a'
    };
	},
	
	handleChange: function(value){
    this.setState({
      value: value,
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
					<div style={{marginTop: '20px'}}>
						<Card style={{ backgroundColor: '#E0E0E0' }}>
							<CardHeader
								title="Izmir"
							/>
							<CardText>
								Lorem ipsum dolor sit amet, consectetur adipiscing elit.
								Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
								Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
								Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.
							</CardText>
						</Card>
					</div>
				</Tab>
				<Tab label="Best" value="b">
				<div style={{marginTop: '20px'}}>
					<Card style={{ backgroundColor: '#E0E0E0' }}>
						<CardHeader
							title="Istanbul"
						/>
						<CardText>
							Lorem ipsum dolor sit amet, consectetur adipiscing elit.
							Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
							Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
							Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.
						</CardText>
					</Card>
				</div>
				</Tab>
				<Tab label="Trended" value="c">
					<div style={{marginTop: '20px'}}>
						<Card style={{ backgroundColor: '#E0E0E0' }}>
							<CardHeader
								title="Efes"
							/>
							<CardText>
								Lorem ipsum dolor sit amet, consectetur adipiscing elit.
								Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
								Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
								Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.
							</CardText>
						</Card>
					</div>
				</Tab>
				<Tab label="New" value="d">
					<div>
						<h2 style={tabStyles.headline}>Controllable Tab B</h2>
						<p>
							This is another example of a controllable tab. Remember, if you
							use controllable Tabs, you need to give all of your tabs values or else
							you wont be able to select them.
						</p>
					</div>
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
