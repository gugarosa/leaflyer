import json

N_FILES = 10

data = {}
data['strains'] = []

for i in range(N_FILES):
    with open(f'strain_data_{i+1}.json', 'r') as f:
        data['strains'] += json.load(f)['strains']
    f.close()
    
with open(f'strain_data.json', 'w') as f:
    json.dump(data, f)
