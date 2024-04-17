from dotenv import load_dotenv
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
clientID = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")
scope = 'playlist-modify-public' #scope in which program modifies user's stuff
username = 'Test Account'#input("Display name:")
realname = '31ezix7o5ij2irsasjoo5ev5vsva'#input("Username:") #user id
token = SpotifyOAuth(redirect_uri=redirect_uri,client_id=clientID,client_secret=client_secret,scope=scope,username=username)
spotifyobj = spotipy.Spotify(auth_manager=token)
def callplaylist(creator,id,start = 0):
    playlist = spotifyobj.user_playlist_tracks(creator,id,offset=start)['items']
    return playlist
baseplaylistname = input("Playlist to sort:")
playlistname = input("Playlist to add(new or existing):")
artist = input("Artist:")
startpt = input("Start:")
playlists = spotifyobj.user_playlists(user=realname)
playlistnames = []
for i in range(len(playlists)):
    playlistnames.append(playlists['items'][i]['name'])
def get_id(name):
    result = ''
    for i in range(len(playlists)):
        if playlists['items'][i]['name'] == name:
            id = playlists['items'][i]['id']
            result = id
    return result
baseplaylist_id = get_id(baseplaylistname)
baseplaylist = callplaylist(username,baseplaylist_id,startpt)
myplaylist_id = ''
if not(playlistname in playlistnames):
    spotifyobj.user_playlist_create(user=realname,name=playlistname,public=True)
else:
   myplaylist_id = get_id(playlistname)
myplaylist = callplaylist(username,myplaylist_id)
def addsongs(playlist):
    songstoadd = []
    for i in range(len(playlist)):
        if playlist[i]['track']['artists'][0]['name'] == artist and not(playlist[i] in myplaylist):
            songstoadd += [playlist[i]['track']['uri']]
    if len(songstoadd) > 0:
        spotifyobj.user_playlist_add_tracks(user=username,playlist_id=myplaylist_id,tracks=songstoadd)
        spotifyobj.user_playlist_remove_all_occurrences_of_tracks(user=username,playlist_id=baseplaylist_id,tracks=songstoadd)
        #spotifyobj.user_playlist_add_tracks(user=username,playlist_id=playlists['items'][0]['id'],tracks=songstoadd)
        print("Tracks added.")
    else:
        print("No songs to add.")
addsongs(baseplaylist)
#animeplaylist = callplaylist(username,'5ZxILz3hhHogN2u5PJUQJf',0)
# animeplaylist2 = callplaylist('Jimmy Bobby Boy','5ZxILz3hhHogN2u5PJUQJf',101)
# animeplaylist3 = callplaylist('Jimmy Bobby Boy','5ZxILz3hhHogN2u5PJUQJf',201)
# animeplaylist4 = callplaylist('Jimmy Bobby Boy','5ZxILz3hhHogN2u5PJUQJf',301)
#print(animeplaylist2[50]['track']['artists'][0]['name'])
#addsongs(animeplaylist)
# addsongs(animeplaylist2)
# addsongs(animeplaylist3)