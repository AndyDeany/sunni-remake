#!/bin/bash
VENV=build-venv
python -m venv $VENV
if [[ "$OSTYPE" == "msys" ]]; then
  source $VENV/Scripts/activate
else
  source $VENV/bin/activate
fi
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

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

tar -a -c -f sunni.zip sunni/

rm -rf sunni/
rm -rf build/
rm -rf dist/
rm main.spec

deactivate
rm -rf $VENV
