import requests
from pprint import pprint
sheety_endpoint_url = "https://api.sheety.co/6d8cf0ef3ae94045ba52f1a0104bbddd/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint_url)
        response.status_code
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint_url}/{city['id']}", json=new_data)
            print(response.text)