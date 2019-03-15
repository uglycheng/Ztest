import matplotlib.pyplot as plt

def transfer_logfile_data_to_useful_list(logfile_name="requester.log"):
	logfile=open(logfile_name)                                                       
	loglines=logfile.readlines()                                                        
																						
	pid=loglines[7][1:-1].split()[0]                                                    
	length_of_pid=len(pid)                                                              
																						
	res=[]
	shr=[]
	cpu_percent=[]
	ram_percent=[]
	times=[]
	moment=0
	for line in loglines:
		if line[1:length_of_pid+1]==pid:
			line=line[1:-1].split()
			res.append(int(line[5]))
			shr.append(int(line[6]))
			cpu_percent.append(round(float(line[8]),1))
			ram_percent.append(round(float(line[9]),1))
			times.append(moment)
			moment=moment+0.5
	return res,shr,cpu_percent,ram_percent,times

def generate_data_file(file_name='',y=[],x=[]):
	fp=open(file_name,'w')
	fp.write("time"+"	"+"value"+"\n")
	for i in range(0,len(y)):
		fp.write(str(x[i])+"	"+str(y[i])+"\n")
	fp.close()


def plot_data(figure_name='',y=[],x=[]):
	plt.title(figure_name+" Plot")
	plt.xlabel("Time")
	plt.ylabel(figure_name)
	plt.plot(x,y,linewidth=1)
	plt.savefig(figure_name+".png")
	plt.close()
	
	
	
res,shr,cpu_percent,ram_percent,times=transfer_logfile_data_to_useful_list()

generate_data_file("RES",res,times)
plot_data("RES",res,times)

generate_data_file("SHR",shr,times)
plot_data("SHR",shr,times)

generate_data_file("CPU Percent",cpu_percent,times)
plot_data("CPU Percent",cpu_percent,times)

generate_data_file("RAM Percent",ram_percent,times)
plot_data("RAM Percent",ram_percent,times)
