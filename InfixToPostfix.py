from typing import List, Dict

class InfixTOPostfix:
    stack: List = []
    prefix: str = []
    Operators: Dict = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3, '(': None, ')': None}

    def __init__(self, value: str) -> None:
        self.strings: str = value

    def main(self) -> None:
        for i in self.strings:
            if i not in self.Operators: self.prefix += i
            else: self.stackOperation(i)
        
        if len(self.stack) != 0:
            for i in self.stack[::-1]: self.prefix +=i
    
    def stackOperation(self, s: str) -> str:
        if len(self.stack) == 0:
            self.push(s)

        elif s == ')':
            pass