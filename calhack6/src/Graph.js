import React, {Component} from "react";
import data from './results.js';



import {
    GraphView, // required
  } from 'react-digraph';
  
  const GraphConfig =  {
    NodeTypes: {
      empty: { // required to show empty nodes
        typeText: "",
        shapeId: "#empty", // relates to the type property of a node
        shape: (
          <symbol viewBox="0 0 100 100" id="empty" key="0">
            <circle cx="50" cy="50" r="50"></circle>
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
  const sample = data
  class Graph extends Component {
  
    constructor(props) {
      super(props);
  
      this.state = {
        graph: sample,
        selected: {}
      }
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
        <div id='graph' style={{width: "100%", height: "100%"}}>
  
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
                      onDeleteEdge={this.onDeleteEdge}
                      
                      />
        </div>
      );
    }
  
  }

  export default Graph;
