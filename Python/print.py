

# f-string

year=2016
event='aaa'
print(f'f-format: {year} {event} {year/2}')
print('.format: {} {} {}'.format(year, event, year / 2))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# repr(), str()

year=2016
print(str(year), type(str(year)))
print(repr(year), type(repr(year)))