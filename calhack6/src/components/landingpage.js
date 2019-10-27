import React, { Component } from 'react';
import Graph from '../Graph';
// import { Grid, Cell } from 'react-mdl';


class Landing extends Component {
  render() {
	return(
		<div style={{height: '100%', width: '100%', margin: 'auto'}}>
			<Graph/>
		</div>
		)
	}
}

export default Landing;
