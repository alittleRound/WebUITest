# -*- coding:utf-8 -*-
# @Time    : 2022/08/26 08:56
# @Author  : wyt
# @Remark:

import yaml


def get_data(file_path):
    """
    对yaml文件中的数据进行处理
    :param file_path: yaml文件路径
    :return:返回一个列表嵌套元组，一组元组表示一条测试用例的数据
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        test_data = yaml.load(f, Loader=yaml.FullLoader)
        data = []
        for value in test_data.values():
            # print(value)
            case_data = []
            for i in value:
                case_data.append(list(i.values())[0])
                # 取每个test_case中的数据
            data.append(tuple(case_data))
        print(data)
        return data
