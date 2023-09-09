import requests
import json

def photo_download():
    pass

def link_requset(link):
    response=requests.get(url=link)
    return response

def main(href):
    link_requset(href)
URL=''
main(URL)
