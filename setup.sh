#!/bin/bash

echo "Downloading Selenium Web Driver ..."
curl -L https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip -o chromedriver.zip
unzip chromedriver.zip
rm -f chromedriver.zip

echo "Setting Up Python Environment  ..."
python3 get-pip.py --user
pip3 install selenium --user
pip3 install requests --user
