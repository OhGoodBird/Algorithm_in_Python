#!/usr/bin/env python3

'''
Dice Throw Problem
https://www.geeksforgeeks.org/dice-throw-dp-30/
'''

def findways(m, n, x):
    table = [[0]*(x+1) for idx in range(n+1)]
    
    for idx in range(1, min(x+1, m+1)):
        table[1][idx] = 1
    
    for idx_n in range(2, n+1):
        for idx_x in range(1, x+1):
            for idx_m in range(1, min(m+1, idx_x)):
                table[idx_n][idx_x] += table[idx_n-1][idx_x-idx_m]
    
    for x1 in table:
        for x2 in x1:
            print('{:3d},'.format(x2), end='')
        print()
    print()
    
    return table[n][x]
    
    
def main():
    print(findways(4,2,1))
    print(findways(2,2,3))
    print(findways(6,3,8))
    print(findways(4,2,5))
    print(findways(4,3,5))
    
if(__name__=='__main__'):
    main()
    
