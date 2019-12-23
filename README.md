# FireWall-Algorithm
# a. how you tested your solution

First of all, import the Illumio.py into the file you want to test. (I have provided a run_function_example.py so you can run result with this file) Then import the class and run the function will be fine!

# b. any interesting coding, design, or algorithmic choices you’d like to point out

In my coding, I did a trade-off between time-complexity and space complexity. I build in most of the input rules into a dictionary (hashmap) in order to decrease the time consuming when judging if the test cases are true.
I combined the direction and protocol together as an index, so that the layer of dictionary could decrease.

for the input rules of like (outbound,tcp,10000-20000,192.168.10.11), since the port at most contain 65535, I will handle all the numbers from 10000-20000 into the dictionary (hashmap). So dic['inboundudp'][10000] = '192.168.10.11', dic['inboundudp'][10001] = '192.168.10.11', dic['inboundudp'][10002] = '192.168.10.11' ... etc

However, for the input rules like (inbound,udp,53,192.168.1.1-192.168.2.5), I would not put all the IP address of range 192.168.1.1 to 192.168.2.5 into the dictionary (hashmap). I would just put the string "192.168.1.1-192.168.2.5" into the value. That is to say, dic['inboundudp'][53] = "192.168.1.1-192.168.2.5". And when I

# c. any refinements or optimizations that you would’ve implemented if you had more time

# d. anything else you’d like the reviewer to know

# The particular team that you’re interested in.
