import requests, json, logging

logging.basicConfig(level=logging.INFO)

def get_random_indices(api_key, count, min_index, max_index):
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer.")
    if min_index >= max_index:
        raise ValueError("Min index must be less than max index")

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

    try:
        response = requests.post('https://api.random.org/json-rpc/2/invoke', data=data, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error(f'HTTP Error: {errh}')
        return []
    except requests.exceptions.ConnectionError as errc:
        logging.error(f'Error ConnectiongL {errc}')
        return []
    except requests.exceptions.Timeout as errt:
        logging.error(f'Timeout Error: {errt}')
        return []
    except requests.exceptions.RequestException as err:
        logging.error(f'Something unexpected happened: {err}')
        return []


    try:
        random_indices = response.json().get('result', {}).get('random', {}).get('data', [])
    except Exception as e:
        logging.error(f'Failed to parse JSON: {e}')
        return []
    
    return random_indices