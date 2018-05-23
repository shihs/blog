# -*- coding: utf-8 -*-

import datetime


title = raw_input("標題：")
date = str(datetime.datetime.now())[:16]
temp = "---\nlayout: post\ncomments: true\ntitle: " + '"' + title + '"'+ "\ndate: " + date + '\nauthor: "Shihs"' + "\ncategory: []\n---"

print temp

with open("/Users/minchunshih/Documents/My Page/blog/_posts/" + date[:10]+ "-" + title + ".md", "w") as f:
	f.write(temp)



