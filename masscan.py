#!/usr/bin/env python
#coding:utf-8
import re

#对相同IP进行整理
def Removeal(l):
        check_2 = []
        check_1 = []
        for L in l:
                if L[0].strip() not in check_1:
                        check_2.append(L[0]+"=>"+L[1])
                        check_1.append(L[0])
                else:
                        num = check_1.index(L[0])
                        inster_value = check_2[num]+","+L[1]
                        check_2.insert(0,inster_value)
                        check_2.pop(num+1)
        with open("live_port.txt","w") as w:
                w.writelines(line+'\n' for line in check_2) 
#解析masscan的输出xml文件
def MASSCAN_ALL_PORT(ma_xml_file):
        ip_list =[]
        res_ip_list=[]
        xml_pattern = re.compile(r'<address addr="(.*?)".*?portid="(.*?)">')
        with open(ma_xml_file) as f:
                l=re.findall(xml_pattern,f.read())
                Removeal(list(l))

MASSCAN_ALL_PORT("158.xml")