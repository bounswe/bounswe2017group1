import React from 'react';
import Heritage from '../components/Heritage.jsx';


class HeritagePage extends React.Component {


	constructor(props, context) {
	    super(props, context);

	    this.state = {
	      
	      deneString: "denemeString123",
	    };

	    this.clickButton = this.clickButton.bind(this);

	}

	clickButton(){
		this.setState({
	      deneString : "asdasd",
	    });
	}

	render() {
		return (
			<div>
				<Heritage
					onClickItem= {this.clickButton}
		          	denemeString={this.state.deneString}
		        />
	        </div>
		)
	}
}

export default HeritagePage;
