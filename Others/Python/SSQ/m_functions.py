import os
import tabulate

import itertools
import time
from tqdm import tqdm
import requests

def print_lottery_data(row=30, column=9):
    """打印往期开奖数据
    Args:
        row (int, optional): _description_. Defaults to 30.
        column (int, optional): _description_. Defaults to 9.

    Returns:
        _type_: _description_
    """

    # 读取数据(开奖信息)
    with open(os.getcwd() + '\\ssq_asc.txt', 'r') as f:
        data_lottery = []
        for line in f:
            fields = line.strip().split()[:column]
            data_lottery.append(fields)

    data_lottery = data_lottery[-row:]

    # 打印开奖数据
    headers = ('期号', '开奖日期', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '蓝球')
    table = tabulate(data_lottery, headers=headers, tablefmt='psql')
    print(table)

    # # 格式化开奖数据
    # for line in data_lottery:
    #     new_line = line[:2]
    #     for i in range(1,34):
    #         if i < 10:

    #             new_line.append("")
    #         else:
    #             new_line.append('')

    # print(new_line)

    # # 整理数据格式为二维List 红球1,红球2,红球3,红球4,红球5,红球6,蓝球
    # tmp = []
    # [tmp.append(line[2:]) for line in data_lottery]

    # # 转换数据格式为一维列表
    # od_data = [element for sublist in tmp for element in sublist]
    # od_data = Counter(od_data)
    # print(od_data)

    # # 转换数据格式为一维列表
    # # od_data = [element for sublist in data for element in sublist]
    # # od_data = Counter(data)
    
    
def requests_data():
    """请求更新数据并保存到本地
    """
    url = 'http://data.17500.cn/ssq_asc.txt'
    path = os.getcwd() + '\\ssq_asc.txt'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
    }

    current_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                 time.localtime(time.time()))

    rs = requests.get(url=url, headers=headers)
    if rs.status_code == 200:
        with open(path, 'wb') as f:
            f.write(rs.content)
            print(f'[info] {current_time} 数据更新成功...\n')
    else:
        print(f'[error] {current_time} 数据更新失败...\n')
    

def get_all_combos():
    """获取所有排列组合"""
    
    
    # iterable: 可迭代的对象, 在手动更新时不需要进行设置
    # desc: 字符串, 左边进度条描述文字
    # total: 总的项目数
    # leave: bool值, 迭代完成后是否保留进度条
    # file: 输出指向位置, 默认是终端, 一般不需要设置
    # ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
    # unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
    # unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s

    # 生成1到34的数字列表
    numbers = list(range(1, 34))

    # 计算排列组合

    combos = itertools.combinations(numbers, 6)
    # 1-33 的数字中，任取6个数字进行排列组合数, 将计算记过保存到txt文本中
    with tqdm(total=1107569, desc='生成排列组合:', leave=True, ncols=100) as pbar:
        for combo in combos:
            with open('all_combos.txt', 'a') as f:
                f.write(','.join(str(num) for num in combo) + '\n')
            pbar.update(1)

    print('生成排列组合完成!')
