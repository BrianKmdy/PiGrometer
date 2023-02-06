const transform = (dataSet) => {
    let result = [];
    for (let data of dataSet) {
        let newData = {};
        let date = new Date(data[0] * 1000)
        let newDate = new Date(date.getTime() - date.getTimezoneOffset() * 60000)
        let time = newDate.toISOString()
        newData.raw = data[0]
        newData.originalTime = time
        newData.year = newDate.getFullYear()
        //newData.time = Number(time.slice(11, 13) + '.' + time.slice(14, 16))
        newData.time = date
        newData.humidity = data[1];
        newData.temperature = data[2];
        result.push(newData);
    }

    return result;
}

export {transform}