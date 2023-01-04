import config from '../config.js';
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import '../App.css';
import Chart from './Chart'

function App() {
  const [rawData, setRawData] = useState([]);
  const [firstLoad, setFirstLoad] = useState(true);

  useEffect(()=>{
    axios.get(`http://${config.API}:5000/data`)
    .then(({data})=>{
      setRawData(data)
      setFirstLoad(false)
    })
    .catch((err)=>{
      console.log(err)
    })
  }, [])
  if (!firstLoad) {
    return (
      <div className="App">
        <Chart rawData={rawData}/>
      </div>
    );
  }
  else {
    return (
      <div>Loading</div>
    )
  }
}

export default App;
