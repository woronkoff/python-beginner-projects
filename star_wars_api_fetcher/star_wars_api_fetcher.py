import requests

def fetch_data(option, count):
  url = f"https://swapi.dev/api/{option}/"
  result = []
  while len(result) < count:
    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
      result.extend(data["results"])
      print(f"Successfully fetched {len(result)} entities!")
      url = data["next"]
    except requests.HTTPError as e:
      print(f"Error Message. {e}")
      return None
    if url == None:
      break
  return result[:count]

count = int(input("How many characters you want? "))
result = fetch_data("people", count)

if result:
  for item in result:
    print(item.get("name"))
else:
  print("Unable to download data")

