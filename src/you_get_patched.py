#!/usr/bin/env python3


# This is a runtime patcher
# Patch you-get at runtime to make it provide enouth message for MoonPlayer


# Init environment and import module
import os, sys, json, platform, io
if platform.system() == 'Darwin':
    _srcdir = '%s/Library/Application Support/MoonPlayer/you-get/src/' % os.getenv('HOME')
else:
    _srcdir = '%s/moonplayer/you-get/src/' % os.getenv('XDG_DATA_HOME', os.getenv('HOME') + '/.local/share')
_filepath = os.path.dirname(sys.argv[0])
sys.path.insert(0, _srcdir)
import you_get


unseekables = []


# Patch json_output.output
def output(video_extractor, pretty_print=True):
    ve = video_extractor
    out = {}
    out['url'] = ve.url
    out['title'] = ve.title
    out['site'] = ve.name
    out['seekable'] = not ve.name in unseekables
    out['streams'] = ve.streams
    if getattr(ve, 'dash_streams', None) and len(ve.dash_streams):
        out['dash_streams'] = ve.dash_streams
    if getattr(ve, 'audiolang', None):
        out['audiolang'] = ve.audiolang
    if getattr(ve, 'ua', None):
        out['user-agent'] = ve.ua
    if getattr(ve, 'danmuku', None) and ve.danmuku.startswith('http'):
        out['danmaku_url'] = ve.danmuku
    if getattr(ve, 'referer', None):
        out['referer'] = ve.referer
    else:
        try:
            out['referer'] = ve.streams['__default__']['refer']
        except KeyError:
            pass

    if pretty_print:
        print(json.dumps(out, indent=4, sort_keys=True, ensure_ascii=False))
    else:
        print(json.dumps(out))
import you_get.json_output
you_get.json_output.output = output


# Patch bilibili
def get_danmuku_xml(cid):
    return 'http://comment.bilibili.com/{}.xml'.format(cid)
from you_get.extractors import bilibili
bilibili.get_danmuku_xml = get_danmuku_xml


# Run you-get
if __name__ == '__main__':
    you_get.main(repo_path=_filepath)
