import os 
import sys
import argparse


# parser = argparse.ArgumentParser(description='命令行中传入一个数字')
# #type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, help='传入的数字')

# args = parser.parse_args()

# #获得传入的参数，输出内容 Namespace(integers='5')
# print(args)






def shellAccept():
    '''
    预定义命令行参数，接收并存储
    必须参数：None
    可选参数：
    -u / --URL
    -t / --threads
    -v / --version
    @return:返回获取到的命令行参数args，以数据字典格式
    '''
    try:    # 异常处理
        parser = argparse.ArgumentParser(description="传入命令参数")
        parser.add_argument("-u", "--URL", type=str, help="待测试的URL")
        parser.add_argument("-t", "--threads", type=str, help="线程数")
        parser.add_argument("-v", "--version", type=str, help="工具版本号")
        args = parser.parse_args()  # 获取参数字典
        return args
    except Exception as e:
        print(e)





if __name__ == '__main__': 
    shellAccept()

