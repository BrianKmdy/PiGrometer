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
    <div>
      This is Chart
      {rawData[1][2]}
    </div>
  )
}

export default Chart
  


