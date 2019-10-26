import React from 'react';
import logo from './logo.svg';
import './App.css';
import NetworkGraph from './NetworkGraph';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          ENUM
        </p>
        <div>
        <NetworkGraph data={[5,10,1,3]} size={[500,500]} />
        </div>
      </header>
    </div>
  );
}

export default App;
