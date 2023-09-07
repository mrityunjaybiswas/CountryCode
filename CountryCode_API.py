from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

# Define the path to the JSON file
Location = "data.json"

def resultApi(Location):
    try:
        with open(Location, 'r') as fileData:
            result = json.load(fileData)
        return result
    except FileNotFoundError:
        return None
def api_status_check():
    try:
        response = requests.get("https://www.travel-advisory.info/api")

        if response.status_code == 200:
            api_status = {"code": 200, "status": "ok"}
        else:
            api_status = {"code": response.status_code, "status": "error"}

    except requests.exceptions.RequestException as e:
        api_status = {"code": 500, "status": "error", "message": str(e)}

    return api_status
   
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/diag', methods=['GET'])
def diag_check():
    api_status = api_status_check()
    return jsonify({"api_status": api_status})

def dataManupulation(resp, country_name):
    for code, country_data in resp["data"].items():
        if country_data["name"].lower() == country_name.lower():
            return {"country_code": code}
    
    return {"error": "Country name not found"}

@app.route('/convert', methods=['GET'])
#this will convert country name to country code
def convert():
    country_name = request.args.get('country_name', '').strip()
    resp = resultApi(Location)
    
    if resp:
        result = dataManupulation(resp, country_name)
        return jsonify(result)
    else:
        return jsonify({"error": "File not found"})

if __name__ == "__main__":
    app.run(debug=True,host=('0.0.0.0'))
