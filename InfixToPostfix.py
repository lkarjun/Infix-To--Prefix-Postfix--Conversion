from typing import List, Dict

class InfixTOPostfix:
    stack: List = []
    prefix: str = []
    Operator: Dict = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3, '(': None, ')': None}