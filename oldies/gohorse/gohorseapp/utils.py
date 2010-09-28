from deliciousapi import DeliciousAPI

from models import Url

def default_opener(login, password):
    dapi = DeliciousAPI()
    return dapi.get_user(login, password)

def import_urls_from_delicious(login, password, opener=default_opener):
    bookmarks = opener(login, password)

    ret = []
    for href, tags, title, desc, time in bookmarks:
        url = Url(url=href)
        url.save()
        ret.append(url)

    return ret
