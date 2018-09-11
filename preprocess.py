import argparse

import cv2
import numpy as np


# argparse
parser = argparse.ArgumentParser(usage="postprocess.py -i <input_video> -o <output_video>")
parser.add_argument("-i", "--input-video", type=str, required=True, help="input video")
parser.add_argument("-o", "--output-video", type=str, required=True, help="output video")
parser.add_argument("-e", "--edge", type=float, required=True, help="edge")


def main(args):
	argedge = args.edge

	# Read video
	input_cap = cv2.VideoCapture(args.input_video)
	
	# Define the codec and create VideoWriter object
	fps = 24
	w = 4096
	h = 2160
	fourcc = cv2.VideoWriter_fourcc(*'H264')
	out = cv2.VideoWriter(args.output_video, fourcc, fps, (w, h), True)
	
	count = 0
	while input_cap.isOpened():
		input_ret, input_img = input_cap.read()
		
		if input_ret == True:
			# bilateral blur
			result = cv2.bilateralFilter(input_img.astype('float32'), 15, 20, 20)
			
			# edge enhancement
			blur = cv2.GaussianBlur(result, (5, 5), 3);
			result = cv2.addWeighted(result, 3, blur, -2, 0);
			
			# clip color
			result = np.clip(result, 0, 255)
				
			#result = input_img.astype('float32')
			
			# add canny edge
			edges = cv2.Canny(result.astype('uint8'), argedge, argedge).astype('float32')
			
			result[:,:,0] = result[:,:,0] - edges
			result[:,:,1] = result[:,:,1] - edges
			result[:,:,2] = result[:,:,2] - edges
			
			# let image range in 0 ~ 255
			result = np.clip(result, 0, 255)
			
			# write the frame
			result = result.astype('uint8')
			out.write(result)
			
			print count
			count += 1
			
			'''
			if count == 6:
				break;
			'''
			
		else:
			break
			
	# Release everything if job is finished
	input_cap.release()
	out.release()

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)