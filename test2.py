import requests
import csv

from urllib3.filepost import writer

url='https://reqres.in/api/users.csv'
p2_url='https://reqres.in/api/users?page=2.csv'
response=requests.get(p2_url)
data=response.json()


with open('user_info .csv','w',newline='')as file:
	writer=csv.DictWriter(file,fieldnames=['id','email','first_name','last_name','avatar'])
	writer.writeheader()
	(writer.writerow({'id':1,'email':"george.bluth@reqres.in",'first_name':"George",'last_name':"Bluth",'avatar':"https://reqres.in/img/faces/1-image.jpg"}))

with open('data_form_page=2 .csv','w',newline='')as fille:
	write=csv.DictWriter(fille,fieldnames=['id','email','first_name','last_name','avatar'])
	write.writeheader()
	for d in data['data']:
		id=d['id']
		email=d['email']
		first_name=d['first_name']
		last_name=d['last_name']
		avatar=d['avatar']
		write.writerow({'id': id, 'email': email, 'first_name': first_name, 'last_name': last_name,
						 'avatar': avatar})
# **********************************************************************************
url2='http://universities.hipolabs.com/search'
re=requests.get(url2)
data_2=re.json()
with open('user_information .csv','w',newline='')as fil:
	writter=csv.DictWriter(fil,fieldnames=['University_name','country','web_pages'])
	writter.writeheader()
	for da in data_2:
		University_name=da['name']
		country=da['country']
		web_pages=da['web_pages']
		writter.writerow({'University_name':University_name,'country':country,'web_pages':web_pages})





