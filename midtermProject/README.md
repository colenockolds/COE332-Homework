# Dr. Moreau's Island

This repository contains a flask app which connects to a redis server to interact with data about animals on Dr. Moreau's island. There are various routes in the flask app which perform the following functions: query a range of dates and return the animals that were created with the specified range, select and return an animal using a UUID, edit an animal by passing the UUID along with a new characteristics, delete a group of animals created is a certain range of dates, return the average legs of the animals on the island, and return the total number of animals on the island. I addition to these routes, I have included a few more in order to test whether things are working properly.

## Installation

Github:
git pull git://github.com/colenockolds/COE332-Homework.git/midtermProject
#downloads the midtermProject repository from Github 

## Usage

Starting the App:

From the web folder, run the following commands:

docker-compose build

docker-compose up -d

Flask Routes:

curl localhost:5023/reset
#this route needs to be run first in order to put the data from the animal.json file into the redis database

curl localhost:5023/animals
#returns a list of all animals currently on the redis database

curl localhost:5023/animals/count
#returns the total number of animals on the island

curl localhost:5023/animals/average_legs
#returns a float which is the average number of legs of the animals on the island

curl "localhost:5023/animals/dates?d1=startdate&d2=enddate"
#returns a list of the animals which were created within the specified rage of dates
#it is important to note the quotations surrounding the url and that dates must be input in the format YYYY-M-D

curl "localhost:5023/animals/dates/remove?d1=startdate&d2=enddate"
#removes from the database all animals created within the specified range of dates
#it is important to note the quotations surrounding the url and that dates must be input in the format YYYY-M-D

curl localhost:5023/animals/select/<UUID>
#selects and returns an animal of an input UUID, replace UUID in the url with an animal's UUID

curl localhost:5023/animals/edit/<UUID>/<bodypart>/<new>
#selects an animal using its UUID, then adds the input trait 'new' to the animal under the category 'bodypart'
#in the url, replace UUID with an animal's UUID, bodypart with the bodypart you would like to edit, and new with the new data

curl localhost:5023/print
#prints the keys of all animals currently in the database

##Final Note
I tried to have my midtermProject folder as neat as possible, but there was a file in the redis-docker folder that ISP told me I did not have permission to delete; that is the only reason it is still in the folder.
