import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import {
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  Tooltip,
  XAxis,
  YAxis
} from "recharts";

class Graph extends Component {
  constructor(props) {
    super(props);
    const serverId = props.match.params.server_id;
    console.log(serverId);
    this.state = {
      serverId: serverId,
      speedtestLogs: [],
      server: {}
    };
  }

  componentDidMount() {
    axios.get(
      'http://localhost:5000/api/v1/speedtests/batch/' + this.state.serverId
    ).then(result => {
      const speedtestLogs = result.data;
      console.log(speedtestLogs);
      this.setState({
        speedtestLogs: speedtestLogs
      })
    }).catch(error => {
      console.error(error);
    });
  }

  viewGraph() {
    const graphData = []
    this.state.speedtestLogs.forEach(speedtest => {
      const log = {
        upload: speedtest.upload,
        download: speedtest.download,
        timestamp: speedtest.timestamp
      };
      graphData.push(log);
    });
    return (
        <LineChart width={1600} height={500}  margin={{top: 5, right: 50, left: 50, bottom: 25}} data={graphData}>
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

  render() {
    return (
      <div className="Graph">
        <h1>server id: {this.state.serverId}</h1>
        {this.viewGraph()}
        <h3><Link to={'/'}>Dashboard</Link></h3>
      </div>
    );
  }
}

export default Graph;