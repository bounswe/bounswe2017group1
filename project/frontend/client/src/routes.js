

import HomePage from './components/HomePage.jsx';
import LoginPage from './containers/LoginPage.jsx';
import SignUpPage from './containers/SignUpPage.jsx';
import DashboardPage from './containers/DashboardPage.jsx';
import Base from './components/Base.jsx';
import HomeDash from './containers/HomeDash.jsx';
import LogoutPage from './containers/LogoutPage.jsx';
const routes = [
    {
        path: '/',
        exact: true,
        component: HomePage
    },
    {
        path: '/dashboard',
        component : DashboardPage
    },

    {
        path: '/login',
        component: LoginPage
    },

    {
        path: '/signup',
        component: SignUpPage
    },
    {
        path: '/logout',
        component: LogoutPage
    },
  ]



export default routes;
