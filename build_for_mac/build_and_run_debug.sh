#!/bin/sh


cd build_for_mac
rm -r -f build dist

pyinstaller -F -d -w build.spec

./dist/Gazer.app/Contents/MacOS/main
