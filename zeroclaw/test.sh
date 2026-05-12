#!/bin/bash
echo "Test"
ls *.md 2>/dev/null || echo "No .md files"
