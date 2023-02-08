import config from '../config.js';
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import '../App.css';
import Chart from './Chart'
import HistoryTabs from './HistoryTabs.jsx';

function App() {
  const [rawData, setRawData] = useState([]);
  const [firstLoad, setFirstLoad] = useState(true);
  const [history, setHistory] = useState('')

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
        <HistoryTabs history={history}/>
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
