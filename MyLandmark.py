# -*- coding: utf-8 -*-

import os, time
from facepp import *
from PIL import Image, ImageDraw

API_KEY = '417f77e0b783cdc9a99aae0ee7f54fda'
API_SECRET = 'dXlQldhEiZa8PrIRhBCIiOLWadCSV2IZ'

# 读取图像
def readImage(imagePath):
	imageList = []
	fileList = os.listdir(imagePath)
	for image in fileList:
		if os.path.isfile(os.path.join(imagePath,image)) and image[-3:].lower() == 'jpg':
			imageList.append(image)

	return imageList

def saveLandmark(outputPath, imageFileName, landmarkPos, img_width, img_height, draw):
	r = 1
	imageName = os.path.splitext(imageFileName)[0]
	landmarkFile = open(os.path.join(outputPath, imageName + '.pts'), 'w')
	landmarkFile.write('version: 1\n')
	landmarkFile.write('n_points: %d\n' %len(landmarkPos))
	landmarkFile.write('{\n')
	for key, value in landmarkPos.iteritems():
		pos_x = value['x'] * img_width / 100.0
		pos_y = value['y'] * img_height / 100.0
		landmarkFile.write('%.3f %.3f\n' %(pos_x, pos_y))
		draw.arc((int(pos_x - r), int(pos_y - r), int(pos_x + r), int(pos_y + r)), 0 , 360,  fill = (255, 0, 0))
	landmarkFile.write('}\n')
	landmarkFile.close()


def getLandmarkFromFacepp(imagePath, outputPath, imageList):
	api = API(API_KEY, API_SECRET)
	for image in imageList:
		print 'image:' + image
		result = api.detection.detect(img = File(os.path.join(imagePath, image)))
		im = Image.open(os.path.join(os.path.join(imagePath, image)))
		draw = ImageDraw.Draw(im)
		img_width = result['img_width']
		img_height = result['img_height']
		face_ID = result['face'][0]['face_id']
		landmark = api.detection.landmark(face_id = face_ID)
		saveLandmark(outputPath, image, landmark['result'][0]['landmark'], img_width, img_height , draw)
		im.save(os.path.join(outputPath, image), 'jpeg')
		im.show()

if __name__ == '__main__':
	imagePath = 'D:\\code\\facepp-python-sdk\\image'
	outputPath = 'D:\\code\\facepp-python-sdk\\image\\point'
	imageList = readImage(imagePath)
	print 'start...  image_count', len(imageList)
	getLandmarkFromFacepp(imagePath, outputPath, imageList)
	print 'end!'