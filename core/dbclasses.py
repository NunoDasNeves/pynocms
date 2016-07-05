#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
import os

class DBConfig:
    def __init__(self, configpath):
        self.exists = False
        self.valid = False
        self.name = ""
        self.user = ""
        self.password = ""
        self.host = "localhost"
        self.configpath = configpath
        
    def check_existence(self): 
        if os.path.isfile(self.configpath):
            self.exists = True
        else:
            self.exists = False
            self.valid = False # if it doesn't exist, it can't be valid
        return self.exists
            
    def  check_valid(self):
        self.f = open(self.configpath, "r")
        self.list = self.f.read().split('\n')
        # find values with split
        if len(self.list) == 5:
            self.valid = True
            # TODO regexp this so user can create file manually without being as strict with formatting
            self.name = self.list[0].split('=')[1]
            self.user = self.list[1].split('=')[1]
            self.password = self.list[2].split('=')[1]
            self.host = self.list[3].split('=')[1]
        else:
            self.valid = False
        self.f.close()
        return self.valid
        
class DBCnx:
    def __init__(self):
        self.connected = False
        
    def connect(self, configfile):
        try:
            self.cnx = mysql.connector.connect(user=configfile.user, password=configfile.password, host=configfile.host,database=configfile.name)
            self.cursor = self.cnx.cursor(dictionary=True) 
            self.connected = True
        #except mysql.Error as err:
         #   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         #         print("Error: could not connect to database "+configfile.name+" on "+configfile.user+"@"+configfile.host+"; authentication failed\n")
         #   elif err.errno == errorcode.ER_BAD_DB_ERROR:
         #       print("Error: database "+configfile.name+" does not exist\n")
         #   else:
         #       print(err)
        except:
            self.cnx.close()
            self.connected = False
            
        return self.connected
    
    def close(self):
        if self.connected:
            self.cnx.close()
        
    # why do we need this? oh...hmm? nah not sure
    def create_tables(self):
        '''
        "CREATE TABLE IF NOT EXISTS `users` ( \
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, \
        `group` VARCHAR(50) CHARACTER SET utf8 NOT NULL,  \
        `joindate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
        `username` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `email` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `password` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        PRIMARY KEY (`id`), \
        UNIQUE KEY (`username`) \
        );"
        '''
        
        '''
        "CREATE TABLE IF NOT EXISTS `pages` ( \
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, \
        `title` VARCHAR(50) CHARACTER SET utf8 NOT NULL,  \
        `author` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
        `editeddate` TIMESTAMP, \
        `slug` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `template` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `text` LONGTEXT CHARACTER SET utf8 NOT NULL, \
        PRIMARY KEY (`id`), \
        UNIQUE KEY (`slug`) \
        );"
        '''
        
        '''
        "CREATE TABLE IF NOT EXISTS `posts` ( \
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, \
        `title` VARCHAR(50) CHARACTER SET utf8 NOT NULL,  \
        `author` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `slug` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
        `editeddate` TIMESTAMP, \
        `photo` VARCHAR(100) CHARACTER SET utf8, \
        `text` LONGTEXT CHARACTER SET utf8 NOT NULL, \
        PRIMARY KEY (`id`), \
        UNIQUE KEY (`slug`) \
        );"
        '''
        
        '''
        "CREATE TABLE IF NOT EXISTS `comments` ( \
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, \
        `postid` BIGINT UNSIGNED NOT NULL, \
        `author` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
        `text` LONGTEXT CHARACTER SET utf8 NOT NULL, \
        PRIMARY KEY (`id`) \
        );"
        '''
        
        '''
        "CREATE TABLE IF NOT EXISTS `sessions` ( \
        `username` VARCHAR(50) CHARACTER SET utf8 NOT NULL, \
        `date` TIMESTAMP, \
        `ssid` CHAR(32) CHARACTER SET utf8 NOT NULL, \
        `ip` VARCHAR(40) CHARACTER SET utf8 NOT NULL, \
        UNIQUE KEY (`ssid`) \
        );"
        '''
        
        return True
    
    def drop_tables(self):
        return True
    
    def select_unique_field(self, responsecol, table, col, val):
        # TODO make this secure
        if self.connected:
            try:
                self.cursor.execute("SELECT "+responsecol+" FROM "+table+" WHERE "+col+"='"+val+"';")
                response = self.cursor.fetchone()[responsecol]
            except:
                response = "Error: {}".format(mysql.connector.Error)
        return response
    
    def authenticate_user(self, username, password):
        # TODO make this secure
        if self.connected:
            try:
                self.cursor.execute("SELECT count(username) as total FROM users WHERE username='"+username+"' AND password='"+password+"';")
                response = self.cursor.fetchone()["total"]
            except mysql.connector.Error as err:
                response = "Error: {}".format(err)
        return response
    
    def insert_row(self, table, cols, values):
        # TODO make this secure
        if self.connected:
            try:
                self.cursor.execute("REPLACE INTO `"+table+"` ("+cols+") VALUES ("+values+");")
                self.cnx.commit()
                response = "Success"
            except mysql.connector.Error as err:
                response = "Error: {}".format(err)
        return response
    
    def delete_row(self, table, col, value):
        # TODO make this secure
        if self.connected:
            try:
                self.cursor.execute("DELETE FROM `"+table+"` WHERE `"+col+"`='"+value+"';")
                self.cnx.commit()
                response = "Success"
            except mysql.connector.Error as err:
                response = "Error: {}".format(err)
        return response