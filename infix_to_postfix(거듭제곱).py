class fix:
    def infix_to_postfix(self, ex):
        self.stack = [] #연산자 저장(임시 저장공간)
        self.output = [] #최종 결과 담는 리스트

        ex = self.tokenization(ex) #토큰단위로 자름
        for token in ex:
            if self.is_operand(token): #숫자면 바로 출력 리스트에
                self.output.append(token)
            elif token == '(': #괄호는 스택에 
                self.stack.append(token)
            elif token == ')': #스택에서 (가 나올 때까지 pop해서 출력에 추가 -> 괄호 안의 연산자를 후위표기식으로 변환하는 과정
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()
            else: #while self.stack -> 스택이 빌때까지 반복
                while self.stack and ((self.precedence(self.stack[-1]) > self.precedence(token)) #스택의 top 연산자가 현재 연산자보다 우선순위가 높으면 pop
                                      or (self.precedence(self.stack[-1]) == self.precedence(token) and token != '^')): #연산자 우선순위가 같고 ^가 아닐때
                    self.output.append(self.stack.pop()) #스택에서 연산자를 꺼내서 출력 리스트에 추가
                self.stack.append(token) #스택이 비면 연산자를 스택에 넣음

        while self.stack:
            self.output.append(self.stack.pop())
        return ' '.join(self.output)

    def precedence(self, op): #우선순위 정의
        if op in ('+', '-'): #op에 +나 -가 포함되어있으면 -> in연산자
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0
    
    def tokenization(self, ex):
        return ex.split() #공백기준 분리
    def is_operand(self, token):
        return token.isdigit() #숫자인지 판별
        

obj = fix() #객체 생성
result = obj.infix_to_postfix('2 ^ 3 ^ 2') 
print(result)