import os
import sys
myip = sys.argv[1]
f = open('/etc/hadoop/hdfs-site.xml','r')
contents = f.readlines()
f.close()
#print contents
#print type(contents)
count = 0
for i in contents:
	count = count + 1
	print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break
#print count
os.system("rm -rf /data")


f = open('/etc/hadoop/hdfs-site.xml','w')

x=0

for i in contents:
	if(x<count):
		f.write(i)
	if(i=="</configuration>\n"):
		f.write(i)
	x=x+1
f.close()
f = open('/etc/hadoop/hdfs-site.xml','r')
contents = f.readlines()
f.close()
f=open("/etc/hadoop/hdfs-site.xml","w")
count = 0
for i in contents:
	count = count + 1
	#print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break

contents.insert(count, "<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n")
contents = "".join(contents)
f.write(contents)
f.close()


########################################################
datanode_core=open("/etc/hadoop/core-site.xml","r")
contents = datanode_core.readlines()
datanode_core.close()
count = 0
for i in contents:
	count = count + 1
        #print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break



datanode_core=open("/etc/hadoop/core-site.xml","w")

x=0

for i in contents:
	if(x<count):
		datanode_core.write(i)
	if(i=="</configuration>\n"):
		datanode_core.write(i)
	x=x+1
datanode_core = open('/etc/hadoop/core-site.xml','r')
contents = datanode_core.readlines()
datanode_core.close()
datanode_core=open("/etc/hadoop/core-site.xml","w")	
contents.insert(count, "<property>\n<name>fs.default.name</name>\n<value>hdfs://"+myip+":9001</value>\n</property>\n")
contents = "".join(contents)
datanode_core.write(contents)
datanode_core.close()

os.system("iptables -F")
os.system("hadoop-daemon.sh start datanode")

#######################################################################################


datanode_core=open("/etc/hadoop/mapred-site.xml","r")
contents = datanode_core.readlines()
datanode_core.close()
count = 0
for i in contents:
	count = count + 1
        #print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break



datanode_core=open("/etc/hadoop/mapred-site.xml","w")

x=0

for i in contents:
	if(x<count):
		datanode_core.write(i)
	if(i=="</configuration>\n"):
		datanode_core.write(i)
	x=x+1
datanode_core = open('/etc/hadoop/mapred-site.xml','r')
contents = datanode_core.readlines()
datanode_core.close()
datanode_core=open("/etc/hadoop/mapred-site.xml","w")	
contents.insert(count, "<property>\n<name>mapred.job.tracker</name>\n<value>hdfs://"+sys.argv[2]+":9002</value>\n</property>\n")
contents = "".join(contents)
datanode_core.write(contents)
datanode_core.close()

os.system("iptables -F")
os.system("hadoop-daemon.sh start tasktracker")

