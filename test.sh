#!/bin/bash

pip install -qr test-requirements.txt

nosetests --with-doctest
