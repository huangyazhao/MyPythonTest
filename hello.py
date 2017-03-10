# -*- coding: utf-8 -*-
'''
Created on 2017年2月23日

@author: huang
'''
import time
from MSsql import MSsqlConn

if __name__ == '__main__':
    '''
    #conn=pymssql.connect(host='192.168.76.157',user='nnzk',password='nnzk',database='nnzk')
    conn=pymssql.connect(host='134.201.178.40:33433',user='nnzk',password='nnzk',database='nnzk')
    cur=conn.cursor()
    cur.execute('SELECT TOP 2 *  FROM [nnzk].[dbo].[2]')
    print (cur.fetchall())
    cur.close()
    conn.close()
    '''
    a=MSsqlConn('134.201.178.40:33433','nnzk','nnzk','nnzk')
    a.dbConn()
    a.seleSql('SELECT *  FROM [nnzk].[dbo].[test]')
    
    #nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    a.udiSql("insert into test values('赵八','男','三中',11,'%s')" %time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    a.udiSql("update  test  set logtime='%s' where name = '李四' " %time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    a.udiSql("delete from test where name = '赵八' ")    
    a.closeConn()
        