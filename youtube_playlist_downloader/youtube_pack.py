# -*- coding: utf-8 -*-
from collections import namedtuple

_checked = namedtuple('YoutubePack', ['result', 'origin_data', 'title', 'link', 'v'])

class YoutubePack(_checked):
    def __new__(cls, result=False, origin_data='', title='', link='', v=''):
        return super(YoutubePack, cls).__new__(cls, result, origin_data, title, link, v)

    def as_dict(self):
        d = {
            'result': self.result,
            'origin_data': self.origin_data,
            'title': self.title,
            'link': self.link,
            'v': self.v,
            # https://i.ytimg.com/vi_webp/[v]/hqdefault.webp
            'thumbnail': "https://i.ytimg.com/vi_webp/" + self.v + "/hqdefault.webp",
        }
        return d