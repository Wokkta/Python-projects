import I. A и B и ошибки компиляции as tfile
import unittest
from random import randint
 class TestCase(unittest.TestCase):
 	def test_first(self):
 		massive=[randint(1,1000) for m in range(10)]
 		massive_m_one=massive
 		massive_m_one.remove(randint(0,len(massive)-1))
 		massive_m_two=massive_m_one
 		massive_m_two.remove(randint(0,len(massive_m_one)-1))
 		tested_o=find_deb(10,massive_m_one,massive)
 		tested_t=find_deb(9,)