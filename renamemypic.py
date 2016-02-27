#!/usr/bin/env python
import MySQLdb
import os
db = MySQLdb.connect(
  host='localhost',
  user='root',
  passwd='',
  port=3306,
  charset='utf8',
  db='new_pixiv'
)
cursor = db.cursor()
ls = os.popen('cd /Users/Lich/Pictures && ls -r')
names = []
for name in ls.readlines():
    if len(name) > 40:
        names.append(name[:-1])
result = {}
for name in names:
    value = {'name' : '%'+name}
    sql = "select image_urls from illusts WHERE path LIKE %(name)s"
    cursor.execute(sql, value)
    pixiv_id = cursor.fetchone()
    if pixiv_id is not None:
        result[name] = pixiv_id[0].split('/')[-1]
for name in result:
    print name, '=>',result[name]
    os.system('cd /Users/Lich/Pictures && mv ' + name +' ' + result[name])
