#!/usr/bin/env python
#!coding:utf-8
import os
file = "/Users/Lich/Downloads/resume.lich2013.com_sha256_cn.zip"
list = ['⑨',
'四散的尘埃',
'acg和谐区',
'acgzone.us',
'http://acgzone.us/',
'acgzone.tk',
'琉璃神社',
'hacg.me',
'节操粉碎机',
'http://www.tianshi2.com',
'傲娇零：aojiao.org ',
'i-ab.com',
'黙示',
'天照大御神',
'猫与好天气 ',
'扶她奶茶',
'lifaner.com ',
'456black',
'moe',
'动漫本子吧',
'里番儿',
'lsmj',
'674434350 psp.duowan.com',
'光影交错的时空 ',
'御宅同萌',
'tangtang',
'9999或999',
'士凛密码',
'名字就是',
'827283516',
'ce',
'樱花树下实现',
'yhsxsx',
'www.acgft.us',
'hentai',
'tianshi2',
'lifaner.com',
'妮妙',
'发条奶茶',
'七曜苏醒 ',
'123456',
'yaoying',
'gg',
'air',
'琉璃神社',
'天照大御神',
'爱有缘有份 ',
'YES',
'malow005',
'我没有节操',
'拉杰尔的图书馆',
'20131225',
'RoC_1112@eyny',
'moe',
'benzi',
'Q10',
'tianshi2.com',
'180998244',
'ntr',
'CR48',
'inori',
'BQ510',
'120505478',
'社会主义歼星炮 ',
'技术宅',
'通宵狂魔技术宅']
type = file.split('.')[-1]
uncompress = {'zip': lambda password: 'unzip ' + '-P ' + password + ' "' + file + '"',
			  'rar': lambda password: 'unrar x "' + file + '" -p' + password + ' -y'}
for x in list:
	commond = uncompress[type](x)
	print commond
	os.system(commond)

exit(0)



