import requests


def fetch_data(option, count):
    url = f"http://127.0.0.1:5000/api/{option}"

    try:
        response = requests.get(url, params={"limit": count}, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data.get("results", [])

    except requests.RequestException as error:
        print(f"Error downloading data: {error}")
        return None


count = int(input("How many Star Wars characters do you want? "))
result = fetch_data("people", count)

if result:
    for item in result:
        print(f"{item.get('name')} - {item.get('race')}")
else:
    print("Unable to download data")