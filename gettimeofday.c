#include <stdio.h>
#include <sys/time.h>

void main(){
	FILE *fp;
	struct timeval tve;
	int k;
	fp=fopen("test_time","w");
	
	for(k=0;k<1000;k++){
		gettimeofday(&tve,NULL);
		fprintf(fp,"%ld  %ld\n",tve.tv_sec,tve.tv_usec);
	}
	fclose(fp);
}

