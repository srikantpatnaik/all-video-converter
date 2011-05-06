#!/usr/bin/env python
from subprocess import Popen, PIPE
import os

os.system('mkdir -p converted_videos original_videos original_videos/.tmp')
    
def rendering_text(input_file, output_file):
     stdout = Popen('mencoder -oac mp3lame -lameopts cbr=128 -ovc xvid -xvidencopts bitrate=300 original_videos/.tmp/%s -o converted_videos/%s' % (input_file , output_file),shell=True, stdout=PIPE).stdout
 
     print "Converting %s to %s " %(input_file,output_file)
     stdout.read()
     return 
os.system('cd original_videos/ && mv *.flv *.FLV *.mp4 *.MP4 *.mpg *.MPG *.dat *.DAT .tmp/')  ### add supported input video formats 

stdout = Popen('cd original_videos/.tmp/ && ls -1',shell=True, stdout=PIPE).stdout

video_files=[]

#get the list of files from pipe output
video_files = stdout.read()

video_files = video_files.strip().split('\n')
print "Converting %d file(s)." %len(video_files)

for i, input_file in enumerate(video_files):
        output_file = '%s.%s' %(input_file,'avi')  ### Change 'avi' with any other format you want
	print "Converting %d of %d file(s)..." %(i+1, len(video_files))
        rendering_text(input_file, output_file)
 
os.system('rm -rf original_videos/.tmp/')
