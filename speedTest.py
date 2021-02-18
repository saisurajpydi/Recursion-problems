"""
speed test
"""
"""
import speedtest
s = speedtest.Speedtest()
options = int(input("what do u want to know: i) upload speed  ii) download speed  iii) ping"))
if options == 1:
    print(s.upload())
elif options == 2:
    print(s.download())
elif options == 3:
    server = []
    s.get_servers(server)
    print(s.results.ping)
else:
    print("invalid option")
"""
# Python program to test 
# internet speed 

import speedtest 


st = speedtest.Speedtest() 

option = int(input('''What speed do you want to test: 

1) Download Speed 

2) Upload Speed 

3) Ping 

Your Choice: ''')) 


if option == 1: 

	print(st.download()) 

elif option == 2: 

	print(st.upload()) 

elif option == 3: 

	servernames =[] 

	st.get_servers(servernames) 

	print(st.results.ping) 

else: 

	print("Please enter the correct choice !") 
