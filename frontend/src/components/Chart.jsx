import React, { useState, useEffect } from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";
import { transform } from '../helpers/transform.js'
import { ticksArr } from '../helpers/timeTicks.js'
import moment from 'moment'

const Chart = ({rawData}) => {
  const data = transform(rawData)
  console.log(data)

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="custom-tooltip">
          <p className="label">{`${moment(label * 1000).format('ll')}`}</p>
          <p className="label">{`${moment(label * 1000).format('LT')}`}</p>
          <p className="label">{`temperature : ${payload[0].value} °C`}</p>
          <p className="label">{`humidity : ${payload[1].value} %`}</p>
        </div>
      );
    }
  }

  return (
    <LineChart
      width={800}
      height={500}
      data={data}
      margin={{
        top: 10,
        right: 30,
        left: 20,
        bottom: 5
      }}
    >
      <CartesianGrid strokeDasharray="3 3"/>
      <XAxis 
        dataKey="raw"
        type="number"
        domain={['dataMin', 'dataMax']}
        tickFormatter={(tick) => moment(tick * 1000).format('LT')}
        ticks={ticksArr(data)}
      />
      <YAxis yAxisId="left"/>
      <YAxis yAxisId="right" orientation="right" />
      <Tooltip content={<CustomTooltip />}/>
      <Legend />
      <Line 
        yAxisId="left"
        type="monotone"
        dataKey="temperature"
        stroke="#FF7B54"
        activeDot={{r:8}}
      />
      <Line 
        yAxisId="left"
        dot = {true}
        type="monotone"
        dataKey="humidity"
        stroke="#243763"
        activeDot={{r:8}}
      />
    </LineChart>
  )
}

export default Chart
  


