# Ztest
Some test about zeromq

Originally use naive one to one PUB-SUB Model to test the latency and throughput of zeromq  
test_pub.c --code for publisher  
test_sub.c --code for subscriber  
plot.py  --generate data to plot latency and throughput  
However,subscriber will miss the messages when lantency accumulate  
So go to PUSH-PULL model
  
  

