import json
import os

def get_json_data():
    json_data = []
    with open("links.json")as f:
        url_data = json.load(f)
        
    json_data.append({
            "url_data" : url_data
        })
    
    return json_data