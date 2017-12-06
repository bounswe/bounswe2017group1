import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Form, FormGroup, Col, FieldGroup, FormControl, Button, PageHeader  } from 'react-bootstrap'



const CommentForm = ({
  onSubmit,
  onChange,
  comment
}) => (
  <Form inline style={{margin: '50px 0 50px 0'}} action="/" onSubmit={onSubmit}>
        <Col sm={9}>
          <FormControl style={{width: '100%'}}
            type="text"
            onChange={onChange}
          />
        </Col>
        <Col sm={3} >
      <Button type="submit" bsStyle="success" className="pull-right">Add Comment</Button>
      </Col>
    </Form>
);

CommentForm.propTypes ={
	onSubmit: PropTypes.func.isRequired,
	onChange: PropTypes.func.isRequired,
	comment: PropTypes.object.isRequired
};

export default CommentForm;