# -*- coding:utf-8 -*-
'''

Created on 2021/12/15
@author: WHT
'''

import unittest
import datafactory.disease.ncov as ncov


class Test(unittest.TestCase):

    def set_data(self):
        self.disp = 10

    def test_get_ncov_tencent_rt(self):
        self.set_data()
        print('get ncov tencent rt................\n')
        ncov_df = ncov.get_ncov_tencent_rt()
        print('\nnums=%d' % len(ncov_df))
        print(ncov_df[:self.disp])
        ncov_df.to_csv('ncov.csv')



    # def test_get_nav_close(self):
    #     self.set_data()
    #     type2 = ['all', 'fbqy', 'fbzq']
    #     qy_t3 = ['all', 'ct', 'cx']
    #     zq_t3 = ['all', 'wj', 'jj', 'cz']
    #
    #     print('\nget nav closed................\n')
    #     fund_df = None
    #     for item in type2:
    #         if item == 'fbqy':
    #             for t3i in qy_t3:
    #                 print('\n=============\nget %s-%s nav\n=============' %
    #                       (item, t3i))
    #                 fund_df = nav.get_nav_close(item, t3i)
    #                 print('\nnums=%d' % len(fund_df))
    #                 print(fund_df[:self.disp])
    #         elif item == 'fbzq':
    #             for t3i in zq_t3:
    #                 print('\n=============\nget %s-%s nav\n=============' %
    #                       (item, t3i))
    #                 fund_df = nav.get_nav_close(item, t3i)
    #                 print('\nnums=%d' % len(fund_df))
    #                 print(fund_df[:self.disp])
    #         else:
    #             print('\n=============\nget %s nav\n=============' % item)
    #             fund_df = nav.get_nav_close(item)
    #             print('\nnums=%d' % len(fund_df))
    #             print(fund_df[:self.disp])
    #
    # def test_get_nav_grading(self):
    #     self.set_data()
    #     t2 = ['all', 'fjgs', 'fjgg']
    #     t3 = {'all': '0', 'wjzq': '13', 'gp': '14',
    #           'zs': '15', 'czzq': '16', 'jjzq': '17'}
    #
    #     print('\nget nav grading................\n')
    #     fund_df = None
    #     for item in t2:
    #         if item == 'all':
    #             print('\n=============\nget %s nav\n=============' % item)
    #             fund_df = nav.get_nav_grading(item)
    #             print('\nnums=%d' % len(fund_df))
    #             print(fund_df[:self.disp])
    #         else:
    #             for t3i in t3.keys():
    #                 print('\n=============\nget %s-%s nav\n=============' %
    #                       (item, t3i))
    #                 fund_df = nav.get_nav_grading(item, t3i)
    #                 print('\nnums=%d' % len(fund_df))
    #                 print(fund_df[:self.disp])
    #
    # def test_nav_history(self):
    #     self.set_data()
    #     lst = ['164905', '161005', '380007', '000733', '159920', '164902',
    #            '184721', '165519', '164302', '519749', '150275', '150305',
    #            '150248']
    #     for _, item in enumerate(lst):
    #         print('\n=============\nget %s nav\n=============' % item)
    #         fund_df = nav.get_nav_history(item, self.start, self.end)
    #         if fund_df is not None:
    #             print('\nnums=%d' % len(fund_df))
    #             print(fund_df[:self.disp])
    #
    # def test_get_fund_info(self):
    #     self.set_data()
    #     lst = ['164905', '161005', '380007', '000733', '159920', '164902',
    #            '184721', '165519', '164302', '519749', '150275', '150305',
    #            '150248']
    #     for item in lst:
    #         print('\n=============\nget %s nav\n=============' % item)
    #         fund_df = nav.get_fund_info(item)
    #         if fund_df is not None:
    #             print('%s fund info' % item)
    #             print(fund_df)

if __name__ == '__main__':
    unittest.main()
