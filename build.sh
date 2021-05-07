#!/bin/bash
pyinstaller --onefile main.py --noconsole

mkdir sunni
cp -r audio/ sunni
cp -r images/ sunni
cp -r lib/ sunni
cp -r dist/ sunni

mkdir sunni/saves
echo 'No save data' > sunni/saves/save1.txt
echo 'No save data' > sunni/saves/save2.txt
echo 'No save data' > sunni/saves/save3.txt
echo 'No save data' > sunni/saves/save4.txt

cp 'Play Sunni.lnk' sunni

echo Please zip up the sunni/ folder. This sunni.zip is your distributable.

rm -rf build/
rm -rf dist/
