

import HomePage from './components/HomePage.jsx';
import LoginPage from './containers/LoginPage.jsx';
import SignUpPage from './containers/SignUpPage.jsx';
import DashboardPage from './containers/DashboardPage.jsx';
import Base from './components/Base.jsx';
import HomeDash from './containers/HomeDash.jsx';
import LogoutPage from './containers/LogoutPage.jsx';
import HeritagePage from './containers/HeritagePage.jsx';
import HeritageAddPage from './containers/HeritageAddPage.jsx';


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
    {
        path: '/item/:heritageId',
        component: HeritagePage
    },
    {
        path: '/itemAdd',
        component: HeritageAddPage
    },
  ]



export default routes;
