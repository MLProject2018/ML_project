import csv

api_list = []

filenames = ['../split_1.csv', '../split_2.csv', '../split_3.csv', '../split_4.csv', '../split_5.csv', '../split_6.csv', '../split_7.csv', '../split_8.csv', '../split_9.csv']

for filename in filenames:
    print(filename)
    with open(filename) as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                api = row[2]
                if api not in api_list:
                    api_list.append(api)
        except:
            print('Error')
    print(len(api_list))

with open('api_list.txt', 'w+') as f:
    f.write(str(api_list))
