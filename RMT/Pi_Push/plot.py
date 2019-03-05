def get_usefuldata(filename=""): 
    fp=open(filename)
    lines=fp.readlines()
    clock=[]
    for line in lines:
        line=line[:-1]
        time=line.split('  ',1)
        #print(time[0]+" fff "+time[1])
        time[0]=int(time[0])
        time[1]=int(time[1])
        clock.append(time)
    fp.close()
    return clock

def throughput(data=[],filename=""):
    fp=open(filename,'w')
    timeval=[]
    for i in range(1,len(data)):
        timeval.append((data[i][0]-data[i-1][0])*1000000+data[i][1]-data[i-1][1])
        fp.write(str(timeval[i-1])+"\n")
    fp.close()
    return timeval

def latency(pub=[],sub=[]):
    latency=[]
    fp=open("latency",'w')
    if len(pub)!=len(sub):
        print("length not same\n")
        return 1
    for i in range(0,len(sub)):
        latency.append((sub[i][0]-pub[i][0])*1000000+sub[i][1]-pub[i][1])
        fp.write(str(latency[i])+"\n")
    fp.close()
    return latency



push_data=get_usefuldata("push")
pull_data=get_usefuldata("pull")
push_throughput=throughput(push_data,"push_throughput")
pull_throughput=throughput(pull_data,"pull_throughput")
latency_data=latency(push_data,pull_data)

