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
Reading a datapoint:
