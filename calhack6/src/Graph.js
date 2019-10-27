import React, {Component} from "react";

import {
		GraphView, // required
	} from 'react-digraph';

	const GraphConfig =  {
		NodeTypes: {
			empty: { // required to show empty nodes
				typeText: "None",
				shapeId: "#empty", // relates to the type property of a node
				shape: (
					<symbol viewBox="0 0 100 100" id="empty" key="0">
						<circle cx="50" cy="50" r="45"></circle>
					</symbol>
				)
			},
			custom: { // required to show empty nodes
				typeText: "Custom",
				shapeId: "#custom", // relates to the type property of a node
				shape: (
					<symbol viewBox="0 0 50 25" id="custom" key="0">
						<ellipse cx="50" cy="25" rx="50" ry="25"></ellipse>
					</symbol>
				)
			}
		},
		NodeSubtypes: {},
		EdgeTypes: {
			emptyEdge: {  // required to show empty edges
				shapeId: "#emptyEdge",
				shape: (
					<symbol viewBox="0 0 50 50" id="emptyEdge" key="0">
						<circle cx="25" cy="25" r="8" fill="currentColor"> </circle>
					</symbol>
				)
			}
		}
	}

	const NODE_KEY = "id"       // Allows D3 to correctly update DOM
	const sample = {"nodes": [
		{
			"id": 1,
			"title": "Node A",
			"x": 300.3976135253906,
			"y": 300.9783248901367,
			"type": "empty"
		},
		{
			"id": 2,
			"title": "Node B",
			"x": 600.9393920898438,
			"y": 300.6060791015625,
			"type": "empty"
		},
		{
			"id": 3,
			"title": "Node C",
			"x": 600.3976135253906,
			"y": 100.9783248901367,
			"type": "empty"
		},
		{
			"id": 4,
			"title": "Node D",
			"x": 900.9393920898438,
			"y": 300.6060791015625,
			"type": "empty"
		},
	],
	"edges": [
		{
			"source": 1,
			"target": 2,
			"type": "emptyEdge"
		},
		{
			"source": 1,
			"target": 3,
			"type": "emptyEdge"
		},
		{
			"source": 3,
			"target": 4,
			"type": "emptyEdge"
		},
		{
			"source": 2,
			"target": 4,
			"type": "emptyEdge"

		},
	]
}
	class Graph extends Component {

		// fetchGraphInformation = () => {
		//   this.setState((prevState) => {
		//     return {graph: {...prevState.graph,
		//       edges: [{
		//         source: 2, target: 1, type: 'emptyEdge'
		//       }]
		//     }
		//   }});
		// }

		constructor(props) {
			super(props);

			this.state = {
				graph: sample,
				selected: {}
			}
		}

		componentDidMount() {
			setTimeout(this.fetchGraphInformation, 2000);
		}

		/* Define custom graph editing methods here */

		render() {
			const nodes = this.state.graph.nodes;
			const edges = this.state.graph.edges;
			const selected = this.state.selected;

			const NodeTypes = GraphConfig.NodeTypes;
			const NodeSubtypes = GraphConfig.NodeSubtypes;
			const EdgeTypes = GraphConfig.EdgeTypes;

			return (
				// <div id='graph' style={{width: "100%", height: "100%"}}>

					<GraphView  ref='GraphView'
											nodeKey={NODE_KEY}
											nodes={nodes}
											edges={edges}
											selected={selected}
											nodeTypes={NodeTypes}
											nodeSubtypes={NodeSubtypes}
											edgeTypes={EdgeTypes}
											onSelectNode={this.onSelectNode}
											onCreateNode={this.onCreateNode}
											onUpdateNode={this.onUpdateNode}
											onDeleteNode={this.onDeleteNode}
											onSelectEdge={this.onSelectEdge}
											onCreateEdge={this.onCreateEdge}
											onSwapEdge={this.onSwapEdge}
											onDeleteEdge={this.onDeleteEdge}/>
				// </div>
			);
		}

	}

	export default Graph;
