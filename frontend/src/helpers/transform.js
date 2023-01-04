const transform = (dataSet) => {
    let result = [];
    for (let data of dataSet) {
        let newData = {};
        newData.time = data[0];
        newData.humidity = data[1];
        newData.temperature = data[2];
        result.push(newData);
    }

    return result;
}

export {transform}