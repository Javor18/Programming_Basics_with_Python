city = input()
sales = float(input())

city_commission  = True
sales_count = True
comision = 0
if 0 <= sales <= 500:
    if city == 'Sofia':
        comision = 0.05
    elif city =='Varna':
        comision = 0.045
    elif city == 'Plovdiv':
        comision = 0.055
elif 500< sales <= 1000:
    if city == 'Sofia':
        comision = 0.07
    elif city == 'Varna':
        comision = 0.075
    elif city == 'Plovdiv':
        comision = 0.08
elif 1000< sales <= 10000:
    if city == 'Sofia':
        comision = 0.08
    elif city == 'Varna':
        comision = 0.10
    elif city == 'Plovdiv':
        comision = 0.12
elif  sales > 10000:
    if city == 'Sofia':
        comision = 0.12
    elif city == 'Varna':
        comision = 0.13
    elif city == 'Plovdiv':
        comision = 0.145
    else:
        city = False
else:
    sales = False



if comision == 0:
    print(f'error')
else:
    total_commission = sales * comision
    print(f'{total_commission:.2f}')
