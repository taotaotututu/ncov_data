# -*- coding:utf-8 -*-

"""
#  Created on 2021/12/14
#  @author: WHT
#  @group : datafactory
#  @contact: whtsf@foxmail.com
"""


VERSION = '0.0.1'
P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}
# FORMAT = lambda x: '%.2f' % x
# FORMAT4 = lambda x: '%.4f' % x
DOMAINS = {'tencent': 'view.inews.qq.com'
           }


NCOV_DEFAULT_PAGE = 1

##########################################################################
# 疫情数据列名

# TENCENT_NCOV_CHINA_RT_COLUMNS = ['total_confirm', 'total_heal', 'total_dead', 'total_nowConfirm',  'total_suspect',
#                                  'total_nowSevere', 'total_importedCase', 'total_noInfect', 'total_localConfirm',
#                                  'total_noInfectH5', 'total_localConfirmH5', 'total_local_acc_confirm', 'add_confirm',
#                                  'add_heal', 'add_dead', 'add_nowConfirm', 'add_suspect', 'add_nowSevere', 'add_importedCase',
#                                  'add_noInfect', 'add_localConfirm', 'add_noInfectH5', 'add_localConfirmH5']

TENCENT_NCOV_AREA_RT_COLUMNS = ['lastUpdateTime', 'area', 'today_confirm', 'today_confirmCuts', 'today_isUpdated',
                                'today_wzz_add', 'total_nowConfirm', 'total_confirm', 'total_suspect', 'total_dead',
                                'total_deadRate', 'total_heal', 'total_healRate', 'grade', 'total_wzz']

# NAV_HIS_JJJZ = ['fbrq', 'jjjz', 'ljjz']
# NAV_HIS_NHSY = ['fbrq', 'nhsyl', 'dwsy']
#
# FUND_INFO_COLS = ['symbol', 'jjqc', 'jjjc', 'clrq', 'ssrq', 'xcr', 'ssdd',
#                   'Type1Name', 'Type2Name', 'Type3Name', 'jjgm', 'jjfe',
#                   'jjltfe', 'jjferq', 'quarter', 'glr', 'tgr']
#
#
# NAV_CLOSE_COLUMNS = ['symbol', 'sname', 'per_nav', 'total_nav', 'nav_rate',
#                      'discount_rate', 'nav_date', 'start_date', 'end_date',
#                      'fund_manager', 'jjlx', 'jjzfe']
#
#
# NAV_GRADING_COLUMNS = ['symbol', 'sname', 'per_nav', 'total_nav', 'nav_rate',
#                        'discount_rate', 'nav_date', 'start_date', 'end_date',
#                        'fund_manager', 'jjlx', 'jjzfe']
#
#
# NAV_COLUMNS = {'open': NAV_OPEN_COLUMNS,
#                'close': NAV_CLOSE_COLUMNS, 'grading': NAV_GRADING_COLUMNS}


##########################################################################
# 数据源URL

TENCENT_NCOV_RT_URL = '%s%s/g2/getOnsInfo?name=disease_h5'
TENCENT_NCOV_HISTORY_URL = '%s%s/g2/getOnsInfo?name=disease_other'

# SINA_NAV_HISTROY_COUNT_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=%s&datefrom=%s&dateto=%s'
# SINA_NAV_HISTROY_DATA_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=%s&datefrom=%s&dateto=%s&num=%s'
#
# SINA_NAV_HISTROY_COUNT_CUR_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNavcur?symbol=%s&datefrom=%s&dateto=%s'
# SINA_NAV_HISTROY_DATA_CUR_URL = '%s%s/fundInfo/api/openapi.php/CaihuiFundInfoService.getNavcur?symbol=%s&datefrom=%s&dateto=%s&num=%s'
#
# SINA_DATA_DETAIL_URL = '%s%s/quotes_service/api/%s/Market_Center.getHQNodeData?page=1&num=400&sort=symbol&asc=1&node=%s&symbol=&_s_r_a=page'
#
# SINA_FUND_INFO_URL = '%s%s/fundInfo/api/openapi.php/FundPageInfoService.tabjjgk?symbol=%s&format=json'

##########################################################################
DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'
DATA_ROWS_TIPS = '%s rows data found.Please wait for a moment.'
DATA_INPUT_ERROR_MSG = 'date input error.'
NETWORK_URL_ERROR_MSG = '获取失败，请检查网络和URL'
# DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
# DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
# TOP_PARAS_MSG = 'top有误，请输入整数或all.'
# LHB_MSG = '周期输入有误，请输入数字5、10、30或60'
#
# OFT_MSG = u'开放型基金类型输入有误，请输入all、equity、mix、bond、monetary、qdii'

# DICT_NAV_EQUITY = {
#     'fbrq': 'date',
#     'jjjz': 'value',
#     'ljjz': 'total',
#     'change': 'change'
# }
#
# DICT_NAV_MONETARY = {
#     'fbrq': 'date',
#     'nhsyl': 'value',
#     'dwsy': 'total',
#     'change': 'change'
# }

import sys
PY3 = (sys.version_info[0] >= 3)


def _write_head():
    sys.stdout.write(DATA_GETTING_TIPS)
    sys.stdout.flush()


def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()


def _write_tips(tip):
    sys.stdout.write(DATA_ROWS_TIPS % tip)
    sys.stdout.flush()


def _write_msg(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


# def _check_nav_oft_input(found_type):
#     if found_type not in NAV_OPEN_KEY.keys():
#         raise TypeError(OFT_MSG)
#     else:
#         return True
#
#
# def _check_input(year, quarter):
#     if isinstance(year, str) or year < 1989:
#         raise TypeError(DATE_CHK_MSG)
#     elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
#         raise TypeError(DATE_CHK_Q_MSG)
#     else:
#         return True