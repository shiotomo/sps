import React, { Component } from 'react';
import Router from './Router.js';
import MenuBar from './component/MenuBar/MenuBar.js'

import './App.module.css';

class App extends Component {
  header() {
    return (
      <header>
        <MenuBar />
      </header>
    );
  }

  footer() {
    return (
      <div className="footer">
        &copy; sps-monitor shiotomo 2020
      </div>
    );
  }

  content() {
    return (
      <div>
        <Router />
      </div>
    );
  }

  render() {
    return (
      <div className="App">
        {this.header()}
        {this.content()}
        {this.footer()}
      </div>
    );
  }
}

export default App;
