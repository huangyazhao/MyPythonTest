# -*- coding: utf-8 -*-
'''
Created on 2017年2月24日

@author: huang
'''

import pymssql

class MSsqlConn():
    def __init__(self,host,user,passwd,dbname):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.dbname=dbname
        #self.dbConn(host,user,passwd,dbname)
        #sqlResult = self.seleSql(sql)
        #self.closeConn()
        pass
    
    pass

    def dbConn(self):
        self.conn=pymssql.connect(host=self.host,user=self.user,password=self.passwd,database=self.dbname)
        self.cur=self.conn.cursor()
    
    def seleSql(self,sql):
        self.cur.execute(sql)
        #print (self.cur.fetchall())
        self.sqlResult = self.cur.fetchall()
        #return self.sqlResult
        self.formattedData(self.sqlResult)
        
    def udiSql(self,sql):
        self.cur.execute(sql)
        #print (self.cur.fetchall())
        #self.sqlResult = self.cur.fetchall()
        #return self.sqlResult
        self.conn.commit()
        print "%s操作成功"%sql
        
    def closeConn(self):
        self.cur.close()
        self.conn.close()
    
    def formattedData(self,result):
        for i in result:
            for m in i:
                print m,
            print
            pass
        pass
    
