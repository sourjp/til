keys = input()
outputs = []

for key in keys:
    if key == 'B':
        if not outputs:
            pass
        else:
            outputs.pop()
    else:
        outputs.append(key)

for output in outputs:
    print(output, end='')
