import argparse

import cv2
import numpy as np


# argparse
parser = argparse.ArgumentParser(usage="optflow.py -i <input_video> -o <output_video>")
parser.add_argument("-i", "--input-video", type=str, required=True, help="input video")
parser.add_argument("-o", "--output-video", type=str, required=True, help="output video")
#parser.add_argument("-g1", "--gamma1", type=float, required=True, help="gamma1")
#parser.add_argument("-g2", "--gamma2", type=float, required=True, help="gamma2")


def main(args):	
	gamma1 = 0.95
	gamma2 = 0.75

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
			result = cv2.addWeighted(result, 2, blur, -1, 0);
			
			# clip color
			result = np.clip(result, 0, 255)
			
			# increase saturation on HSV
			result = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
			result[:, :, 1] = (pow((result[:, :, 1] / 255), gamma1) * 255);
			result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
			
			# clip color
			result = np.clip(result, 0, 255)

			# increase lightness on HLS
			result = cv2.cvtColor(result, cv2.COLOR_BGR2HLS)
			result[:, :, 1] = (pow((result[:, :, 1] / 255), gamma2) * 255);
			result = cv2.cvtColor(result, cv2.COLOR_HLS2BGR)
			
			# clip color
			result = np.clip(result, 0, 255)
			
			#result = cv2.GaussianBlur(result, (3, 3), 3);
			
			# clip color
			result = np.clip(result, 0, 255)
			
			# write the frame
			result = result.astype('uint8')
			out.write(result)
			
			'''
			cv2.imwrite(
				args.output_video,
				result,
				[int(cv2.IMWRITE_JPEG_QUALITY), 100]
				)
			break;
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
	out.release()

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)