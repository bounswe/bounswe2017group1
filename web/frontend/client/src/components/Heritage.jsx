import React, { Component } from 'react';
import PropTypes from 'prop-types'

const Heritage = ({ }) => (
        <TopBar auth={false}/>

)

Heritage.propTypes = {
  denemeString: PropTypes.string.isRequired,
};

export default Heritage;