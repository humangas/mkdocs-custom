#!/bin/bash

mkdocs build --clean
open -a "Google Chrome" "http://0.0.0.0:8000"
mkdocs serve
