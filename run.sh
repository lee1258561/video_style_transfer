#time python preprocess.py -i source/video/${1}.mp4 -o result/edge/${1}_pre.mp4 -e ${2}
#time python optflow.py -s result/edge/${1}_pre.mp4 -i source/video/${1}.mp4 -o result/edge/${1}_opt.mp4
#time python postprocess.py -i result/edge/${1}_opt.mp4 -o result/edge/${1}_post_${3}_${4}.mp4 -g1 ${3} -g2 ${4}

time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_99_70_0.mp4 -g1 99 -g2 70 -he 0
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_99_70_1.mp4 -g1 99 -g2 70 -he 1
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_99_50_0.mp4 -g1 99 -g2 50 -he 0
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_99_50_1.mp4 -g1 99 -g2 50 -he 1
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_97_70_0.mp4 -g1 97 -g2 70 -he 0
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_97_70_1.mp4 -g1 97 -g2 70 -he 1
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_97_50_0.mp4 -g1 97 -g2 50 -he 0
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_97_50_1.mp4 -g1 97 -g2 50 -he 1
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_95_70_0.mp4 -g1 95 -g2 70 -he 0
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_95_70_1.mp4 -g1 95 -g2 70 -he 1
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_95_50_0.mp4 -g1 95 -g2 50 -he 0
time python postprocess.py -i result/${1}_door_3_opt.mp4 -o result/new/${1}_door_3_post_95_50_1.mp4 -g1 95 -g2 50 -he 1