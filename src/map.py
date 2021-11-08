import pandas as pd
import folium
import webbrowser
 
state_geo = './data/TL_SCCO_EMD_toWGS84.json'
state_foreign = './data/유동인구_09_제주도장기체류외국인유동인구구성비율.csv'
state_data = pd.read_csv(state_foreign, encoding = 'utf-8')
 
m = folium.Map(location=[33.37, 126.5], tiles="OpenStreetMap", zoom_start=11) # 제주도
'''
# Add the color for the chloropleth:
m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['Code', 'Population'],
 key_on='feature.properties.SIG_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)
folium.LayerControl().add_to(m)
''' 
m.save('foreign_Jeju.html')
webbrowser.open_new("foreign_Jeju.html")