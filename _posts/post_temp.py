# -*- coding: utf-8 -*-

import datetime


title = input("標題：")
date = str(datetime.datetime.now())[:16]
temp = "---\nlayout: post\ncomments: true\ntitle: " + '"' + title + '"'+ "\ndate: " + date + '\nauthor: "Shihs"' + "\ncategory: []\n---"

print(temp)

with open("./" + date[:10]+ "-" + title + ".md", "w") as f:
	f.write(temp)



