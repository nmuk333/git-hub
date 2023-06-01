import requests

def search_shows_by_actor(actor):
  url = f'https://api.tvmaze.com/search/people?q={actor}'
  response = requests.get(url)
  response.raise_for_status()
  data = response.json()
  
  for result in data:
    person = result["person"]
    print (person["deathday"])
    print (person["birthday"])
    print ()
    
  
  return data

# Example usage
actor = input('Enter actor name: ')
shows = search_shows_by_actor(actor)

if shows:
   print(f'Information about {actor}:')
   for show in shows:
       print(show)
else:
   print('No actor found.')
