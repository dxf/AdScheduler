# AdScheduler

*Automatic advert scheduling for Vmix and other m3u-based clients.*

This script is a simple solution for generating advert playlists for live broadcast, allowing for accurate timing for running orders etc.

It works by taking a root directory, i.e a Samba share, or the directory in which they live in on the playout client.

Each advertiser has their own directory full of video files, and AdScheduler will pick a random video file from each advertiser, and compile a 'stack' of however many adverts that takes. That then outputs into a Vmix-friendly m3u file, containing 1 ad from each advertiser, with the length of each stack clearly viewable in the filename.

## To-do

* Shuffle stack before playlist is written.
* Make the output directory configurable. It currently needs a folder called `stacks` to run.
* Output to CSV/Google sheet for easy tracking of which stacks have been used

## Requirements
* Python 3.11
* `pip install -r requirements.txt`