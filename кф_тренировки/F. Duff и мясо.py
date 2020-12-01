# https://codeforces.com/group/XWOeQO4RLM/contest/206799/problem/F
days=int(input())
'''for i in range(days):
	kolvo,cost=list(map(int,input().split()))'''
from collections import namedtuple
from functools import lru_cache

Item = namedtuple('Item', 'value weight')
print(Item)