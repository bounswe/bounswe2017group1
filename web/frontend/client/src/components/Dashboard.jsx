import React from 'react';
import PropTypes from 'prop-types'
import { Card, CardTitle, CardText } from 'material-ui/Card';

/**
* Dashboard element for authentication control
*/
const Dashboard = ({ secretData }) => (
  <Card className="container">
    <CardTitle
      title="Dashboard"
      subtitle="You should get access to this page only after authentication."
    />

    {secretData && <CardText style={{ fontSize: '16px', color: 'green' }}>{secretData}</CardText>}
  </Card>
);

Dashboard.propTypes = {
  /**
  * container for all the tabs on the main page
  */
  secretData: PropTypes.string.isRequired
};


export default Dashboard;
