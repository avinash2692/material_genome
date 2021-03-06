import json
import requests

data = {
    'criteria': {
        'elements': {'$in': ['Li', 'Na', 'K'], '$all': ['O']},
        'nelements': 2,
    },
    'properties': [
        'formula',
        'formation_energy_per_atom',
    ]
}
r = requests.post('https://materialsproject.org/rest/v2/query',
                 headers={'X-API-KEY': '<YOUR-API-KEY>'},
                 data={k: json.dumps(v) for k,v in data.iteritems()})
response_content = r.json() # a dict