#!/bin/bash

wget "$SAMPLE_URL" -O sample.tar.gz
tar -xzf sample.tar.gz -C resources
rm sample.tar.gz
