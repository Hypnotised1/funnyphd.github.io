import xlrd
import os
from decimal import Decimal

os.chdir(os.path.dirname(__file__))
filename='./bills.xlsx'
data=xlrd.open_workbook(filename)

table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols

total_bill=[]
hanzi=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','佰']
danwei=['元','角','分']
total_top=0
total_mid=0
total_end=0
for i in range(1,nrows):
    price_str=table.cell(i,0).value
    data_top=''
    data_mid=''
    data_end=''
    if '元' in price_str:
        data = price_str.split('元')
        data_yuan =data[0]

        data_top = list(map(lambda  x: hanzi.index(x), data_yuan))

        if 10 in data_top and data_top[0]!=10 and data_top[-1]!=10:
            data_top.remove(10)
        elif data_top[0]==10:
            if len(data_top)==1:
                data_top[0]=10
            else:
                data_top[0]=1
        elif data_top[-1]==10:
            data_top[-1]=0
                
        if 11 in data_top:
            data_top.remove(11)
        

        data_top=int(''.join(str(x) for x in data_top))
        data=data[-1]

    else:
        data=price_str
        data_top=0

    if '角' in price_str:

        data = data.split('角')
        data_jiao = data[0]
        data_mid= int(''.join(list(map(lambda  x: str(hanzi.index(x)), data_jiao))))
        data=data[-1]
    else:
        # 9.006 玖元零陆分 1
        data_mid=0
   

    if '分' in price_str:

        data = data.split('分')
        data_fen = data[0]
        data_end=int(''.join(list(map(lambda  x: str(hanzi.index(x)), data_fen))))
    else:
        data_end=0

    # price = float(data_top + Decimal(0.1)* Decimal(data_mid) + Decimal(0.01) *data_end)
    number=int(table.cell(i,1).value)

    print(price_str, data_top, data_mid, data_end)
    # print(price, price_str, number)
    # print(data_top, data_mid, data_end)

    total_top+=int(data_top) * number
    total_mid+=int(data_mid) * number
    total_end+=int(data_end) * number
print(total_top, total_mid,total_end)
print(total_top+ 0.1*total_mid+0.01*total_end)


print(f'flag{{{total_top+ 0.1*total_mid+0.01*total_end}}}')

# flag{16947.62}



