import React, { useState, useEffect } from 'react';
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend
  } from "recharts";
import { transform } from '../helpers/transform.js'

const Chart = ({rawData}) => {
  const data = transform(rawData)
  console.log(data)
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
      <XAxis dataKey="time" />
      <YAxis yAxisId="left"/>
      <YAxis yAxisId="right" orientation="right" />
      <Tooltip />
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
        type="monotone"
        dataKey="humidity"
        stroke="#243763"
        activeDot={{r:8}}
      />
    </LineChart>
  )
}

export default Chart
  


