#!/usr/bin/sh

report="REPORT.md"
report1="part1/REPORT.md"
report2="part2/REPORT.md"
report3="part3/REPORT.md"

if [ -f "$report" ]; then
    rm -rf "$report"
fi

if [[ -f "$report1" && -f "$report2" && -f "$report3" ]]; then
    echo "[SUCCESS] The compiled result is generated."
else
    echo "[FAIL] Some of the input files are missing."
fi
