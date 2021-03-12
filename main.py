import sys
import time

import filler

print(r'请选择执行模式 (两种模式的区别以及程序使用请先阅读 README 文件)')
print('1. 完全模式')
print('2. 更新模式')
print('其它. 退出')

num = input()
print()
if num != '1' and num != '2':
    sys.exit()

my_filler = filler.Filler(num)

data_res, content = my_filler.get_fill_list()
if data_res is True:
    print(r"1. 生成獭爹代码并拷贝到剪贴板")
    print(r"2. 执行填充操作 (注意: 程序执行后请在5秒之内将鼠标指针移动到网页的创建词语输入框处)")
    print(r"其它. 退出程序")

    command_index = input()
    print()
    if command_index == '1':
        my_filler.export_tata_code()
    elif command_index == '2':
        time.sleep(5)
        my_filler.fill()
    else:
        sys.exit()

    input("请按任意键退出")
else:
    print(r"[ERROR] 数据文件错误 请检查data.txt或data_old.txt完整性")
