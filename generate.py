import json
import random


def get_random_quote():
    with open('data.json') as data_file:
        data = json.load(data_file)
        num = random.randint(1, len(data))
        for i in data:
            if i["id"] == num:
                print("Quote: " + i["quote"])
                print("Author: " + i["author"])

get_random_quote()
