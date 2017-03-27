from __future__ import print_function
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        sttn = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ph = sys.stdin.read(1)
            if ph == '\x1b':
                ph+=sys.stdin.read(2)
        finally:
            termios.tcsetattr(fd,termios.TCSADRAIN,sttn)
        return ph
input_file = open(sys.argv[1],'r')
counter=1
l=[]
s = input_file.readline()
initial = input_file.tell()
while(True):
    inpk = _Getch()
    for lines in range(50):
	    print(counter,s,sep=' ')
	    l.append(str(counter)+" "+s+'\n')
	    s = input_file.readline()
	    counter+=1
    print('\nType Q to quit, P to read the previous lines, M to move to a specific line number, S to search for a text, otherwise press the Enter/Return Key ',end=' ')
    user_input = inpk()
    if user_input == 'Q':
        break
    elif user_input == 'P':
	print("*****",*l)
	inp = raw_input('\nType C to continue ')
	if inp == 'C':
	    continue
    elif user_input == 'M':
        inp = raw_input('\nEnter the line numbers to be moved ahead from the current position ')
	for Mlines in range(int(inp)):
	    l.append(str(counter)+' '+input_file.readline()+'\n')
	    counter+=1
	print("*******************************************")
	continue
    elif user_input == 'S':
        inp = raw_input('\nEnter the text to be searched followed by an offset from where to begin the search-Enter B for beginning and P for present ')
        text,offset = inp.split()
        if offset == 'B':
            for i in l:
                if text in i:
                    print(i)
            uip = raw_input('\nSearch Completed!! Press C to continue scrolling the file')
	    if uip == 'C':
	        continue
        elif offset == 'P':
	    search_file = open(sys.argv[1],'r')
	    search_file.seek(input_file.tell())
            scounter = counter+1
	    flag=''
	    while(True):
	        for line in range(50):
                    se = search_file.readline()
	            if text in se:
                        print(str(scounter)+" "+se+'\n')
		    scounter+=1
                uip = raw_input('\nEnter Q to Quit Searching ')
                if uip == 'Q':
                    break
    elif user_input == '\x1b[B':
	    continue
    elif user_input == 'X':
	    print('\nBad Input!!')