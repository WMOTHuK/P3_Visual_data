import json

from pygal_maps_world.maps import World

from country_codes import get_country_code

#Создаём карту
wm = World()
wm.title = 'World population'

# Список заполняется данными.
filename = 'json_data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # Вывод населения каждой страны за 2010 год.
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                wm.add(country_name, {code: population})

            else:
                print('ERROR - ' + country_name)

wm.render_to_file('world_population_multicolor.svg')



