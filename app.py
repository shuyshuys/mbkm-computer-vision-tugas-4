from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests
import xmltodict
import json


def convert_xml_to_json(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/xml,text/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = requests.get(url, headers=headers)
    # response = requests.get(url)
    # print("Status code:", response.status_code)
    # print("Response content:", response.content)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    json_data = json.dumps(data_dict)
    return json_data

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

@app.route('/api/prakiraan-cuaca/<region>', methods=['GET'])
@cross_origin()
def get_data(region):
    url = f'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-{region}.xml'
    data = convert_xml_to_json(url)
    data_dict = json.loads(data)    
    return jsonify(data_dict), 200

@app.route('/api/data/jakarta', methods=['GET'])
def get_data_jakarta():
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DKIJakarta.xml'
    data = convert_xml_to_json(url)
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DKIJakarta.xml'

    data_dict = json.loads(data)    
    return jsonify(data_dict), 200


@app.route('/api/data/gorontalo', methods=['GET'])
def get_data_gorontalo():
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-Gorontalo.xml'
    data = convert_xml_to_json(url)
    data_dict = json.loads(data)    
    return jsonify(data_dict), 200

@app.route('/api/data/jawa-barat', methods=['GET'])
def get_data_jawabarat():
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-JawaBarat.xml'
    data = convert_xml_to_json(url)
    data_dict = json.loads(data)    
    return jsonify(data_dict), 200

@app.route('/api/data/jawa-timur', methods=['GET'])
def get_data_jawatimur():
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-JawaTimur.xml'
    data = convert_xml_to_json(url)
    data_dict = json.loads(data)    
    return jsonify(data_dict), 200

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()  # Get the JSON data from the request
    # Process the data here
    return jsonify({"message": f"Data received: {data}!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)