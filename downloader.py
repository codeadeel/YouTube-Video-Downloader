#!/usr/bin/env python3

"""
YOUTUBE VIDEO DOWNLOADER
========================

The follwoing program is used to download livestream & fully uploaded videos form YouTube
"""

# %%
# Importing Libraries
import os
import argparse

# %%
# Execution
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='YouTube Video Downloader.')
    parser.add_argument('-l', '--link', metavar = '', type = str, help ='YouTube Link to Download Livestream from', required = True)
    parser.add_argument('-qc', '--quality_check', action = 'store_true', help ='Check Available Qualities')
    parser.add_argument('-q', '--quality', metavar = '', type = int, help ='Set Video Download Quality', default = 94)
    parser.add_argument('-s', '--save', metavar = '', type = str, help ='Absolute Address to Save Downloaded Video', default = '\'' + os.getcwd() + '/Downloaded_Video.mp4\'')
    parser.add_argument('-fr', '--frame_rate', metavar = '', type = int, help ='Frame Rate to Save the Downloaded Video', default = 30)
    parser.add_argument('-fmpg', '--ffmpeg', metavar = '', type = str, help ='Absolute Address to Standalone FFMPEG File', default = '\'' + os.getcwd() + '/ffmpeg\'')
    parser.add_argument('-ytdl', '--youtube_dl', metavar = '', type = str, help ='Absolute Address to Standalone youtube-dl File', default = '\'' + os.getcwd() + '/youtube-dl\'')
    args = vars(parser.parse_args())
    os.system('chmod 777 ' + args['ffmpeg'])
    os.system('chmod 777 ' + args['youtube_dl'])
    if args['quality_check']:
        os.system(args['youtube_dl'] + ' -F ' + args['link'])
    else:
        os.system(args['ffmpeg'] + ' -i $(' + args['youtube_dl'] + ' -f ' + str(args['quality']) + ' -g ' + args['link'] + ') -r ' + str(args['frame_rate']) + ' ' + args['save'])