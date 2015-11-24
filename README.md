#Youtube Playlist Downloader

### Youtube Playlist Downloader

* 기존에 유튜브 동영상 다운로더는 단일 동영상만 가능
* 플레이 리스트 링크를 넘기면 해당 플레이리스트 다운로드

### Usage

**single video**

	from youtube_playlist_downloader.youtube_mp3_download import *

	YoutubeSingleDownloader("<video_link>").music_single_downloader()

**video list**

	from youtube_playlist_downloader.youtube_mp3_download import *

	YoutubePlaylistDownloader("<list_link>").music_list_downloader()


### Requirements
* FFMPEG binary (https://www.ffmpeg.org/)