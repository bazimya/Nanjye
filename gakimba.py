import qrcode
name="gakumba"
age="24"
location="kicukiro"
img=qrcode.make('http://rslr.connectbind.com:8080/bulksms/bulksms?username=infk-kiza&password=lab250&type=0&dlr=1&destination=250788522501&source=BAZIMYA&message=Hello sir if you have time may i come and we meet i have aproggress ')

img.save('gakumba.png')
img.show()
