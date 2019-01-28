#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:30:45 2019

@author: polo
"""
#https://github.com/nikhilkumarsingh/YouTubeAPI-Examples/blob/master/5.Most-Disliked-Channel-Vids.ipynb

from apiclient.errors import HttpError
from oauth2client.tools import argparser
from apiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = 'AIzaSyDb_OgiI9beU0BmuHvlHlNP_5ZuXUSKK8Q'

YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

#req = youtube.search().list(part='snippet', q='avengers', type='video', maxResults=50)
#res = req.execute()
#print (res['items'][0])

vid = '_inj6yoM6fI'

def get_comment_threads(youtube, video_id, comments):
   threads = []
   results = youtube.commentThreads().list(part="snippet", videoId=video_id,
                                           textFormat="plainText").execute()
   print (results)
   #Get the first set of comments
   for item in results["items"]:
       threads.append(item)
       comment = item["snippet"]["topLevelComment"]
       text = comment["snippet"]["textDisplay"]
       comments.append(text)

   #Keep getting comments from the following pages
   while ("nextPageToken" in results):
         results = youtube.commentThreads().list(part="snippet", videoId=video_id, 
         pageToken=results["nextPageToken"],textFormat="plainText",).execute()
         for item in results["items"]:
             threads.append(item)
             comment = item["snippet"]["topLevelComment"]
             text = comment["snippet"]["textDisplay"]
             comments.append(text)

   print ("Total threads: %d" % len(threads))

   return threads,results

comments = []
threads,reults = get_comment_threads(youtube, vid, comments)