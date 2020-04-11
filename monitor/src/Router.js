import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import Dashboard from './component/Dashbaord/Dashboard.js';
import Graph from './component/Graph/Graph.js';

class Router extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Dashboard} />
          <Route path="/graph/:server_id" component={Graph} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default Router;