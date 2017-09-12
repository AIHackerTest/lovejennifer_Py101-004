def daily():
	print(open('my.log').read())
	while 1:
	    d = input(">>> ")
	    #print(d)
	    if d in ['q','quit','exit']:
	    	break
	    elif d in ['s','sync']:
	    	#print('sdsdsdsd sds s ...')
	    	print(open('my.log').read())
	    elif d in ['?','h','H','help']:
	    	print('''usage:
	    	?|h|H|help help
	    	s|sync re-load all history msg
	    	q|quit|exit quit
	    	''')
	    else:
	    	print('saving', d)
	    	open('my.log', 'a').write('\n'+d)



if __name__ == '__main__':
	daily()
