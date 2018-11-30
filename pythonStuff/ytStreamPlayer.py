import youtube_dl
import pafy
import vlc


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

#PAFY_BACKEND = "internal"

audio = pafy.new(url)
best = audio.getbestaudio()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()


"""
solved that pip install click didn’t work: https://stackoverflow.com/questions/49768770/not-able-to-install-python-packages-ssl-tlsv1-alert-protocol-version/49769015#49769015

youtube-dl: https://github.com/rg3/youtube-dl/blob/master/README.md

pafy documentation: https://pythonhosted.org/Pafy/#pafy-objects-and-stream-objects

https://stackoverflow.com/questions/49354232/stream-youtube-audio-from-python-using-url-without-downloading-python

"""