import requests
import json

def get_random_indices(api_key, count, min_index, max_index):
    raw_data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": api_key,
            "n": count,
            "min": min_index,
            "max": max_index,
            "replacement": True
        },
        'id': 1
    }

    headers = {'Content-type': 'application/json'}
    data = json.dumps(raw_data)

    response = requests.post('https://api.random.org/json-rpc/2/invoke', data=data, headers=headers)
    random_indices = response.json().get('result', {}).get('random', {}).get('data', [])
    return random_indices