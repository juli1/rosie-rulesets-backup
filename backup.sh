#!/bin/sh

rm -rf output
mkdir -p output

for ruleset in `cat ruleset-names.txt`; do
  python backup_ruleset.py $ruleset > output/$ruleset.json
done
