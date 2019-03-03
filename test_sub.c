//  Hello World server

#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>
#include<sys/time.h>


int main (void)
{
    
    int j;
  
    struct timeval tve;
    FILE *fp;
    void *context = zmq_ctx_new ();
    void *responder = zmq_socket (context, ZMQ_SUB);
    int rc=zmq_connect (responder, "tcp://localhost:5555");
    assert(rc==0);
    rc = zmq_setsockopt (responder, ZMQ_SUBSCRIBE,NULL,0);
    assert (rc == 0);
    
    fp=fopen("sub","w");
    
    /*
    char message[1020];
    zmq_recv (responder, message, 1000, 0);
    gettimeofday(&tve,NULL);
	fprintf(fp,"%ld  %ld\n",tve.tv_sec,tve.tv_usec);
	*/
		
    
    
    for(j=0;j<1000;j++){
        char message[1000];
        if(zmq_recv (responder, message, 1000, 0)==1000)
        {
            //printf("%s\n",zmq_strerror(errno));
			gettimeofday(&tve,NULL);
	       fprintf(fp,"%ld  %ld\n",tve.tv_sec,tve.tv_usec);
       }
        
        
    }

    
    fclose(fp);
    zmq_close (responder);
    zmq_ctx_destroy (context);
    return 0;
}
