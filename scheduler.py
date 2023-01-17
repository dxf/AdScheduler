import random, os
from moviepy.editor import VideoFileClip
import gspread
import numpy as np

folders = []
stack = []
length = 0


gc = gspread.service_account(filename='epic-central-controller-dev.json')

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1eQ-MAD9eheVm9qjLF9bqZyACI3GBu4RmIQJDZpv1vLU/edit")
sheet = wks.worksheet("AdStacks")




qty = input('Enter desired quantity of stacks to generate! ')

root = input('Please enter the root path of your adverts directory (including the last backslash): ')
output = input('Please enter your stacks output directory here (including the last backslash): ')
stackqty = input('Please enter the number of advertisers for this event: ')
for i in range(0, int(stackqty)):
    advertiser = input(f'Please enter the directory name for advertiser {i+1}: ')
    folders.append(advertiser)
content = []
for loop in range(0,int(qty)):
    boneless_stack = []
    for i in range(0,1000):
        random.shuffle(folders)
    for i in folders:
        ch = random.choice(os.listdir(f'{root}\\{i}'))
        stack.append(f'{root}\{i}\\{ch}')
        boneless_stack.append(ch)
    for i in stack:
        try:
            clip = VideoFileClip(i)
            length += clip.duration
            clip.close()
        except OSError as e:
            print(e)

    minutes = int(length // 60)
    seconds = round(length % 60)
    row = [loop+1,f'{minutes}m-{seconds}s',"N"]
    with open(f'{output}Ad Stack {loop+1} - {minutes}m-{seconds}s.m3u','w') as playlist:
        for i in stack:
            playlist.write(f'{i}\n')
    row = row + boneless_stack + [f'{output}Ad Stack {loop+1} - {minutes}m-{seconds}s.m3u']
    content.append(row)

    length = 0
    minutes = 0
    seconds = 0
    stack = []
sheet.update('A2',content)