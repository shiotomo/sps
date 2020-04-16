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

  fotter() {
    return (
      <div className="fotter">
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
        {this.fotter()}
      </div>
    );
  }
}

export default App;
