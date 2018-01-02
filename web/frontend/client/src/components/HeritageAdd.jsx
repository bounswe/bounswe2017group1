import React from 'react';
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom';
import { Card, CardText } from 'material-ui/Card';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import { Form, FormGroup, Col, FieldGroup, FormControl, Button, PageHeader  } from 'react-bootstrap'
import PlacesAutocomplete from 'react-places-autocomplete';
import Select from 'react-select'
const AsyncComponent = Select.Async;
/**
* Heritage form for creating new heritage items
*/
const HeritageForm = ({
  onSubmit,
  onChange,
  errors,
  successMessage,
  heritage,
  onImageChange,
  locationInputProps,
  handleLocationSelect,
  placesAutocompleteItem,
  getTags,
  onTagChange,
  isEdit,
  onVideoChange,
  video
}) => (
  <Card className="container">
    <PageHeader >New Heritage Item</PageHeader>
    <Form horizontal style={{margin: '50px 0 50px 0'}} action="/" onSubmit={onSubmit}>
      {isEdit? (
        <FormGroup>
          <Col className="custom-label" sm={3}>
            Media
          </Col>
          <Col sm={6}>
            <FormControl
              type="file"
              onChange={onImageChange}
              multiple
            />
          </Col>
        </FormGroup>
      ): (<br/>)}
      <FormGroup>
        <Col className="custom-label" sm={3}>
          Title
        </Col>
        <Col sm={6}>
          <FormControl
            type="text"
            placeholder="Enter Title"
            onChange={onChange}
            value={heritage.title}
            name="title"
          />
        </Col>
      </FormGroup>

      <FormGroup>
        <Col className="custom-label" sm={3}>
          Description
        </Col>
        <Col sm={6}>
          <FormControl
            componentClass="textarea"
            placeholder="Enter Description"
            onChange={onChange}
            value={heritage.description}
            name="description"
          />
        </Col>
      </FormGroup>

      <FormGroup>
        <Col className="custom-label" sm={3}>
          Tags
        </Col>
        <Col sm={6}>
          <div className="selection">
            <AsyncComponent
              multi={true}
              value={heritage.tags}
              onChange={onTagChange}
              valueKey="id"
              labelKey="label"
              loadOptions={getTags}
              backspaceRemoves={true}/>
          </div>
          </Col>
      </FormGroup>

      <FormGroup>
        <Col className="custom-label" sm={3}>
          Location
        </Col>
        <Col sm={6}>
          <PlacesAutocomplete 
            inputProps={locationInputProps}
            onSelect={handleLocationSelect}
            onEnterKeyDown={handleLocationSelect}
            autocompleteItem={placesAutocompleteItem}
            />
        </Col>
      </FormGroup>
      <FormGroup>
        <Col className="custom-label" sm={3}>
          Video
        </Col>
        <Col sm={6}>
          <FormControl
            type="text"
            placeholder="Enter video link here"
            onChange={onVideoChange}
            value={video}
            name="video"
          />
        </Col>
      </FormGroup>
      <Button type="submit" bsStyle="primary">{isEdit? 'Create' : 'Save'}</Button>
    </Form>
  </Card>
);


HeritageForm.propTypes = {
  /**
  * Submit function for the heritage form
  */
  onSubmit: PropTypes.func.isRequired,
  /**
  * onChange function for form elements
  */
  onChange: PropTypes.func.isRequired,
  /**
  * errors from http requests
  */
  errors: PropTypes.object.isRequired,
  /**
  * success message from http requests
  */
  successMessage: PropTypes.string.isRequired,
  /**
  * heritage item to create
  */
  heritage: PropTypes.object.isRequired,
  /**
  * location of the heritage item as coordinates
  */
  locationInputProps: PropTypes.object.isRequired,
  /**
  * location handler function
  */
  handleLocationSelect: PropTypes.func.isRequired
};
export default HeritageForm;
