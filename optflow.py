import argparse

import cv2
import numpy as np


# argparse
parser = argparse.ArgumentParser(usage="optflow.py -s <style_video> -i <input_video> -o <output_video>")
parser.add_argument("-s", "--style-video", type=str, required=True, help="style video")
parser.add_argument("-i", "--input-video", type=str, required=True, help="input video")
parser.add_argument("-o", "--output-video", type=str, required=True, help="output video")


def main(args):
	# parameter
	a = 0.75
	
	# Read video
	input_cap = cv2.VideoCapture(args.input_video)
	style_cap = cv2.VideoCapture(args.style_video)
	
	# Define the codec and create VideoWriter object
	fps = 24
	w = 4096
	h = 2160
	fourcc = cv2.VideoWriter_fourcc(*'H264')
	out = cv2.VideoWriter(args.output_video, fourcc, fps, (w, h), True)
	
	input_ret, input_prev = input_cap.read()
	style_ret, style_prev = style_cap.read()
	
	input_prevgray = cv2.cvtColor(input_prev, cv2.COLOR_BGR2GRAY)
	
	# first frame
	# write the frame
	result = style_prev.astype('uint8')
	out.write(result)
	
	count = 0
	while style_cap.isOpened() and input_cap.isOpened():
		input_ret, input_img = input_cap.read()
		style_ret, style_img = style_cap.read()
		
		if style_ret == True:
			input_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
			
			flow = cv2.calcOpticalFlowFarneback(input_gray, input_prevgray, None, 0.5, 3, 30, 3, 5, 1.2, 0)
			
			# interpolate prev and img by optflow
			for i in range(h):
				for j in range(w):
					result[i, j] = style_prev[
											min(h - 1, i + int(flow[i, j, 1])),
											min(w - 1, j + int(flow[i, j, 0]))
											]
											
			result = cv2.addWeighted(result, a, style_img, (1 - a), 0);
			
			input_prevgray = input_gray
			style_prev = result.astype('uint8')
			
			
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
			if count == 12:
				break
			'''
			
		else:
			break
			
	# Release everything if job is finished
	input_cap.release()
	style_cap.release()
	out.release()

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)