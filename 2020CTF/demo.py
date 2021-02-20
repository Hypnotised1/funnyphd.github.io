import xlrd
import os
os.chdir(os.path.dirname(__file__))
filename='./bills.xlsx'
data=xlrd.open_workbook(filename)

table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols

total_bill=[]
hanzi=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','佰']
danwei=['元','角','分']
total=0
for i in range(1,nrows):
    price_str=table.cell(i,0).value
    data_top=''
    data_mid=''
    data_end=''
    if '元' in price_str:
        data = price_str.split('元')
        data_yuan =data[0]


        #  成千上百的, 无法计算.
        data_top = list(map(lambda  x: hanzi.index(x), data_yuan))

        if 11 in data_top:
            # print(len(data_top),'-------')
            data_top = data_top[0]* 100+data_top[2]*10+data_top[-1]
            # [1, 11, 0, 2]
            # [1, 11, 1, 10, 5]
            # [1, 11, 0, 3]

        elif 10 in data_top:
            # 10.35 拾壹元叁角伍分 3
            
            if len(data_top)==3:
                data_top=data_top[0]*data_top[1]+data_top[2]
            elif len(data_top)==2:
                data_top=data_top[0]*data_top[1]
            else:
                data_top=data_top[0]
        else:
            data_top=data_top[0]

        data=data[-1]
    else:
        data=price_str
        data_top='0'

    if '角' in price_str:

        data = data.split('角')
        data_jiao = data[0]
        data_mid= list(map(lambda  x: hanzi.index(x), data_jiao))[0]
        data=data[-1]
    else:
        data_mid='0'
   

    if '分' in price_str:

        data = data.split('分')
        data_fen = data[0]
        data_end=''.join(list(map(lambda  x: str(hanzi.index(x)), data_fen)))
 
    price = str(data_top) + '.' + str(data_mid) + str(data_end)
    number=int(table.cell(i,1).value)
    print(price, price_str, number)

    total+=float(price) * number
    # for j in data_yuan:
    #     data_top+=str(hanzi.index(j)+1)
    
    # data = data[-1].split('角')
    # data_jiao = data[0]
    # data_mid=''
    # for j in data_jiao:
    #     data_mid+= hanzi.index(j)+1
    
    # data = data[-1].split('分')
    # data_fen = data[0]
    # data_end=''

    # for j in data_fen:
    #     data_end+= hanzi.index(j)+1


    
    # print(price_str, )
# print(nrows, ncols)
print(total)