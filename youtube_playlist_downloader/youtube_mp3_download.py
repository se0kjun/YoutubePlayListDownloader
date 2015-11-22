# -*- coding: utf-8 -*-

import urllib2
import re
import sys,os

from bs4 import BeautifulSoup
from youtube_pack import YoutubePack

'''
YoutubePlaylistDownloader
Youtube play list를 다운로드하기위함

get_music_list
링크상에서 플레이리스트가 존재하면 해당 플레이 리스트에 존재하는 음악의 링크를 가져옴

music_download
각 링크에 방문하여 해당 동영상의 소스 링크, 타이틀, 등의 정보를 가져옴

데이터 예시
fallback_host=tc.v15.cache2.googlevideo.com\u0026type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22\u0026url=https%3A%2F%2Fr4---sn-ab02a0nfpgxapox-bh26.googlevideo.com%2Fvideoplayback%3Fsignature%3D468DBD00E3D305A4F206873D45D170809A7A4AB8.2927A3FC1ADBAD7E962F2C6B95B99E6CB238EC12%26ms%3Dau%26mt%3D1434975789%26pl%3D18%26mv%3Dm%26mm%3D31%26mn%3Dsn-ab02a0nfpgxapox-bh26%26key%3Dyt5%26sver%3D3%26mime%3Dvideo%252Fwebm%26expire%3D1434997519%26ratebypass%3Dyes%26ipbits%3D0%26initcwndbps%3D2607500%26upn%3DP5sx0Y9eCoE%26fexp%3D3300102%252C3300134%252C3300137%252C3300161%252C3310754%252C3311907%252C3312195%252C923611%252C9407141%252C9408142%252C9408207%252C9408420%252C9408710%252C9413503%252C9414612%252C9414626%252C9414656%252C9415304%252C9415554%252C9416126%252C9416285%252C9416456%252C952640%26sparams%3Ddur%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpcm2cms%252Cpl%252Cratebypass%252Crequiressl%252Csource%252Cupn%252Cexpire%26dur%3D0.000%26pcm2cms%3Dyes%26source%3Dyoutube%26id%3Do-APYBEaDKqHKxAnBINnpw8mpVSZfHtXK-VybHkVzGvxip%26requiressl%3Dyes%26lmt%3D1431846669717664%26itag%3D43%26ip%3D112.148.17.28\u0026quality=medium\u0026itag=43,fallback_host=tc.v13.cache2.googlevideo.com\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.42001E%2C+mp4a.40.2%22\u0026url=https%3A%2F%2Fr4---sn-ab02a0nfpgxapox-bh26.googlevideo.com%2Fvideoplayback%3Fsignature%3D54FE6CB9FCABD10B2D6376DC1B1DB758D0B11771.3BDB039406D9A9F8BC905FA2A5356208E0B2B4BF%26ms%3Dau%26mt%3D1434975789%26pl%3D18%26mv%3Dm%26mm%3D31%26mn%3Dsn-ab02a0nfpgxapox-bh26%26key%3Dyt5%26sver%3D3%26mime%3Dvideo%252Fmp4%26expire%3D1434997519%26ratebypass%3Dyes%26ipbits%3D0%26initcwndbps%3D2607500%26upn%3DP5sx0Y9eCoE%26fexp%3D3300102%252C3300134%252C3300137%252C3300161%252C3310754%252C3311907%252C3312195%252C923611%252C9407141%252C9408142%252C9408207%252C9408420%252C9408710%252C9413503%252C9414612%252C9414626%252C9414656%252C9415304%252C9415554%252C9416126%252C9416285%252C9416456%252C952640%26sparams%3Ddur%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpcm2cms%252Cpl%252Cratebypass%252Crequiressl%252Csource%252Cupn%252Cexpire%26dur%3D213.228%26pcm2cms%3Dyes%26source%3Dyoutube%26id%3Do-APYBEaDKqHKxAnBINnpw8mpVSZfHtXK-VybHkVzGvxip%26requiressl%3Dyes%26lmt%3D1431846094662600%26itag%3D18%26ip%3D112.148.17.28\u0026quality=medium\u0026itag=18,fallback_host=tc.v1.cache7.googlevideo.com\u0026type=video%2Fx-flv\u0026url=https%3A%2F%2Fr4---sn-ab02a0nfpgxapox-bh26.googlevideo.com%2Fvideoplayback%3Fsignature%3D056E6A98B7B076090FCE3C5E2E15D38318CBD292.C5AC9EC66C38325F91E8BE54E4BEE1A4BCDF787C%26ms%3Dau%26mt%3D1434975789%26pl%3D18%26mv%3Dm%26mm%3D31%26mn%3Dsn-ab02a0nfpgxapox-bh26%26key%3Dyt5%26sver%3D3%26mime%3Dvideo%252Fx-flv%26expire%3D1434997519%26ipbits%3D0%26initcwndbps%3D2607500%26upn%3DP5sx0Y9eCoE%26fexp%3D3300102%252C3300134%252C3300137%252C3300161%252C3310754%252C3311907%252C3312195%252C923611%252C9407141%252C9408142%252C9408207%252C9408420%252C9408710%252C9413503%252C9414612%252C9414626%252C9414656%252C9415304%252C9415554%252C9416126%252C9416285%252C9416456%252C952640%26sparams%3Ddur%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpcm2cms%252Cpl%252Crequiressl%252Csource%252Cupn%252Cexpire%26dur%3D213.211%26pcm2cms%3Dyes%26source%3Dyoutube%26id%3Do-APYBEaDKqHKxAnBINnpw8mpVSZfHtXK-VybHkVzGvxip%26requiressl%3Dyes%26lmt%3D1431845292049831%26itag%3D5%26ip%3D112.148.17.28\u0026quality=small\u0026itag=5,fallback_host=tc.v16.cache6.googlevideo.com\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026url=https%3A%2F%2Fr4---sn-ab02a0nfpgxapox-bh26.googlevideo.com%2Fvideoplayback%3Fsignature%3D50ED336C9100E92367D5CA8137950B1D0DA06B3D.6ABC19E7449F0DF236E8124B4AA2DB3C88645580%26ms%3Dau%26mt%3D1434975789%26pl%3D18%26mv%3Dm%26mm%3D31%26mn%3Dsn-ab02a0nfpgxapox-bh26%26key%3Dyt5%26sver%3D3%26mime%3Dvideo%252F3gpp%26expire%3D1434997519%26ipbits%3D0%26initcwndbps%3D2607500%26upn%3DP5sx0Y9eCoE%26fexp%3D3300102%252C3300134%252C3300137%252C3300161%252C3310754%252C3311907%252C3312195%252C923611%252C9407141%252C9408142%252C9408207%252C9408420%252C9408710%252C9413503%252C9414612%252C9414626%252C9414656%252C9415304%252C9415554%252C9416126%252C9416285%252C9416456%252C952640%26sparams%3Ddur%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpcm2cms%252Cpl%252Crequiressl%252Csource%252Cupn%252Cexpire%26dur%3D213.391%26pcm2cms%3Dyes%26source%3Dyoutube%26id%3Do-APYBEaDKqHKxAnBINnpw8mpVSZfHtXK-VybHkVzGvxip%26requiressl%3Dyes%26lmt%3D1431846128599998%26itag%3D36%26ip%3D112.148.17.28\u0026quality=small\u0026itag=36,fallback_host=tc.v15.cache3.googlevideo.com\u0026type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22\u0026url=https%3A%2F%2Fr4---sn-ab02a0nfpgxapox-bh26.googlevideo.com%2Fvideoplayback%3Fsignature%3DC2B9D54EC33C2A976CC0F46266F4F5B46171CF9C.B4F0975EA25034FEE1A174E42C33D78863C87700%26ms%3Dau%26mt%3D1434975789%26pl%3D18%26mv%3Dm%26mm%3D31%26mn%3Dsn-ab02a0nfpgxapox-bh26%26key%3Dyt5%26sver%3D3%26mime%3Dvideo%252F3gpp%26expire%3D1434997519%26ipbits%3D0%26initcwndbps%3D2607500%26upn%3DP5sx0Y9eCoE%26fexp%3D3300102%252C3300134%252C3300137%252C3300161%252C3310754%252C3311907%252C3312195%252C923611%252C9407141%252C9408142%252C9408207%252C9408420%252C9408710%252C9413503%252C9414612%252C9414626%252C9414656%252C9415304%252C9415554%252C9416126%252C9416285%252C9416456%252C952640%26sparams%3Ddur%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpcm2cms%252Cpl%252Crequiressl%252Csource%252Cupn%252Cexpire%26dur%3D213.344%26pcm2cms%3Dyes%26source%3Dyoutube%26id%3Do-APYBEaDKqHKxAnBINnpw8mpVSZfHtXK-VybHkVzGvxip%26requiressl%3Dyes%26lmt%3D1431846107085506%26itag%3D17%26ip%3D112.148.17.28\u0026quality=small\u0026itag=17
위 데이터는 url_encoded_fmt_stream_map의 데이터임
'''
class YoutubeBaseDownloader():
    base_url = "https://www.youtube.com"

    def music_info(self, play_link):
        headers = { 'User-Agent': None }
        req = urllib2.Request(play_link, None, headers)
        s = urllib2.urlopen(req).read()
        # json에서 title정보 가져옴
        music_title = re.findall(r'"title":"(.*?)"', s)
        # json에서 music data 가져옴
        music_meta = re.findall(r'"url_encoded_fmt_stream_map":"(.*?)"', s)
        # music data는 비디오 품질에 따라 나뉘어져있음 
        music_meta_list = re.split(',', music_meta[0])
        # 비디오 품질
        # video_type = re.findall(r'type=(.*?)u0026', music_meta[0])

        # url parse (\\u0026 or ;)
        url_parse = []
        for video_link in music_meta_list:
            url_parse.append(str(re.findall(r'url=(.*?)u0026', urllib2.unquote(video_link)))[:-2])

        # youtube링크에서 v의 값을 가져옴
        v = re.search(r'v=(.*?)(&|$)', play_link).group(1)

        d = {
            'title' : music_title,
            'link' : url_parse,
            'origin_data' : music_meta,
            'v' : 'v',
            'result' : True if url_parse[0] != '' else False,
            # 'type' : video_type,
        }
        
        return YoutubePack(**d)

    def music_downloader(self, pl):
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
            
            return False

        return True

class YoutubePlaylistDownloader(YoutubeBaseDownloader):
    # base_url = "https://www.youtube.com"
    playlist_link = []

    def __init__(self, youtube_playlist_link):
        self.youtube_playlist_link = youtube_playlist_link
        self.get_music_list()

    def get_music_list(self):
        headers = { 'User-Agent': None }
        req = urllib2.Request(self.youtube_playlist_link, None, headers)
        self.play_data = urllib2.urlopen(req).read()
        yt_soup = BeautifulSoup(self.play_data)

        for link in yt_soup.select("a.pl-video-title-link"):
            self.playlist_link.append(self.base_url + link.get('href'))
        for link in yt_soup.select("a.playlist-video"):
            self.playlist_link.append(self.base_url + link.get('href'))

        return self.playlist_link

    def music_list_downloader(self):
        data = []
        for play_link in self.playlist_link:
            d = self.music_info(play_link)
            res = self.music_downloader(d)

        return data

class YoutubeSingleDownloader(YoutubeBaseDownloader):
    def __init__(self, play_link):
        self.play_link = play_link

    def music_single_downloader(self):
        d = self.music_info(self.play_link)
        return self.music_downloader(d)

