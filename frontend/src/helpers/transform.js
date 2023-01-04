const transform = (dataSet) => {
    let result = [];
    for (let data of dataSet) {
        let newData = {};
        let date = new Date(data[0] * 1000)
        let newDate = new Date(date.getTime() - date.getTimezoneOffset() * 60000)
        let time = newDate.toISOString()
        newData.time = time.slice(11, 16)
        newData.humidity = data[1];
        newData.temperature = data[2];
        result.push(newData);
    }

    return result;
}

export {transform}