import React from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import { Route } from 'react-router-dom'
import HomePage from './HomePage.jsx';
import LoginPage from '../containers/LoginPage.jsx';
import SignUpPage from '../containers/SignUpPage.jsx';
import routes from '../routes.js'
import Auth from '../../modules/Auth.js'
import RouteWithSubRoutes from '../RouteWithSubRoutes.jsx'

/**
* Base object for all frontend elements
*/
const Base = () => (

    <Router>
        <div>
            {routes.map((route, i) => (
                <RouteWithSubRoutes key={i} {...route}/>
            ))}
        </div>
    </Router>

)

export default Base;
