# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

# from moviepy_effetcs import *
from generate_sequence import *
from files_scanner import *
from text_tools import *
from image_tools import *

class VideoEditor():
	pass

def test():
	pass

''' 
# Так, чо мне надо сюда написать. Нужен composite video clip - сначала рандомная нарезка, потом каждый из этих кадров в рандомном месте смешивается с картинкой. А чтобы сделать композит, необходимо загрузить картинку во внутенний тип или просто? Нужны доки.
- Нужно подгрузить в кастомный тип, а потом каждый из клипов смешать с подгруженными имейджами.
## Ещё надо взять сайз клипа из готового скрипта по текстам и плейсить картинку в размере этого клипа. У меня есть заготовка "add_rand_placed_image"
'''
# =======================================================================OUT====================================
path = '../shaker/'
pathImages = '../imgShaker'
print(files_scanner_video(path))
print(files_scanner_images(pathImages, 1))
exec_numb = 5
dur = []
textEffects = ["Blur", "Mirror", "BlackCircle", "Fractal", "DoubleFace", "Glitchface", ]

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	imagesList = files_scanner_images(pathImages, 1)
	clipsCounter = len(clipsList) - 1
	imagesCounter = len(imagesList) - 1
	for i, objects in enumerate(clipsList[::1]):
		for j in range(0,3):
		# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 5))
			# clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 4))
			# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 4)))
			# clips.append(imagesList[randclip(imagesCounter)])
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
			clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 5))
			# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, random.uniform(1, 3)))
			# clips.append(imagesList[randclip(imagesCounter)])
			# clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
			# clips.append(generate_sequence(clipsList[randclip(clipsCounter)], [6.7, 6.8])
	for i, objects in enumerate(clips):
		clips[i] = add_rand_placed_image(clips[i], imagesList[randclip(imagesCounter)])
		
	concat_and_write(clips, exec_numb)

def resulst_store(clips, exec_numb):
	pass

def concat_and_write(clips, exec_numb):
	write_data = time.strftime("%I%M%S")
	print(write_data)
	try:
		clipOut = concatenate_videoclips(clips, method='compose')
		clipOut.write_videofile("./" + write_data + "-out.mp4",fps=25)
	except Exception as e:
		print(str(e))
		print("An error occured, try {} times".format(exec_numb))
		if exec_numb > 0:
			exec_numb -= 1
			cut_logic(exec_numb)
		else:
			print("game over")


cut_logic(exec_numb)