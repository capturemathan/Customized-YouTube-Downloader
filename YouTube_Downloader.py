import pytube
import random
import webbrowser	
import time
import progressbar
import os
import requests
from time import sleep
from bs4 import BeautifulSoup

print("Welcome To Youtube Downloader :",os.getlogin())
print("The Date and Time are :",time.ctime())
sleep(2)
print("Crafted with love by Mathan.S")
sleep(2)
a=["M234x","Ad34T","Fr45C","J234r","PKa67"]
z=random.randint(0,4)
print("The Captcha Is :",a[z])
captcha=input("Enter the captcha :")
while(captcha!=a[z]):
	print("Enter the correct captcha..")
	a=["M234x","Ad34T","Fr45C","J234r","PKa67"]
	z=random.randint(0,4)
	print(a[z])
	captcha=input("Enter the captcha")

url="https://www.youtube.com/results?search_query="
query=""
search=input("Enter the search query :")
search=search.split(" ")
if len(search)==1:
	query=search[0]
else:
	for i in range(len(search)):
		query+=search[i]+"+"
	query=query[:-1]
url=url+query
print("View your desired video and then return to YouTube Downloader")
sleep(3)
webbrowser.open_new(url)
print("Enter the link to download :")
try:
	link=input()
	print("Loading ...")
	yt=pytube.YouTube(link)
except:
	print("Enter a proper URL !")
	link=input()
	print("Loading ...")
	yt=pytube.YouTube(link)
print("Loading ...")
bar = progressbar.ProgressBar(maxval=20, \
	widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(20):
	bar.update(i+1)
	sleep(0.1)
bar.finish()
print("The title of your video is :")
print(yt.title)
try:
        choice=int(input("Enter 1 to continue or 0 to exit :"))
except:
        print("Enter a proper number")
        choice=int(input("Enter 1 to continue or 0 to exit :"))
while((choice!=1) and (choice!=0)):
	choice=int(input("Enter 1 to continue or 0 to exit :"))
if(choice):
	print("Loading ...")
	all_streams=yt.streams.filter(progressive=True).all()
	bar = progressbar.ProgressBar(maxval=len(all_streams), \
		widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	bar.start()
	for i in range(len(all_streams)):
		bar.update(i+1)
		sleep(0.1)
	bar.finish()
	for i in range(len(all_streams)):
		print(str((i+1))+". "+str(all_streams[i]))
	try:
		ch=int(input("Enter your choice"))
	except:
		print("Enter a proper number..")
		ch=int(input("Enter your choice"))
	while((ch>len(all_streams)) or (ch<0)):
			ch=int(input("Enter your choice"))
	print("Your present working directory is :",os.getcwd())
	try:
		dir=int(input(("Press 1 to continue or 0 to change your working directory")))
	except:
		print("Enter a proper number")
		dir=int(input(("Press 1 to continue or 0 to change your working directory")))
	while((dir!=1) and (dir!=0)):
		dir=int(input("Enter 1 to continue or 0 to exit :"))
	if(dir==0):
		dir1=input(("Enter your desired directory :"))
		try:
			os.chdir(dir1)
		except:
			print("You did'nt enter the directory in the correct format")
			dir1=input(("Enter your desired directory :"))
			os.chdir(dir1)
		dir=1
		print("The List of available folders under your present working directory are :")
		files_path = [os.path.abspath(x) for x in os.listdir()]
		for i in range(len(files_path)):
			print(str((i+1))+". "+str(files_path[i]))
		ch1=int(input("Enter your desired folder :"))
		while((ch1>len(files_path)) or (ch1<0)):
			ch1=int(input("Enter your desired folder :"))
		try:
			directory=files_path[ch1-1]
		except:
			print("Enter a proper number..")
			ch1=int(input("Enter your desired folder :"))
		print("Downloading ...")
		desired_stream=all_streams[ch-1]
		desired_stream.download(directory)
		bar = progressbar.ProgressBar(maxval=len(all_streams), \
			widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
		bar.start()
		for i in range(len(all_streams)):
			bar.update(i+1)
			sleep(0.1)
		bar.finish()
		print("Download Complete!!")
	else:
		directory=os.getcwd()
		print("Downloading ...")
		desired_stream=all_streams[ch-1]
		desired_stream.download(directory)
		print("Download Complete!!")
else:
	print("Provide the correct URL to get the correct title ..")
