import numpy as np
import pandas as pd

region = pd.read_csv('../data/region_code.csv')
#origin = pd.read_csv('../data/daytime_외국인 유동인구_2019년 4분기(10-12월).csv')
origin = pd.read_csv('../data/nighttime_외국인 유동인구_2019년 4분기(10-12월).csv')

atts = list(origin.columns)
base = atts[:3]
pops = atts[3:]
reg_code = {}

data_time = origin.to_dict('records')
data_region = region.to_dict('records')
for reg in data_region:
    reg_code[reg['명칭']] = reg['코드']

result = {atts[0]:[], atts[1]:[], atts[2]:[], 'population':[], 'region_code':[]}

for record in data_time:
    psum = 0.0
    for p in pops:  psum += record[p]
    for b in base:  result[b].append(record[b])
    result['population'].append(psum)
    result['region_code'].append(reg_code[record[atts[2]]])

result_df = pd.DataFrame(result)
#result_df.to_csv('../data/daytime.csv', encoding='utf-8')
result_df.to_csv('../data/nighttime.csv', encoding='utf-8')