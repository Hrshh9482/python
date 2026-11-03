n = int(input())
class Pattern:
    def part1(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end = " ")
            print(" ")
    def part2(self, n):
        for i in range(n-1):
            for j in range(n-i-1):
                print("*",end = " ")
            print(" ")
    def __init__(self):
        self.part1(n)
        self.part2(n)
Pattern()
#patterns added