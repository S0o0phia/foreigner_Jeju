import json
import folium
from folium import features
import pandas as pd

move = pd.read_csv('../data/daytime.csv')

time = move['time_range']
nation = move['nationality']
region = move['emd_name']
pop = move['population']
region_code = move['region_code']

region_mean = move.pivot_table(index='emd_name', values = ['region_code', 'population'], aggfunc = 'mean')
data = region_mean.reset_index().reindex(columns=['region_code', 'population'])

m = folium.Map(location = [33.431441, 126.5], zoom_start = 10 )

with open('../data/TL_SCCO_EMD_WGS84.json', 'r', encoding = 'utf-8') as file:
  state_geo = json.loads(file.read())

for i in range(0, len(state_geo['features'])):
  state_geo['features'][i]['properties']['EMD_CD'] = int(state_geo['features'][i]['properties']['EMD_CD'])

m.choropleth(
    geo_data=state_geo,
    name='Floating population',
    data=data,
    columns=['region_code', 'population'],
    key_on='feature.properties.EMD_CD',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.3,
    color = 'gray',
    legend_name = 'Population(/60)'
)
folium.LayerControl().add_to(m)

m.save('../foreign_jeju.html')