import json
import os
import os.path as path

template_folder = 'data/seasons/functions/templates'
output_folder = 'data/seasons/functions/generated'

tag_file ='data/seasons/tags/blocks/snowable_plants.json'

with open(tag_file) as file:
    data = json.load(file)
    values = data['values']

for filename in os.listdir(template_folder):
    template_path = path.join(template_folder, filename)
    if not path.isfile(template_path):
        continue

    with open(template_path) as file:
        template = file.readline()
    
    with open(path.join(output_folder, filename), 'w') as file:
        for value in values:
            file.write(template.replace('$plant', value))

