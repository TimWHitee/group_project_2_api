import requests
import json
from guardian_api_key import theguardian_key


base_url = 'https://content.guardianapis.com/search'

params = {
    'q': 'APPL',
    'from-date': '2026-01-01',
    'to-date': '2026-04-01',
    'order-by': 'relevance',
    'show-blocks': 'body',
    'api-key': theguardian_key
}

response = requests.get(base_url, params=params).json()



with open('pretty_json.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, indent=4)

print(response)