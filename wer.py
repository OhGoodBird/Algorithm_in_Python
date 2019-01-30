#!/usr/bin/env python3

def compute_ids(ref, hyp):
    '''
    Compute insersion, deletion and substitution of two string.
    
    Args:
        ref: string, reference
        hyp: string, hypothesis
    
    Returns:
        insersion: int
        deletion: int
        substitution: int
    '''
    d = [[0 for x in range(len(ref)+1)] for y in range(len(hyp)+1)]
    backtrace = [['O' for x in range(len(ref)+1)] for y in range(len(hyp)+1)]
        
    
    for y in range(1, len(ref)+1):
        d[0][y] = y
        backtrace[0][y] = 'D'
    for x in range(1, len(hyp)+1):
        d[x][0] = x
        backtrace[x][0] = 'I'
    
    # compute distance
    for x in range(1, len(hyp)+1):
        for y in range(1, len(ref)+1):
            if(ref[y-1] == hyp[x-1]):
                d[x][y] = d[x-1][y-1]
                backtrace[x][y] = 'O'
            else:
                d[x][y] = min(d[x-1][y] + 1, d[x][y-1] + 1, d[x-1][y-1]+1)
                if(d[x][y] == d[x-1][y] + 1):
                    backtrace[x][y] = 'I'
                elif(d[x][y] == d[x][y-1] + 1):
                    backtrace[x][y] = 'D'
                else:
                    backtrace[x][y] = 'S'
    
    # backtrace
    x = len(hyp)
    y = len(ref)
    num_ins, num_del, num_sub = 0, 0, 0
    while(x > 0 and y > 0):
        if(backtrace[x][y] == 'O'):
            x -= 1
            y -= 1
        elif(backtrace[x][y] == 'I'):
            x -= 1
            num_ins += 1
        elif(backtrace[x][y] == 'D'):
            y -= 1
            num_del += 1
        elif(backtrace[x][y] == 'S'):
            x -= 1
            y -= 1
            num_sub += 1
    
    # show tables
    #for x in d:
    #    for y in x:
    #        print('%d, '%(y), end='')
    #    print()
    #print()
    #for x in backtrace:
    #    for y in x:
    #        print('%s, '%(y), end='')
    #    print()
    #print('ins = {}'.format(num_ins))
    #print('del = {}'.format(num_del))
    #print('sub = {}'.format(num_sub))
    
    return num_ins, num_del, num_sub
    
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('reference', type=str)
    parser.add_argument('hypothesis', type=str)
    args = parser.parse_args()
        
    num_ins, num_del, num_sub = compute_ids(args.reference, args.hypothesis)
    wer = (num_ins + num_del + num_sub)*100 / len(args.reference)
    print('WER = {:.2f} %'.format(wer))
    
if __name__ == '__main__':
    main()
    
    
