import time
import re


def trans_date(v_timestamp):
    """10位时间戳转换为时间字符串/Converting Time Format"""
    timeArray = time.localtime(v_timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def trans_gender(gender_tag):
    """转换性别/Gender"""
    if gender_tag == 1:
        return '男'
    elif gender_tag == 0:
        return '女'
    else:  # -1
        return '未知'


def clean_content(v_text):
    """回答内容数据清洗/Clean the Content"""
    dr = re.compile(r'<[^>]+>', re.S)
    text2 = dr.sub('', v_text)
    return text2
