import os
import sys
import argparse
import subprocess
import time
'''
	自定义参数

'''
default_thread = 3

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
        parser.add_argument("-u", "--url", type=str,required=True, help="待测试的URL")
        parser.add_argument("-t", "--threads", type=str, help="线程数")
        parser.add_argument("-ssh", "--ssh", type=str, help="指定ssh爆破参数")
        parser.add_argument("-ftp", "--ftp", type=str, help="指定ftp爆破参数")
        parser.add_argument("-rdp", "--rdp", type=str, help="指定rdp爆破参数")
        parser.add_argument("-mysql", "--mysql", type=str, help="指定mysql爆破参数")
        parser.add_argument("-redis", "--redis", type=str, help="指定redis爆破参数")
        parser.add_argument("-dir", "--dir", type=str, help="指定dirsearch参数")

        parser.add_argument("-v", "--version", type=str, help="工具版本号")
        args = parser.parse_args()  # 获取参数字典
        return args
    except Exception as e:
        print(e)


if __name__ == '__main__': 
    args = shellAccept()
    thread = default_thread if args.threads==None else args.threads
    if args.version !=None:
    	print("version_1.0")
    print("""
            ||====================================
            ||	url：  """+args.url+"""  
            ||	线程数：   """+thread+ """   
            ||====================================
        """)
    if args.ssh !=None:
    	print("==================================================================检测到ssh参数 开始爆破ssh服务====================================================")
    	print("")
    	res = ""
    	if args.ssh.isdigit():
    		print("接收到ssh端口号"+args.ssh)
    		cmd = "hydra "+args.url+" ssh -L ./dict/user.txt -P ./dict/pass.txt -s "+args.ssh+" -t "+thread+" -V -f |tee ssh.log"
    	else:
    		print("使用ssh 默认端口号")
    		cmd = "hydra "+args.url+" ssh -L ./dict/user.txt -P ./dict/pass.txt -t "+thread+" -V -f |tee ssh.log"
    	print("正在执行命令 :" + cmd)
    	res=os.system(cmd)
    	print("==================================================================ssh 扫描命令执行结束==================================================")
    	print("\n")
    	time.sleep(8)	
    
    if args.ftp !=None:
    	print("==================================================================检测到ftp参数 开始爆破ftp服务====================================================")
    	print("")
    	res = ""
    	if args.ftp.isdigit():
    		print("接收到ftp端口号"+args.ftp)
    		cmd = "hydra "+args.url+" ftp -L ./dict/user.txt -P ./dict/pass.txt -s "+args.ftp+" -t "+thread+" -V -f |tee ftp.log"
    	else:
    		print("使用ftp 默认端口号")
    		cmd = "hydra "+args.url+" ftp -L ./dict/user.txt -P ./dict/pass.txt -t "+thread+" -V -f |tee ftp.log"
    	print("正在执行命令 :" + cmd)
    	res=os.system(cmd)
    	print("==================================================================ftp 扫描命令执行结束==================================================")
    	time.sleep(8)	
    

