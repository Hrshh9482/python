n = int(input())
class Pattern:
    def part1(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end =" ")
            for j in range(2*i+1):
                print("*", end = " ")
            for j in range(n-i-1):
                print(" ", end =" ")
            print(" ")
    def part2(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end =" ")
            for j in range(2*n -(2*i +1)):
                print("*", end = " ")
            for j in range(i):
                print(" ", end =" ")
            print(" ")
    def __init__(self):
        self.part1(n)
        self.part2(n)
Pattern()