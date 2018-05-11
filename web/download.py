import requests
import os

#file_url = "https://drive.google.com/uc?export=download&id=1hYsX7222wbV_sHHVw4P0s5vhlo8hu8Cn"
#os.system("xdg-open 'https://chatapp-198116.firebaseapp.com/client.html'")
os.system("rm -f /root/Downloads/log.txt")
i=0
while(True):
	
	try :
		
		f=open("/root/Downloads/log.txt").read().split(',') 
		if "USER" in f[0]:
			if "2" in f[1]:
				f[2]=f[2].replace("\n","")
				print f[2]
				
				os.system("hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar grep hdfs:/out1 hdfs:/outnew "+f[2])
				
				os.system("hadoop fs -get /outnew/part-00000 /root/Desktop/hack/")
				g=open("part-00000")
				line=g.readline()
				line=line.replace(f[2],"")
				os.system("xdg-open 'https://chatapp-198116.firebaseapp.com/upload.html?"+line+"-"+f[2]+"'")
				os.system("rm -f /root/Downloads/log.txt")
				os.system("rm -f part-00000")
				os.system("hadoop fs -rmr /outnew")
		
		elif(i==0 or limit!=y):
			y=f[1].split("/")
			
			z="https://drive.google.com/uc?export=download&id="+y[5]
			#print z
			os.system("rm -f temp")
			os.system("wget --no-check-certificate -O temp '"+z+"'")
			os.system("rm -f /root/Downloads/log.txt")
			os.system("hadoop fs -rm /out1")
			x=os.system("hadoop fs -put temp /out1")
			if(x==0):
				limit=y
				i=1
				os.system("xdg-open 'https://chatapp-198116.firebaseapp.com/upload.html?Your file Uploaded! Please Enter Your Query'")
			else :
				os.system("xdg-open 'https://chatapp-198116.firebaseapp.com/upload.html?Your file not uploaded! Please Try again'")
			
		else:
			
			pass
			#os.system("rm -f /root/Downloads/log.txt")
				
	except:
		pass	
	
	
