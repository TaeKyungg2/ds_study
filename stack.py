class Stack:
    def __init__(self,len):
        self.len=len

    def push(self):
        pass
    def helpKr(self):
        print("""스택 자료구조를 다루는 클래스입니다. 
스택은, 가장 최근에 들어온 아이템을 내보내는 형식입니다.
객체.push(값) : 값 넣기
객체.pop() : 최근 값 빼기
객체.allPrint() : 모든 값 출력""")