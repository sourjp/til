A, B, C = map(int, input().split())

l = [5, 5, 7]

def main(A=A, B=B, C=C):
    if A in l:
        l.remove(A)
        if B in l:
            l.remove(B)
            if C in l:
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    result = main()
    print(result)