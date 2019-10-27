import React, { Component } from 'react';
import Graph from '../Graph';
// import { Grid, Cell } from 'react-mdl';


class Landing extends Component {
  render() {
	return(
		<div style={{width: '100%', height: '100%', margin: 'auto'}}>
			<Graph/>
		</div>
		)
	}
}

export default Landing;
