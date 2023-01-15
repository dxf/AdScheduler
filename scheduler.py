import random, os
from moviepy.editor import VideoFileClip

folders = []
stack = []
length = 0

qty = input('Enter desired quantity of stacks to generate! ')

root = input('Please enter the root path of your adverts directory (including the last backslash): ')
stackqty = input('Please enter the number of advertisers for this event: ')
for i in range(0, int(stackqty)):
    advertiser = input(f'Please enter the directory name for advertiser {i+1}: ')
    folders.append(advertiser)

for loop in range(0,int(qty)):
    for i in folders:
        ch = random.choice(os.listdir(f'{root}\\{i}'))
        stack.append(f'{root}\\{i}\\{ch}')
    for i in stack:
        try:
            clip = VideoFileClip(i)
            length += clip.duration
            clip.close()
        except OSError as e:
            print(e)

    minutes = int(length // 60)
    seconds = round(length % 60)

    with open(f'stacks/Ad Stack {loop} - {minutes}m-{seconds}s.m3u','w') as playlist:
        for i in stack:
            playlist.write(f'{root}{i}\n')
    length = 0
    minutes = 0
    seconds = 0
    stack = []