# Raspberry Pi Temperature and Humidity

This app can be used to measure temperature and humidity with a DHT11 or DHT22 sensor connected to your raspberry pi. 

![Chart](https://github.com/BrianKmdy/PiGrometer/raw/main/docs/chart.png)

### Usage
Install on your raspberry pi with the command `pip install pigrometer` and connect a DHT11/DHT22 sensor to your raspberrry pi on port GPIO 4. You can then run the app with `python -m pigrometer`. After starting the app you should be able to connect to the server at `http://<raspberry_pi_ip>:5000` on your local network.

To change which DHT sensor you're using or which pin you want to connect it to, run with `--dht-version` or `--dht-pin` set. --dht-version can be set to either `'DHT11'` or `'DHT22'`. For possible pin names see [this circuit python guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules). For other options type `--help`.


To change the amount of data shown on the chart add params to the url `?granularity=900&history=3` where granularity is the number of seconds between points on the graph and history is the number of days to display.

### Upcoming features
- More readable timestamps at the bottom of the chart
- Better logging
- More features in the web ui, ability to easily set time range and granularity
- Ability to download data .csv with data from the web ui

#### Feel free to create an issue if you run into any problems, or if there's any features you think would be a nice addition. Contributions are welcome as well.
