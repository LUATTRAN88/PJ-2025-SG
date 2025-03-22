  GNU nano 8.1                   loadbank_script.sh
cd  /home/loadbank/PJ-2025-SG/Toan/test\ demo/gui_test/
fuser -k /dev/ttyUSB0
echo "123456" | sudo -S -k chmod a+rw /dev/ttyUSB0
pkill -9 python
python3 main.py
