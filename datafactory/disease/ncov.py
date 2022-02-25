# -*- coding:utf-8 -*-

"""
获取疫情数据接口
#  Created on 2021/12/15
#  @author: WHT
#  @group : datafactory
#  @contact: whtsf@foxmail.com
"""

from __future__ import division
import time
import json
import re
import pandas as pd
import numpy as np
from datafactory.disease import cons as ct
from datafactory.util import dateu as du
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib3 import urlopen, Request            # 王



def get_ncov_tencent_rt():
    '''
    获取腾讯疫情实时数据
    '''

    listed_columns = ct.TENCENT_NCOV_AREA_RT_COLUMNS
    request = ct.TENCENT_NCOV_RT_URL % (
        ct.P_TYPE['http'], ct.DOMAINS['tencent'])
    text = urlopen(request, timeout=10).read()
    text = text.decode('utf-8')
    org_js = json.loads(text)

    status_code = int(org_js['ret'])
    if status_code != 0:
        status = str(org_js['ret'])
        raise ValueError(status)
    data = org_js['data']   # str(org_js['data']).replace('\\','')
    data = data.replace('true','1')
    data = data.replace('false','0')
    data = eval(data)
    # print(type(data))

    # print(data['areaTree'])
    dict_data = list()
    for row in data['areaTree']:
        row_dict = {'lastUpdateTime':data['lastUpdateTime']}
        if row['name'] == '中国':
            row_dict['area'] = '中国'
            for i in row['today']:
                row_dict['today_' + i] = int(row['today'][i])
            row_dict['today_confirmCuts', 'today_wzz_add'] = {-1, -1}
            for i, field in enumerate(listed_columns[6:]):
                if field in ['total_deadRate', 'total_healRate']:
                    row_dict[field] = float(row['total'][field[6:]])
                elif field in ['grade']:
                    row_dict[field] = ''
                else:
                    row_dict[field] = int(row['total'][field[6:]])
        dict_data.append(row_dict)

    # temp_data = data['areaTree'][0]
    # print(type(temp_data))
    area_data = data['areaTree'][0]['children']
    for row in area_data:
        row_dict = {'lastUpdateTime': data['lastUpdateTime']}
        row_dict['area'] = row['name']
        for i, field in enumerate(listed_columns[2:5]):
            row_dict[field] = int(row['today'][field[6:]])
        for i, field in enumerate(listed_columns[6:]):
            if field in ['total_deadRate', 'total_healRate']:
                row_dict[field] = float(row['total'][field[6:]])
            elif field in ['grade']:
                row_dict[field] = ''
            else:
                row_dict[field] = int(row['total'][field[6:]])
        dict_data.append(row_dict)
        if 'children' in row.keys():
            children_data = row['children']
            for row in children_data:
                row_dict = {'lastUpdateTime': data['lastUpdateTime']}
                row_dict['area'] = row['name']
                for i, field in enumerate(listed_columns[2:5]):
                    row_dict[field] = int(row['today'][field[6:]])
                for i, field in enumerate(listed_columns[6:]):
                    if field in ['total_deadRate', 'total_healRate']:
                        row_dict[field] = float(row['total'][field[6:]])
                    elif field in ['grade']:
                        if 'grade' in row['total'].keys():
                            row_dict[field] = str(row['total']['grade'])
                    else:
                        row_dict[field] = int(row['total'][field[6:]])
                dict_data.append(row_dict)

    # result = []
    # for i in data['areaTree']:
    #     t = {}
    #     for j in list(i.keys()):
    #         if isinstance(i[j],dict):
    #             t1 = {}
    #             for k in list([j].keys()):
    #                 if isinstance(i[j][k],dict):
    #                     continue
    #                 else:
    #                     t1[j+'_'+k] = i[j][k]
    #             t.update(t1)
    #         else:
    #             t.update({j:i[j]})
    #     result.append(t)
    ncov_df = pd.DataFrame(dict_data,columns=ct.TENCENT_NCOV_AREA_RT_COLUMNS)


    # ncov_df = pd.DataFrame(data)

    #dict_data = list()
    # for row in data[1:]:
    #     row_dict = {'lastUpdateTime': row[0].value}
    #     for i, field in enumerate(ct.TENCENT_NCOV_RT_COLUMNS[1:]):
    #         dict_data.append(row)
    # ncov_df = pd.DataFrame(dict_data, columns=ct.TENCENT_NCOV_RT_COLUMNS, index=[0])
    return ncov_df