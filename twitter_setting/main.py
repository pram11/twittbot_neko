#this is a main file
#Date: 2015.07.29

#functions
def auth_checker():
	try:
		f=open('/home/auth_data.txt')
	except:
		return "False"
	f.close()
	return "True"

def authfile_gen():
	f=open('/home/auth_data.txt','w')
	print("계정명을 입력하세요")
	twitter_id=input()
	f.write('twitter_acount:')
	f.write(twitter_id)
#initializing program

#check this variable before checking twitter auth needed
check_auth = auth_checker()

if check_auth=="False":
	print ("auth file don't exist.generate file." )
	authfile_gen()

else: 
	print("file exists")

