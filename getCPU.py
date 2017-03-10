# -*- coding: utf-8 -*-
'''
Created on 2017年2月27日

@author: huang
'''
import wmi,time


def cpu_use(): 
    #5s取一次CPU的使用率 
    c = wmi.WMI() 
    while True: 
        for cpu in c.Win32_Processor(): 
            timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime()) 
            print '%s | Utilization: %s: %d %%' % (timestamp, cpu.DeviceID, cpu.LoadPercentage) 
            time.sleep(5) 