import React from 'react';
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom';
import { Card, CardText } from 'material-ui/Card';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import DropDownMenu from 'material-ui/DropDownMenu';
import MenuItem from 'material-ui/MenuItem';


const SignUpForm = ({
  onSubmit,
  onChange,
  errors,
  user,
  handleDropDownChange
}) => (
  <Card className="container">
    <form action="/" onSubmit={onSubmit}>
      <h2 className="card-heading">Sign Up</h2>

      {errors.summary && <p className="error-message">{errors.summary}</p>}

      <div className="field-line">
        <TextField
          floatingLabelText="Username"
          name="name"
          errorText={errors.name}
          onChange={onChange}
          value={user.name}
        />
      </div>

      <div className="field-line">
        <TextField
          floatingLabelText="Email"
          name="email"
          errorText={errors.email}
          onChange={onChange}
          value={user.email}
        />
      </div>
      <div className="field-line">
        <TextField
          floatingLabelText="Location"
          name="location"
          onChange={onChange}
          value={user.location}
        />
      </div>
      <div className="field-line">
        <DropDownMenu
          value={user.gender}
          onChange={handleDropDownChange}
          style={dropDownStyle.customWidth}
          autoWidth={false}
          >
          <MenuItem value={'Empty'} primaryText=" " />
          <MenuItem value={'Male'} primaryText="Male" />
          <MenuItem value={'Female'} primaryText="Female" />
          <MenuItem value={'Not'} primaryText="Not Specefied" />
        </DropDownMenu>
      </div>
      
      <div className="field-line">
        <TextField
          floatingLabelText="Password"
          type="password"
          name="password"
          onChange={onChange}
          errorText={errors.password}
          value={user.password}
        />
      </div>
      <div className="field-line">
        <TextField
          floatingLabelText="Password again"
          type="password"
          name="passwordagain"
          onChange={onChange}
          errorText={errors.password}
          value={user.passwordagain}
        />
      </div>

      <div className="button-line">
        <RaisedButton type="submit" label="Create New Account" primary />
      </div>

      <CardText>Already have an account? <Link to={'/login'}>Log in</Link></CardText>
    </form>
  </Card>
);

SignUpForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  onChange: PropTypes.func.isRequired,
  errors: PropTypes.object.isRequired,
  user: PropTypes.object.isRequired
};

const dropDownStyle = {
  customWidth: {
    width: 200,
  },
};

export default SignUpForm;
