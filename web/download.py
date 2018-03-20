import requests
file_url = "https://drive.google.com/uc?export=download&id=1hYsX7222wbV_sHHVw4P0s5vhlo8hu8Cn"
r = requests.get(file_url, stream = True) 
with open("python.txt","wb") as pdf:
	for chunk in r.iter_content(chunk_size=1024):
		if chunk:
			pdf.write(chunk)
