import logo from './logo.svg';
import React, {useEffect} from 'react';
import axios from 'axios';
import './App.css';

function App() {
  useEffect(()=>{
    axios.get('http://192.168.0.144:5000/data')
    .then(({data})=>{
      console.log(data)
    })
    .catch((err)=>{
      console.log(err)
    })
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div>
        
      </div>
    </div>
  );
}

export default App;
