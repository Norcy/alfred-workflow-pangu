#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pangu
import pyperclip
import sys
from enum import Enum, unique

@unique
class QueryMode(Enum):
    Paste = 0		# 格式化剪切板文字
    Selection = 1	# 格式化选中文字


mode = QueryMode.Selection
query = ""

if sys.argv[1]:
	mode = QueryMode.Selection
	query = sys.argv[1]
else:
	mode = QueryMode.Paste
	query = pyperclip.paste()

ret = pangu.spacing_text(query)

if mode == QueryMode.Selection:
	print(ret, end='') # 默认输出不要换行
else:
	pyperclip.copy(ret)