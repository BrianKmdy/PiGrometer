# Raspberry Pi Temperature and Humidity

This app can be used to measure temperature and humidity with a DHT11 or DHT22 sensor connected to your raspberry pi. 

With the DHT11/DHT22 sensor connected to your raspberrry pi on port GPIO 4, run humidityReader.py which will store data to a local database. Then run humidityServer.py as a separate process which will start a webserver to serve the temperature and humidity data.

![Chart](docs/chart.png)

### Upcoming features
- More readable timestamps at the bottom of the chart
- Smoother deployment, ideally it will be easier to start and stop the server and reader apps
- More command line args for setting which DHT sensor is being used and which GPIO pin to use on the pi
- Better logging
- More features in the web ui, ability to set time range and granularity
- Ability to download data .csv with data from the web ui

#### Feel free to create an issue if you run into any problems, or if there's any features you think would be a nice addition. Contributions are welcome as well.
