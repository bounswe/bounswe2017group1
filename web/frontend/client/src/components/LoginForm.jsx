import React from 'react';
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom';
import { Card, CardText } from 'material-ui/Card';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
/**
* Login form for logining registered users
*/
const LoginForm = ({
  onSubmit,
  onChange,
  errors,
  successMessage,
  user
}) => (
  <Card className="container">
    <form action="/" onSubmit={onSubmit}>
      <h2 className="card-heading">Login</h2>

      {successMessage && <p className="success-message">{successMessage}</p>}
      {errors.summary && <p className="error-message">{errors.summary}</p>}

      <div className="field-line">
        <TextField
          floatingLabelText="Username"
          name="username"
          errorText={errors.username}
          onChange={onChange}
          value={user.username}
        />
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

      <div className="button-line">
        <RaisedButton type="submit" label="Log in" primary />
      </div>

      <CardText><Link to={'/signup'}>Forgot Password?</Link></CardText>
    </form>
  </Card>
);

LoginForm.propTypes = {
  /**
  * Submit function for the login form
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
  * user information to login
  */
  user: PropTypes.object.isRequired
};

export default LoginForm;
