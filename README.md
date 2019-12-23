# FireWall-Algorithm
# a. how you tested your solution

First of all, import the Illumio.py into the file you want to test. (I have provided a run_function_example.py so you can run result with this file) Then import the class and run the function will be fine!

# b. any interesting coding, design, or algorithmic choices you’d like to point out

In my coding, I did a trade-off between time-complexity and space complexity. I build in most of the input rules into a dictionary (hashmap) in order to decrease the time consuming when judging if the test cases are true.

I combined the direction and protocol together as an index, so that the layer of dictionary could decrease.

for the input rules of like (outbound,tcp,10000-20000,192.168.10.11), since the port at most contain 65535, I will handle all the numbers from 10000-20000 into the dictionary (hashmap). So dic['inboundudp'][10000] = '192.168.10.11', dic['inboundudp'][10001] = '192.168.10.11', dic['inboundudp'][10002] = '192.168.10.11' ... etc

However, for the input rules like (inbound,udp,53,192.168.1.1-192.168.2.5), I would not put all the IP address of range 192.168.1.1 to 192.168.2.5 into the dictionary (hashmap). I would just put the string "192.168.1.1-192.168.2.5" into the value. That is to say, dic['inboundudp'][53] = "192.168.1.1-192.168.2.5". And when I want to know as if 192.168.1.141 is between range(192.168.1.1, 192.168.2.5), I will then compare by minusing method (specific in code). Thus I dont need to store 256*256*256*256 times data into the dictionary, which can save a lot of time.

The coding is pretty robust and run very quick even I give a lot input rules. Hope this idea satisfying you!

# c. any refinements or optimizations that you would’ve implemented if you had more time

If there is enough time, I think decreasing the time complexity of dealing with port could be possible (since I store all port range into the dictionary). If we want to know 10500 is in 10000-20000, we can set condition as (10500-10000 > 0) and (20000-10500 > 0) to determine if it is inside the range. But the algorithm will become more complicated since the IP address could also be a range.

# d. anything else you’d like the reviewer to know

I am really really really interested in Illumio, and I have improved my coding ability a lot through this semester. I have even build a full stack project during the period when I applied for this position, the renew resume link is at the below for your reference. Please give me a chance to join Illumio! Thank you! https://drive.google.com/file/d/1IvNh1Qgi_b4WolwrqmTn3pk11CPNLPY2/view

# The particular team that you’re interested in.

Actually I am really interest in data-team and platform-team. Although my past experience is more related to data-team, I have also learn some skills at platform and software engineer side. I am confident that I could handle each team well. Thank you so much for your consideration.
