import requests
import pp
def search_shows_by_actor(actor):
  url = f'https://api.tvmaze.com/search/people?q={actor}'
  response = requests.get(url)
  response.raise_for_status()
  data = response.json()
  
  for result in data:
    person = result["person"]
    if person["birthday"] is not None:
      print ("Birthday: " + person["birthday"])
    else:
      print("Birthday is unknown")
    if person ["deathday"] is not None:
      print ("Deathday: " + person['deathday'])
    else:
      print("Still alive")
    if person ["gender"] is not None:
      print ("Gender: " + person["gender"])
    else:
      print ("Gender not known")

  return data
actor = input('Enter actor name: ')
shows = search_shows_by_actor(actor)



"""
if shows:
   print(f'Information about {actor}:')
   for show in shows:
       print(show)
else:
   print('No actor found.')
"""