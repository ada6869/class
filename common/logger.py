# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 15:49 
# @Author : Ada
# @File : logger.py

import logging
from API.API_8.common import contants

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"

    formatter = logging.Formatter(fmt=fmt)

    console_handle = logging.StreamHandler()#控制台
    #把日志级别放到配置文件里面配置--优化
    console_handle.setLevel("DEBUG")
    console_handle.setFormatter(formatter)

    file_handle = logging.FileHandler(contants.log_dir + '/case.log') #文件
    # 把日志级别放到配置文件里面配置
    file_handle.setLevel('INFO')
    file_handle.setFormatter(formatter)

    logger.addHandler(console_handle)
    logger.addHandler(file_handle)
    return logger
logger = get_logger('case')
logger.info("测试开始了")
logger.error("测试报错")
logger.debug("测试数据")
logger.info("测试结束")