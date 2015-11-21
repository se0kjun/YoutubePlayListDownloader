#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import sys,os

from youtube_playlist_downloader import youtube_mp3_download

def yt_download(playlist_link):
	youtube = youtube_mp3_download.YoutubePlaylistDownloader(playlist_link)
	pl_list = youtube.music_download()
	fail_list = []

	for pl in pl_list:
		if not pl.result:
			fail_list.append(pl.title[0].decode('unicode_escape').encode('ascii','ignore'))
			continue
		# CORS
		headers = { 'User-Agent': None, 'Access-Control-Allow-Origin' : '*' }
		try:
			# parse할때 str로 바꾸는것 때문에 [""]가 문자열 처리되면서 앞뒤를 잘라내는 부분이 추가 / 나중에 수정해야
			req = urllib2.Request(pl.link[0][2:-2], None, headers)
			file1 = open('output', 'wb')
			req = urllib2.Request(pl.link[0][2:-2], None, headers)
			s = urllib2.urlopen(req).read()
			file1.write(s)
			sys.stdout.flush()

			# ffmpeg 필요
			cmd = 'ffmpeg -i output -acodec libmp3lame -aq 4 \'%s.mp3\'' % pl.title[0].decode('unicode_escape').encode('ascii','ignore')

			os.system(cmd);
		except urllib2.HTTPError as e:
			# exception fail list
			fail_list.append(pl.title[0].decode('unicode_escape').encode('ascii','ignore'))
			pass

	#return fail
	return fail_list

if __name__ == '__main__':
	# print download.yt_download(sys.argv[1])
    print yt_download("https://www.youtube.com/playlist?list=PLkMRAPworbEffRLXVVAc-etlLIYGlPHvp")
