#!/bin/bash
exec 2>&1
echo "Testing bash execution"
pwd
ls -la /home/diogo/dev/library-docs/zeroclaw/ | head -20
