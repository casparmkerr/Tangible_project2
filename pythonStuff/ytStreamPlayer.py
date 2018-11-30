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

