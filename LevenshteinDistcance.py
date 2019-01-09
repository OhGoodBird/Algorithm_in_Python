def LevenshteinDistcance(s1, s2):
    import numpy as np
    '''
    Levenshtein Distcance
    reference: https://en.wikipedia.org/wiki/Levenshtein_distance
    
    TO-DO: write remove numpy module version
    
    Args:
        s1: string, first string
        s2: string, second string
    
    Returns:
        distance: int, Levenshtein Distcance of two string
    '''
    d = np.zeros((len(s1)+1, len(s2)+1), dtype=np.int32)
    
    for x in range(len(s1)+1):
        d[x, 0] = x
    for y in range(len(s2)+1):
        d[0, y] = y
    
    for x in range(1, len(s1)+1):
        for y in range(1, len(s2)+1):
            if(s1[x-1] == s2[y-1]):
                cost = 0
            else:
                cost = 1
            d[x, y] = min(d[x-1, y] + 1, d[x, y-1] + 1, d[x-1, y-1] + cost)
    
    return d[len(s1), len(s2)]
    
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('string1', type=str)
    parser.add_argument('string2', type=str)
    args = parser.parse_args()
        
    distance = LevenshteinDistcance(args.string1, args.string2)
    print(distance)
    
if __name__ == '__main__':
    main()
