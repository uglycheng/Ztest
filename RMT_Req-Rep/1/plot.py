import matplotlib.pyplot as plt

def get_useful_data(filename=""): 
    raw_data=open(filename)
    lines=raw_data.readlines()
    useful_data=[]
    for line in lines:
        line=line[:-1]            #kick the \n out
        m_and_u_seconds=line.split('  ',1)
        m_and_u_seconds[0]=int(m_and_u_seconds[0])
        m_and_u_seconds[1]=int(m_and_u_seconds[1])
        useful_data.append(m_and_u_seconds)
    raw_data.close()
    return useful_data

def get_throughput(data=[],filename=""):
	throughput=open(filename,'w')
	timeval=[]
	for i in range(1,len(data)):
		timeval.append((data[i][0]-data[i-1][0])*1000000 + data[i][1]- data[i-1][1])
		throughput.write(str(timeval[i-1])+"\n")
	throughput.close()
	return timeval

def get_latency(send=[],recv=[]):
    latency_data=[]
    latency=open("latency",'w')
    if len(send)!=len(recv):
        print("length not same\n")
        return 1
    for i in range(0,len(send)):
        latency_data.append(( (recv[i][0] - send[i][0])*1000000 + recv[i][1] - send[i][1]) / 2)
        latency.write(str(latency_data[i])+"\n")
    latency.close()
    return latency_data


'''generate data file'''
send_data = get_useful_data("send")
recv_data = get_useful_data("recv")
send_throughput = get_throughput(send_data,"send_throughput")
recv_throughput = get_throughput(recv_data,"recv_throughput")
latency_data = get_latency(send_data,recv_data)

'''plot throughput and latenct'''
plt.figure(figsize=(20,20),dpi=200)

plt.subplot(2,2,1)
plt.title("throughput_recv")
plt.xlabel("order of messages")
plt.ylabel("time to process the message (us)")
plt.plot(list(range(1,len(recv_throughput)+1)),recv_throughput,linewidth=0.5)
#plt.plot(list(range(1,len(send_throughput)+1)),send_throughput,linewidth=0.5,label='send')
#plt.legend(loc="upper right")

plt.subplot(2,2,2)
plt.title("throughput_send")
plt.xlabel("order of messages")
plt.ylabel("time to process the message (us)")
plt.plot(list(range(1,len(send_throughput)+1)),send_throughput,linewidth=0.5)


plt.subplot(2,1,2)
plt.title("latency")
plt.ylabel("latency (us)")
plt.xlabel("order of messages")
plt.plot(list(range(1,len(latency_data)+1)),latency_data)

plt.tight_layout()
plt.savefig("ZMQ_Performance_Test.png")




