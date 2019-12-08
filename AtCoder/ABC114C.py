'''
N = int(input())

def fes(cul='0'):
    if int(cul) > N:
        print('none')
        return 0 
    counter = 0
    print(cul, counter)

    if "3" in cul and "5" in cul and "7" in cul:
        counter += 1
    counter += fes(cul + "3")
    counter += fes(cul + "5")
    counter += fes(cul + "7")

    return counter

print(fes())
'''

N = int(input())

def fes(cul=0):
    if cul > N:
        return 0 
    counter = 0

    if "3" in str(cul) and "5" in str(cul) and "7" in str(cul):
        counter += 1
    counter += fes(cul * 10 + 3)
    counter += fes(cul * 10 + 5)
    counter += fes(cul * 10 + 7)

    return counter

print(fes())