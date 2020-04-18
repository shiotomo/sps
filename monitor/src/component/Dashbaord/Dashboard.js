import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import axios from 'axios';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import './Dashboard.module.css';

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      serverList: []
    }
  }

  componentDidMount() {
    axios.get(
      'http://localhost:5000/api/v1/speedtest_servers/'
    ).then(result => {
      const serverList = result.data;
      this.setState({
        serverList: serverList
      })
    }).catch(error => {
      console.error(error);
    });
  }

  render() {
    return (
      <div className="Dashboard">
        <h1>Dashboard</h1>
        {this.state.serverList.map(server => {
          return (
            <Card key={server.id} className="server-card">
              <CardHeader title={server.id} />
              <CardContent>
                <Typography variant="h5" component="h3">
                  id: {server.id}
                </Typography>
                <Typography variant="h5" component="h3">
                  country: {server.country}
                </Typography>
                <Typography variant="h5" component="h3">
                  city: {server.city}
                </Typography>
                <Typography variant="h5" component="h3">
                  host: {server.host}
                </Typography>
              </CardContent>
              <CardActions>
                <Button size="small">
                  <Link to={'/graph/' + server.id}>Learn More</Link>
                </Button>
              </CardActions>
            </Card>
          );
        })}
      </div>
    );
  }
}

export default Dashboard;