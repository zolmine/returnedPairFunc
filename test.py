
from json import load

from orjson import loads
from collections import ChainMap

# data = { line.split()[0] for line in open("data.txt") }
file = open('data.json', 'r')
data = load(file)
data = ChainMap(*data)

print(data['0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270']['0x6dd04Cf9D7221fEdd6a8008d1577F3aBBb011E1C']['probability'])
