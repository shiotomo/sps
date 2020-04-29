import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import {
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  Tooltip,
  XAxis,
  YAxis
} from 'recharts';
import './DateGraph.module.css'

class DateGraph extends Component {
  constructor(props) {
    super(props);
    const serverId = props.match.params.server_id;
    const date = props.match.params.date;
    this.state = {
      serverId: serverId,
      date: date,
      speedtestLogs: [],
      server: {},
      datetimeList: []
    };
  }

  componentDidMount() {
    axios.get(
      '/api/v1/speedtests/batch/' + this.state.serverId
    ).then(result => {
      const speedtestLogs = result.data;
      this.setState({
        speedtestLogs: speedtestLogs
      });
    }).catch(error => {
      console.error(error);
    });

    axios.get(
      '/api/v1/speedtest_servers/' + this.state.serverId
    ).then(result => {
      const server = result.data;
      this.setState({
        server: server
      })
    }).catch(error => {
      console.error(error);
    });
  }

  viewGraph() {
    const graphData = []
    this.state.speedtestLogs.forEach(speedtest => {
      const timestamp = speedtest.timestamp.match(/^\d{4}-\d{2}-\d{2}/).toString();
      if (this.state.date === timestamp) {
        const log = {
          upload: speedtest.upload,
          download: speedtest.download,
          timestamp: speedtest.timestamp
        };
        graphData.push(log);
      }
    });
    return (
        <LineChart width={1300} height={500}  margin={{top: 5, right: 50, left: 50, bottom: 25}} data={graphData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Line dataKey="upload" stroke="#ff5500" />
          <Line dataKey="download" stroke="#0055ff" />
          <Tooltip />
          <Legend />
        </LineChart>
    );
  }

  viewTable() {
    return (
      <div className="serveTable">
        <TableContainer className="server-table" component={Paper}>
          <Table aria-label="sps-info">
            <TableHead>
              <TableRow>
                <TableCell size="small">id</TableCell>
                <TableCell size="small">host</TableCell>
                <TableCell size="small">provider</TableCell>
                <TableCell size="small">country</TableCell>
                <TableCell size="small">city</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow>
                <TableCell size="small">{this.state.server.id}</TableCell>
                <TableCell size="small">{this.state.server.host}</TableCell>
                <TableCell size="small">{this.state.server.provider}</TableCell>
                <TableCell size="small">{this.state.server.country}</TableCell>
                <TableCell size="small">{this.state.server.city}</TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    );
  }

  render() {
    return (
      <div className="Graph">
        <h1>Network graph where date</h1>
        <h3><Link to={'/'}>Dashboard</Link> > <Link to={'/graph/' + this.state.serverId}>Graph[{this.state.serverId}]</Link> > {this.state.date}</h3>
        {this.viewTable()}
        {this.viewGraph()}
      </div>
    );
  }
}

export default DateGraph;