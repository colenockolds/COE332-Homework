# Dr. Moreau's Island

This repository contains a script to generate a list of twenty hybrid animals. Another script to print and breed two parent animals and print their child. It also contains a unit test script to make sure the the number of arms, legs, and tails on the child animal are whole numbers.

## Installation

Github:
git pull git://github.com/colenockolds/COE332-Homework.git/homework02
#downloads the homework02 repository, which contains the scripts generate_animals.py, read_animals.py, test_read_animals.py, the Dockerfile, and this README

Dockerhub:
docker pull colenockolds/homework02:1.0
#pulls the dockerfile from dockerhub

## Usage

Running on ISP:

python3 generate_animals.py
#generates a list of 20 random hybrid animals in a file called animals.json

python3 read_animals.py
#prints two parent animals and runs a breeding fuction that combines the two animals traits to create a new child animal

python3 test_read_animals.py
#runs a unit test to make sure the the number of arms, legs, and tails on the child animal are whole numbers

Running in a Container:

docker run --rm -it colenockolds/homework02:1.0 /bin/bash
#enters a container for the dockerfile

cd /home
#enters home directory

generate_animals.py filename.json
#generates a list of 20 random hybrid animals in a file called filename.json, (filename can be replace with anything followed by .json)

read_animals.py filename.json
#prints two parent animals and runs a breeding fuction that combines the two animals traits to create a new child animal
