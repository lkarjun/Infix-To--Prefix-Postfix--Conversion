from typing import List, Dict

class InfixTOPostfix:
    stack: List = []
    prefix: str = ''
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
            while True:
                lastElement: str = self.peek()
                if lastElement != '(':
                    self.prefix += lastElement
                    self.pop()
                else:
                    self.pop()
                    break
        
        elif s == '(': self.push(s)
        else:

            lastElement: str = self.peek()
            
            if lastElement == '(':
                self.push(s)
            
            elif self.Operators[lastElement] == self.Operators[s]:
                self.prefix += lastElement
                self.pop()
                self.push(s)

            elif self.Operators[s] < self.Operators[lastElement]:
                self.prefix += lastElement
                self.pop()
                if self.peek() != '(' or ')':
                    self.stackOperation(s)

            else:
                self.push(s)
        

    def push(self, s: str): self.stack.append(s)

    def pop(self): self.stack.pop()

    def peek(self) -> str: return False if len(self.stack) == 0 else self.stack[-1]

    def displayPrefix(self) -> str: return self.prefix

    def displayStack(self) -> List: return self.stack if len(self.stack) !=0 else 'zero elements'



string = 'K+L-M*N(O^P)*W/U/V*T+Q'
c = InfixTOPostfix(string)
c.main()
ans = c.displayPrefix()

assert ans == 'KL+MNOP^*W*U/V/T*-Q+'

print(f"\nRegular form = {string}\nInfix form = {ans}")