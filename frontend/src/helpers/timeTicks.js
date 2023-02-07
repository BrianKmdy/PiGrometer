const ticksArr =  (dataSet) => {
    let result = [];
    let tick = dataSet[0].raw;
    while (tick < dataSet[dataSet.length - 1].raw) {
      tick += 3600;
      result.push(tick);
    }
    return result;
  }

export {ticksArr}