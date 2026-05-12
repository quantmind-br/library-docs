#!/bin/bash
find /home/diogo/dev -name "*vi-providers*" -o -name "*troubleshooting*" -o -name "*contributing*" 2>/dev/null | grep -E "\.(md|markdown)$"
