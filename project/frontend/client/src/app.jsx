import React from 'react';
import ReactDom from 'react-dom';
import injectTapEventPlugin from 'react-tap-event-plugin';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import { BrowserRouter as Router} from 'react-router-dom'
import Base from './components/Base.jsx'
import routes from './routes.js'

//import { browserHistory, Router } from 'react-router';
//import Base from './components/Base.jsx'
// remove tap delay, essential for MaterialUI to work properly
import RouteWithSubRoutes from './RouteWithSubRoutes.jsx'

injectTapEventPlugin();

ReactDom.render((
  <MuiThemeProvider muiTheme={getMuiTheme()}>
    <Base/>
  </MuiThemeProvider>), document.getElementById('react-app'));
