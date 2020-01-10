#!/bin/bash

del() {
	find $1 -type f -regex ".*\.\(pyc\|log\)" -exec rm -rf {} \;
	find $1 -type d -name "__pycache__"  -exec rmdir {} \; 2> /dev/null
}

del rest
rm -rf *.log*
