Weather API

Creating Simple Service to display past week weather information based on the location.

In order to get the historic weather data API provided by https://www.worldweatheronline.com/ is used, the service currently returns the weather information as provided by the API mentioned earlier, for last 7 days. It uses the start_date, end_date and time_period (24 Hrs) parameter as the fields to query the weather data.

1. The Service can be called weather API hosted on Google Cloud Platform. Currently service supports:
This API check the users IP address and returns the corresponding location's weather information.
2. <param> : Here the param can be one of the following values:
    a. City or town name (eg., New+York; New+york,ny; London,united+kingdom)
    b. UK or Canada Postal Code or US Zipcode (90201, 98101, 30052)
    c. Latitude and longitude (two comma separated numeric values, q=48.834,2.394)

This service works and is tested on Google App Engine.

The URL for the service will be provided in the email that will be sent over for this assignment.

If you're curious to deploy it yourself, deploy please follow the instructions from https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env.

Must have valid API key from: www.worldweatheronline.com
