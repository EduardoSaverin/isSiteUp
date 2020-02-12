import platform, subprocess

def checkConnection(host):
	option = '-c'
	if platform.system().lower() == 'windows':
		option = '-n'
	process = subprocess.run(['ping',option,'1',host], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	if process.returncode == 0:
		print(f"{host} is Up")
	else:
		print(f"{host} is Down")

def program():
	sites = []
	with open("list.txt") as file:
		checkConnection(file.readline())

if __name__ == '__main__':
	program()