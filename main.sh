#!/usr/bin/env bash

while :; do
    python multi.py
    ps -ef --forest
    sleep 1
done
