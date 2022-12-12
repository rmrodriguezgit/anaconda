# Importing all necessary libraries
import cv2
import os
import pytesseract
import openpyxl

# Read the video from specified path
cam = cv2.VideoCapture("../F1-Data-Extractor/replay.mp4")

try:

	# creating a folder named data
	if not os.path.exists('data'):
		os.makedirs('data')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0

# Set up Excel file
wb = openpyxl.Workbook()
sheet = wb.active
colNum = 1
coox_i = 1054
cooy_i = 1442
while(True):

	# reading from frame
	ret,frame = cam.read()

	if ret:

		roi_velocity = frame[1165: 1473 , 1060 : 1192]
		roi_rpm = frame[1508: 1544 , 1058 : 1189]
		roi_gear = frame[1646:1673, 1146 : 1173]
		roi_laptime = frame[1238:1265, 1313:1413]
		roi_laptire = frame[1298:1318, 1333:1367]
		roi_tire = frame[1296:1317, 1375:1397]



		# Tesseract
		custom_config = r'--oem 3 --psm 6'
		#print(pytesseract.image_to_string(roi, config=custom_config))
		velocidad = pytesseract.image_to_string(roi_velocity, config=custom_config)
		rpm = pytesseract.image_to_string(roi_rpm, config=custom_config)
		gear = pytesseract.image_to_string(roi_gear, config=custom_config)
		laptime = pytesseract.image_to_string(roi_laptime, config=custom_config)
		laptire = pytesseract.image_to_string(roi_laptire, config=custom_config)
		tire = pytesseract.image_to_string(roi_tire, config=custom_config)


		#print(f'velocidad = {velocidad}')
		#print(f'RPM = {rpm}')
		#print(f'RPM = {gear}')
		# if video is still left continue creating images
		#name = './data/frame' + str(currentframe) + '.jpg'
		#print ('Creating...' + name)

		# writing the extracted images
		#cv2.imwrite(name, frame)

		try:
			sheet['A'+ str(colNum)].value = int(rpm)
		except:
			sheet['A'+ str(colNum)].value = rpm

		try:
			sheet['B'+ str(colNum)].value = int(gear)
		except:
			sheet['B'+ str(colNum)].value = gear

		try:
			sheet['C'+ str(colNum)].value = int(velocidad)
		except:
			sheet['C'+ str(colNum)].value = velocidad

		try:
			sheet['D'+ str(colNum)].value = int(laptime)
		except:
			sheet['D'+ str(colNum)].value = laptime

		try:
			sheet['E'+ str(colNum)].value = int(laptire)
		except:
			sheet['E'+ str(colNum)].value = laptire

		try:
			sheet['F'+ str(colNum)].value = int(tire)
		except:
			sheet['F'+ str(colNum)].value = tire

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1
		colNum += 1
		print(f'Current Frame {currentframe}')
#		if currentframe == 3:
#			break
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
wb.save('dataPerez2.xlsx')
wb.close
