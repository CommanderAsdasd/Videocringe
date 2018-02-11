# -*- coding: utf-8 -*-
# C:/Python27/python.exe
from moviepy.editor import *
from moviepy.video.fx.all import *
import random
import time

from generate_sequence import *
from files_scanner import *
import sys

class VideoEditor():
	pass

def test():
	pass


# =======================================================================OUT====================================

def randclip(maxclips):
	return random.randint(0, maxclips)

def cut_logic(exec_numb):
	clips = []
	print(clips)
	clipsList = files_scanner_video(path)
	clipsCounter = len(clipsList) - 1
	for i, objects in enumerate(clipsList[::1]):
		for j in range(0, 4):
			clips.append(generate_rand_sequence(clipsList[randclip(clipsCounter)], 0, random.uniform(1, 4)))
			clips.append(loop(generate_rand_sequence(clipsList[randclip(clipsCounter)], 1, 0.2), 3))
		if i % random.randint(2, 3) == 0:
			clips[i] = time_symmetrize(clips[i])

	concat_and_write(clips, exec_numb)

def resulst_store(clips, exec_numb):
	pass


if __name__ == "__main__":
	try:
		path = sys.argv[1]
		print(files_scanner_video(path))
		exec_numb = 5
		dur = []
		cut_logic(exec_numb)
	except IndexError as e:
		# print(str(e))
		print("please enter the path")