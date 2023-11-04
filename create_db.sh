#!/bin/bash

docker exec schedoom flask db init
docker exec schedoom flask db migrate
docker exec schedoom flask db upgrade