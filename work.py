import csv

with open ('水务.csv') as file:
    reader = csv.reader(file)
    for data_list in reader:
        filename = data_list[2] + '.md'
        with open(filename, 'w') as mdFile:
            mdFile.write('---\n')
            mdFile.write('序号: ' + data_list[0] + '\n')
            mdFile.write('市级指导部门: ' + data_list[1] + '\n')
            mdFile.write('实施清单名称: ' + data_list[2] + '\n')
            mdFile.write('法律法规: ' + data_list[3] + '\n')
            mdFile.write('实施编码: ' + data_list[4] + '\n')
            mdFile.write('事项类型: ' + data_list[5] + '\n')
            mdFile.write('备注: ' + data_list[6] + '\n')
            mdFile.write('---' + '\n')
