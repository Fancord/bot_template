from dotenv import dotenv_values

config = dotenv_values(".env")

API_TOKEN = config["API_TOKEN"]

print(type(API_TOKEN))
