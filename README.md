# Raspberry Pi Temperature and Humidity

This app can be used to measure temperature and humidity with a DHT11 or DHT22 sensor connected to your raspberry pi. 

![Chart](docs/chart.png)

### Usage
Install the wheel from the releases section using pip and connect a DHT11/DHT22 sensor connected to your raspberrry pi on port GPIO 4. You can then run the app with `python -m pigrometer`. To change which DHT sensor you're using or which pin you want to connect it to, run with `--dht-version` or `--dht-pin` set. Type `--help` for more options.

To change the amount of data shown on the chart add params to the url `?granularity=900&history=3` where granularity is the number of seconds between points on the graph and history is the number of days to display.

### Upcoming features
- More readable timestamps at the bottom of the chart
- Better logging
- More features in the web ui, ability to easily set time range and granularity
- Ability to download data .csv with data from the web ui

#### Feel free to create an issue if you run into any problems, or if there's any features you think would be a nice addition. Contributions are welcome as well.
