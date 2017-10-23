import requests

base_url = "http://api.genius.com"
headers = {'Authorization': 'Bearer t9nQ0cmX9aYZ8Q0eoTmz8BL4jl9WuiGj3A3jyqSV24aP4Bros1sJpUfmkdrTgTG9'}
search_url = base_url + "/search"
song_title = "Capsized"
artist_name = "Andrew Bird"
data = {'q': song_title}
response = requests.get(search_url, data=data, headers=headers)
json = response.json()
song_info = None
for hit in json["response"]["hits"]:
  if hit["result"]["primary_artist"]["name"] == artist_name:
    song_info = hit
    break
if song_info:
  pass
  #now we have the song info and can do what we want