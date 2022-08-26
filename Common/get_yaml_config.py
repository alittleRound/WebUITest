# -*- coding:utf-8 -*-
# @Time    : 2022/08/26 08:54
# @Author  : wyt
# @Remark:

import yaml


def get_url(file_path):
    """
    处理yaml配置文件
    :param file_path:
    :return:返回拼接好的url
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        config_data = yaml.load(f, Loader=yaml.FullLoader)
        url = 'http://' + str(config_data['ip']) + ':' + str(config_data['port'])
        return url