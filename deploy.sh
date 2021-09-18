#!/bin/sh

rm -rfv dist/*
python3 setup.py sdist
twine upload dist/*

