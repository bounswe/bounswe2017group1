import React from 'react';
import PropTypes from 'prop-types';


const Vote = ({
    voteStatus,
    onUpVote,
    onDownVote,
    voteCount
}) => {
    const upStyle = voteStatus > 0 ? " orange600":"";
    const downStyle = voteStatus < 0 ? " orange600":"";
    return (
        <div style={{fontSize: 'x-large'}}>
            <button style={buttonStyle} onClick={onUpVote}>
                <i className={"material-icons md-64"+upStyle}>keyboard_arrow_up</i>
            </button>
            <p/>
            {voteCount}
            <p/>
            <button style={buttonStyle} onClick={onDownVote}>
                <i className={"material-icons md-64"+downStyle}>keyboard_arrow_down</i>
            </button>
        </div>
    );
};

const buttonStyle = {
    background: 'transparent',
    borderWidth: 0,
    outline: 'none'
}
export default Vote