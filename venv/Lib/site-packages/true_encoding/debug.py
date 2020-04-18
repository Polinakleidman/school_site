# coding=utf-8
# authoor:UlionTse

import re


def debug(res):
    if ((res.encoding == 'ISO-8859-1') or (res.encoding is None)):
        if (('charset=gb2312' in res.text) or ('charset=GB2312' in res.text)):
            return 'gb2312'
        elif (('charset=GBK' in res.text) or ('charset=gbk' in res.text)):
            return 'GBK'
        elif (('charset=cp936' in res.text) or ('charset=CP936' in res.text)):
            return 'cp936'
        elif (('charset=utf-8' in res.text) or ('charset=UTF-8' in res.text)):
            return 'utf-8'
        elif 'charset="' in res.text:
            pattern = re.compile('charset="(.*?)"', re.S)
            res.encoding = re.findall(pattern, res.text)[0]
            return res.encoding
    return res.encoding
