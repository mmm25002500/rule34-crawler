import requests
import bs4
import time
import urllib
import os

x = 1
success = 0
fault = 0

startDown = int(input('從第幾個圖片開始?:'))
endDown = int(input('第幾個圖片結束?:'))
isDownload = input('需要下載嗎?(Y/n)')
if isDownload == 'Y' or isDownload == 'y' or isDownload == 'Yes' or isDownload == 'yes':
	whereDownload = input('下載目的地(網址字串)(不需要檔案只需要目錄)(沒有則空白)')
	folderDownload = input('下載目的地(圖片與影片或是gif)(不需要檔案只需要目錄)(沒有則空白)')
	if folderDownload == '' or folderDownload == ' ':
		folderDownload = os.getcwd() + '/' + 'Rule34/'
		if not os.path.isdir(folderDownload):
			os.makedirs(folderDownload)
	if whereDownload == '' or whereDownload == ' ':
		whereDownload = 'Rule34.txt'
		file = open(whereDownload,'w')
	else:
		whereDownload = whereDownload + 'Rule34.txt'
		file = open(whereDownload,'w')
for i in range(startDown,endDown+1):
	url = 'https://rule34.paheal.net/post/view/' + str(i)
	html = requests.get(url)
	html.encoding = 'utf-8'
	bs = bs4.BeautifulSoup(html.text,'html.parser')
	bs.find('img' , class_  = 'shm-main-image')
	if isDownload == 'Y' or isDownload == 'y' or isDownload == 'Yes' or isDownload == 'yes':
		if bs.find('img' , class_  = 'shm-main-image') is None:
			print('第' + str(i) + '個無法擷取圖片')
			i += 1
			fault +=1
			continue
		else:
			bsa = bs.find('img' , class_  = 'shm-main-image').get('src')
			file.write('第' + str(i) + '個網址:' + bsa + '\n')
			print('第' + str(i) + '個網址:' + bsa + '\t下載成功')
			imgUrl = str(bsa).replace(' ','%20')
			urllib.request.urlretrieve(imgUrl, folderDownload +'{}{}.jpg'.format('',x))
			x +=1
			success+=1
	elif isDownload == 'N' or isDownload == 'n' or isDownload == 'No' or isDownload  == 'no':
		print('Thannks For Using!')
		exit()
	else:
		print('Type Error: No Option '+'\"' + isDownload + '\"') 
		print('輸入錯誤: 沒有選項' + '\"' + isDownload + '\"')
		i -= 1
		isDownload = input('需要下載嗎?(Y/n)')

file.write('總共:\t' + str(i) + '\t' + '成功:\t' + str(success) + '\t' + '失敗:\t' + str(fault))
