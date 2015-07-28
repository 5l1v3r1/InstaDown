# coding=utf-8
__author__ = 'kandalf'
import json,urllib2
class InstaDown(object):
    def __init__(self):
        self.token = "" #Instagram developer token id. Get your own!
        self.id = ""  # Instagram User ID
        self.count = "" # Media count of user. How many photos user have.
        self.url = ""  # Global variable of getMedia()'s url variable. It will change to instagram api's next_url in loop.

    def getID(self,username): #function for getting user id
        url = "https://api.instagram.com/v1/users/search?q=" + username + "&access_token=" + self.token
        jsondata = urllib2.urlopen(url)
        j = json.load(jsondata)
        self.id = j["data"][0]["id"]

    def getMediaCount(self): #function for getting media count
        url = "https://api.instagram.com/v1/users/" + self.id + "/?access_token=" + self.token
        try:
            jsondata = urllib2.urlopen(url)
        except urllib2.HTTPError:
            print "User locked and not in your friend list !"
        else:
            j = json.load(jsondata)
            self.count = j["data"]["counts"]["media"]

            # Instagram API have restriction. You can get 20 photos per request.
            # Varible "steps" is storage number of total request.
            # Last request can be include less than 20 photos. Variable "left" is storage number of photos have last request.

    def getMedia(self,path):
        self.url = "https://api.instagram.com/v1/users/" + self.id + "/media/recent/?access_token=" + self.token
        try:
            jsondata = urllib2.urlopen(self.url)
        except urllib2.HTTPError:
            print "User locked and not in your friend list !"
        else:
            j = json.load(jsondata)
            if self.count <= 20:
                for n in range(0,self.count):
                    self.downloadPhoto(j["data"][n]["images"]["standard_resolution"]["url"], n,path)
            else:
                steps = self.count // 20
                left = self.count % 20
                for step in range(0,steps):
                    jsondata = urllib2.urlopen(self.url)
                    j = json.load(jsondata)
                    for n in range(0, 20):
                        self.downloadPhoto(j["data"][n]["images"]["standard_resolution"]["url"], 20* step + n,path)
                    self.url = j["pagination"]["next_url"]
                for n in range(0,left):
                    jsondata = urllib2.urlopen(self.url)
                    j = json.load(jsondata)
                    self.downloadPhoto(j["data"][n]["images"]["standard_resolution"]["url"], 20* (step+1) + n,path)

    def downloadPhoto(self , url, pn,path):
        fileName = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(path + fileName, 'wb')
        blockSize = 4096
        while True:
            buffer = u.read(blockSize)
            if not buffer:
                break
            f.write(buffer)
        f.close()
        status = r"[%3.2f%%]" % (pn * 100. / (self.count-1))
        print status,
        print "Downloading: #%s" % (pn+1)