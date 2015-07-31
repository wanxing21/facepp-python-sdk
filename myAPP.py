# -*- coding: utf-8 -*-

import os
from facepp import *
from PIL import Image, ImageDraw, ImageFont

API_KEY = '417f77e0b783cdc9a99aae0ee7f54fda'
API_SECRET = 'dXlQldhEiZa8PrIRhBCIiOLWadCSV2IZ'

api = API(API_KEY, API_SECRET)
result = api.detection.detect(img = File(os.path.join(os.getcwd(), 'test.jpg')))
face_ID = result['face'][0]['face_id']
landmark = api.detection.landmark(face_id = face_ID)

# im = Image.open(os.path.join(os.getcwd(), 'test.jpg'))
# draw = ImageDraw.Draw(im)
# font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 1)
# count = 0
# r = 1


# for key, value in landmark['result'][0]['landmark'].iteritems():
# 	count += 1
# 	pos_x = value['x'] * 6.4
# 	pos_y = value['y'] * 4.8
# 	print count, 'x', pos_x, 'y', pos_y
# 	draw.arc((int(pos_x - r), int(pos_y - r), int(pos_x + r), int(pos_y + r)), 0 , 360,  fill = (255, 0, 0))
	# draw.text((pos_x, pos_y), str(count))

# im.save('ok.jpg', 'jpeg')
# im.show()

print result
# print landmark['result'][0]['landmark']
# print face_ID

# for key, value in landmark['result'][0]['landmark'].iteritems():
# 	pos_x = value['x']
# 	pos_y = value['y']
# 	print "key:%40s  x:%11.6f  y:%11.6f"  %(key, pos_x, pos_x)

