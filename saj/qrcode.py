import pyqrcode, qrtools, time, csv

with open ('inventory.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='	')
	iterrow = iter(reader)
	next(iterrow)	
	for row in iterrow:			
		qr_encode = pyqrcode.create('	'.join(row))
		qr_encode.png(row[0], scale=6)
		
		## for decode 		
		#time.sleep(3)
		#qr_decode = qrtools.QR()
		#qr_decode.decode(row[0])
		#print qr_decode.data
		
