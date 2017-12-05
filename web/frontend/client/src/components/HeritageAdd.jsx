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
  onTagChange
}) => (
  <Card className="container">
    <PageHeader >New Heritage Item</PageHeader>
    <Form horizontal style={{margin: '50px 0 50px 0'}} action="/" onSubmit={onSubmit}>
      <FormGroup>
        <Col className="custom-label" sm={3}>
          Media
        </Col>
        <Col sm={6}>
          <FormControl
            type="file"
            onChange={onImageChange}
          />
        </Col>
      </FormGroup>
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
      <Button type="submit" bsStyle="primary">Create</Button>
    </Form>
  </Card>
);


HeritageForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  onChange: PropTypes.func.isRequired,
  errors: PropTypes.object.isRequired,
  successMessage: PropTypes.string.isRequired,
  heritage: PropTypes.object.isRequired,
  locationInputProps: PropTypes.object.isRequired,
  handleLocationSelect: PropTypes.func.isRequired
};

export default HeritageForm;
