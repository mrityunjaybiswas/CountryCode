import json
from flask import Flask

# Define the path to the JSON file
Location = "C:\\Users\\mrity\OneDrive\Desktop\data.json"
app = Flask(__name__)
def resultApi(Location):
    try:
        with open(Location, 'r') as fileData:
            result = json.load(fileData)
        return result
    except FileNotFoundError:
        print(f"File '{Location}' not found.")
        return None

def countryCode(resp):
    while True:
        country_code = input("Enter Country Code (or type 'EXIT' to quit): ").strip().upper()
        
        if country_code == 'EXIT':
            break  # Exit the loop if the user types 'EXIT'
        
        if country_code in resp["data"]:
            country_name = resp["data"][country_code]["name"]
            print("The country with code ",country_code," is ",country_name)
        else:
            print("Sorry, the country code was not found in the data.")

if __name__ == "__main__":
    resp = resultApi(Location)
    
    if resp:
        countryCode(resp)
