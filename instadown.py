# coding=utf-8
__author__ = 'kandalf'
import os,json,urllib2

class InstaDown(object):
	def __init__(self,token):
		self.token = token 

	def getUserID(self,username): 
		url = "https://api.instagram.com/v1/users/search?q=" + username + "&access_token=" + self.token
		jsondata = urllib2.urlopen(url)
		j = json.load(jsondata)
		return j["data"][0]["id"]

	def getMediaCount(self,userId): #function for getting media count
		url = "https://api.instagram.com/v1/users/" + userId + "/?access_token=" + self.token
		try:
			jsondata = urllib2.urlopen(url)
		except urllib2.HTTPError:
			print "User locked nor not in your friend list !"
		else:
			j = json.load(jsondata)
			return j["data"]["counts"]["media"]

	# Instagram API have restriction. You can get only 20 photos per request.
	# The variable "steps" is store that number of steps (Number of photos / 20).
	# If number of photos didn't multiple of 20, the "left" variable store that how many photos left for last request.

	def getMedia(self,path,userId,mediaCount,download):
		url = "https://api.instagram.com/v1/users/" + userId + "/media/recent/?access_token=" + self.token
		urlList = []
		try:
			jsondata = urllib2.urlopen(url)
		except urllib2.HTTPError:
			print "User locked nor not in your friend list !"
		else:
			j = json.load(jsondata)
			if mediaCount <= 20:
				for n in range(0,mediaCount):
					if download:
						self.downloadPhoto(j["data"][n]["images"]["standard_resolution"]["url"], n,path,mediaCount)
					else:
						urlList.append(j["data"][n]["images"]["standard_resolution"]["url"])
			else:
				steps = mediaCount // 20
				left = mediaCount % 20
				for step in range(0,steps):
					jsondata = urllib2.urlopen(url)
					j = json.load(jsondata)
					for n in range(0, 20):
						if download:
							self.downloadPhoto(j["data"][n]["images"]["standard_resolution"]["url"], 20 * step + n,path,mediaCount)
						else:
							urlList.append(j["data"][n]["images"]["standard_resolution"]["url"])
					url = j["pagination"]["next_url"] #It will return to Instagram Media API's next_url in loop.
				for n in range(0,left):
					jsondata = urllib2.urlopen(url)
					j = json.load(jsondata)
					if download:
						self.downloadPhoto(j["data"][n]["images"]["standard_resolution"]["url"], 20 * (step+1) + n,path,mediaCount)
					urlList.append(j["data"][n]["images"]["standard_resolution"]["url"])
		if not download:
			return urlList

	def downloadPhoto(self , url, pn,path,mediaCount):
		if not os.path.isdir(path):
			os.makedirs(path)
		fileName = url.split('/')[-1].split('?')[0]
		u = urllib2.urlopen(url)
		f = open(path + '/' + fileName, 'wb')
		blockSize = 65536
		while True:
			buffer = u.read(blockSize)
			if not buffer:
				break
			f.write(buffer)
		f.close()
		status = r"[%3.2f%%]" % (pn * 100. / (mediaCount -1))
		print status,
		print "Downloading: #%s" % (pn+1)