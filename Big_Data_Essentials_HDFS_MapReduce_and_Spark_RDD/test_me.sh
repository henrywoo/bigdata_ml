#!/bin/bash

cat wikipedia.txt | python mapper.py  | sort | python reducer.py
