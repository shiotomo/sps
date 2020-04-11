import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'

class Menubar extends Component {
  render() {
    return (
      <div className="Menubar">
        <AppBar position="static" color="default">
          <Toolbar>
            <Typography variant="h6">
              sps-monitor
            </Typography>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default Menubar;
