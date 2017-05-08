echo -ne "ATD $1;\r\n" > /dev/ttyUSB2
cat /dev/ttyUSB2
sleep $2
echo -ne "AT+CHUP\r\n" > /dev/ttyUSB2
cat /dev/ttyUSB2
