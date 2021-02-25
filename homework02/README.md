# Dr. Moreau's Island

This repository contains a script to generate a list of twenty hybrid animals. Another script to print and breed two parent animals and print their child. It also contains a unit test script to make sure the the number of arms, legs, and tails on the child animal are whole numbers.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

Running on ISP:

python3 generate_animals.py animals.json
#generates a list of 20 random hybrid animals in a file called animals.json

python3 read_animals.py animals.json
#prints two parent animals and runs a breeding fuction that combines the two animals traits to create a new child animal

python3 test_read_animals.py animals.json
#runs a unit test to make sure the the number of arms, legs, and tails on the child animal are whole numbers

Running in a Container:
