This app takes the health insection score data from restaurants in Austin and plots a graph of the score a given restaurant has received over time.
## Routes
Populating the database:
```
curl 10.101.16.98:5000/reset
```
##### Creating a datapoint:
```
curl 10.101.16.98:5000/create/<key>/<name>/<address>/<zipcode>/<date>/<score>
```
Replace key with a key name, name with a restaurant name, address with an address, zipcode with a zipcode, date with a date formatted as m/d/y, and score with an inspection score. If there are spaces in any of these entries, represent them in the curl with a %.
##### Reading a datapoint:
```
curl 10.101.16.98:5000/read/<key>
```
Replace key with a key name. The default key names from populating the redis are key1, key2, key3, ... , key25393.
##### Update a datapoint:
```
curl 10.101.16.98:5000/update/<key>/<datapoint>/<new>
```
Replace key with a key name and new with the new value you would like to input. To choose which data point you are editing replace datapoint with restaurant, zipcode, date, score, or Address. Address must be capital all others must be lowercase.
##### Delete a datapoint:
```
curl 10.101.16.98:5000/delete/<key>
```
Replace key with a key name.
##### Empty both databases:
```
curl 10.101.16.98:5000/emptydb
```
The datapoints are stored on a separate database from the jobs and plots.
##### List the restaurant names:
```
curl 10.101.16.98:5000/restaurantlist
```
Returns a list of all the restaurants in the database.
##### Posting a job to plot the health inspection data:
Restaurants must be input in the curl exactly as they appear in the restaurant list. Some examples are below.
```
curl -X POST -H "content-type: application/json" -d '{"restaurant": "Chick-Fil-A"}' 10.101.16.98:5000/jobs
curl -X POST -H "content-type: application/json" -d '{"restaurant": "Black Walnut Cafe"}' 10.101.16.98:5000/jobs
```
##### Accessing the plots:
Go to the following URL:
```
https://isp-proxy.tacc.utexas.edu/nockolds/download/restaurantname
```
Replace restaurant name with the name of the restaurant. If there are spaces in the name, replace them with -.
```
https://isp-proxy.tacc.utexas.edu/nockolds/download/Chick-Fil-A
```
This will download a plot of the recent health inspection data.
