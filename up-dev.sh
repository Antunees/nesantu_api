#! /usr/bin/env bash

docker-compose -f docker-compose.nesantu.yml -f docker-compose.nesantu.dev.yml down
docker build . -t nesantu_api -f api.Dockerfile
docker-compose -f docker-compose.nesantu.yml -f docker-compose.nesantu.dev.yml up