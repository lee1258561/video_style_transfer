import argparse

import cv2
import numpy as np


# argparse
parser = argparse.ArgumentParser(usage="blend.py -a <input_video1> -b <input_video2> -o <output_video>")
parser.add_argument("-a", "--input_video1", type=str, required=True, help="input_video1")
parser.add_argument("-b", "--input-video2", type=str, required=True, help="input video2")
parser.add_argument("-o", "--output-video", type=str, required=True, help="output video")


def main(args):
	# parameter
	a = 0.75
	
	# Read video
	input_cap1 = cv2.VideoCapture(args.input_video1)
	input_cap2 = cv2.VideoCapture(args.input_video2)
	
	# Define the codec and create VideoWriter object
	fps = 24
	w = 4096
	h = 2160
	fourcc = cv2.VideoWriter_fourcc(*'H264')
	out = cv2.VideoWriter(args.output_video, fourcc, fps, (w, h), True)
	
	count = 0
	while input_cap1.isOpened() and input_cap2.isOpened():
		input_ret1, input_img1 = input_cap1.read()
		input_ret2, input_img2 = input_cap2.read()
		
		if input_ret1 == True:											
			result = cv2.addWeighted(input_img1, a, input_img2, (1 - a), 0);
			
			# write the frame
			result = result.astype('uint8')
			out.write(result)
			
			'''
			cv2.imwrite(
				args.output_video,
				result,
				[int(cv2.IMWRITE_JPEG_QUALITY), 100]
				)
			'''
			print count
			count += 1
			
			'''
			if count == 48:
				break
			'''
			
		else:
			break
			
	# Release everything if job is finished
	input_cap1.release()
	input_cap2.release()
	out.release()

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)