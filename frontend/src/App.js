import './App.css';
import Layout from './hocs/Layout'
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from './containers/Home'
import About from './containers/About'
import Contact from './containers/Contact'
import Listings from './containers/Listings'
import ListingDetail from './containers/ListingDetail'
import Signin from './containers/Signin'
import SignUp from './containers/SignUp'
import NotFound from './components/NotFound'
import './sass/main.scss'
const App = () => {
  return (
    <Router>
      <Layout>
         <Switch>
           <Route exact path="/" component={Home} />
           <Route exact path="/about" component={About} />
           <Route exact path="/contact" component={Contact} />
           <Route exact path="/listings" component={Listings} />
           <Route exact path="/listings/:id" component={ListingDetail} />
           <Route exact path="/signin" component={Signin} />
           <Route exact path="/signup" component={SignUp} />
           <Route component={NotFound} />
         </Switch>
      </Layout>
    </Router>
     
  );
}

export default App;
