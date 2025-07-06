import numpy as np # type: ignore
print('\tWeek 1\tWeek 2\tWeek 3 Week 4')
june=np.array([[100,205,3000,0],[150,20,20,0],[180,30,270,300]])
print('1. Clothes',june[0])
print('2. Travel',june[1])
print('3. Groceries',june[2])

print('Total bill is Rs.',june.sum())
print('Average bill is Rs.',june.mean())
print('Maximum bill is of Rs.',max(june[0].sum(), june[1].sum(), june[2].sum()))