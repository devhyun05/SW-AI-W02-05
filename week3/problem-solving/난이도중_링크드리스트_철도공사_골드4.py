# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

class Node:
    def __init__(self, data, next, prev):
        self.data = data 
        self.next = next 
        self.prev = prev 

class LinkedList:
    def __init__(self):
        self.head = None 
        self.count = 0 
    
    # 새로운 노드를 추가하는 함수 
    def append(self, data):
        # 처음 생성하는 거라면 
        if self.head is None: 
            self.head = Node(data)
        # 마지막에 생성하는 거라면 
        else:
            curr = self.head 
            if self.count < 2: 
                while curr.next: 
                    curr = curr.next 
                prev_node = curr 
                new_node = Node(data) 
                
    # 다음역 출력
    # 현재역과 다음역 사이에 새로운 역 설립
    def bn(self):
        print()
    
    # 이전역 출력 
    # 현재역과 이번역 사이에 새로운 역 설립
    def bp(self):
        print()
    
    # 다음역 폐쇄
    # 폐쇄한역 출력
    def cn(self):
        print()
    
    # 이전역 폐쇄
    # 폐쇄한역 출력 
    def cp(self):
        print()
