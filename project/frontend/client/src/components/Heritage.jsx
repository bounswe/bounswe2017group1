import React, { Component } from 'react';
import PropTypes from 'prop-types'


const Heritage = ({ denemeString, onClickItem }) => (
  <div>
    <p>{denemeString}</p>
    <button onClick={onClickItem}>Click Here!</button> 
  </div>

)

Heritage.propTypes = {
  denemeString: PropTypes.string.isRequired,
};

export default Heritage;