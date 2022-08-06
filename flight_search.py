import requests

endpoint_url = "https://tequila-api.kiwi.com"
flight_api_key = "ufBPxQZJlItcqO_Jg5GhJbNDHgQUz0RB"

class FlightSearch:
    def __init__(self):
        self.city_code = ""

    def get_destination_code(self, city_name):
        headers = {"apikey": flight_api_key}
        query= {"term": city_name, "location_types": "city"}
        self.city_code = requests.get(url=f"{endpoint_url}/locations/query", params=query, headers=headers)
        results = self.city_code.json()["locations"]
        code = results[0]["code"]
        return code
