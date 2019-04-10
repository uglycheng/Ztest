#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>
#include <sys/time.h>

#define NUMBER_OF_MESSAGES 10000
#define LENGTH_OF_MESSAGES 1000

int main (void)
{
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);
    zmq_connect (requester, "tcp://192.168.43.122:5555");
    
    
    struct timeval tve;
    FILE *SendTimeRecorder, *RecvTimeRecorder;
    SendTimeRecorder=fopen("send","w");
    RecvTimeRecorder=fopen("recv","w");
    
    sleep(10); //reserve time to start "top" 
    
    for(int j=0;j<NUMBER_OF_MESSAGES;j++)
    {
		
	
	zmq_send (requester, "NWLRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCOQHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCACEHCHZVFRKMLNOZJKPQPXRJXKITZYXACBHHKICQCOENDTOMFGDWDWFCGPXIQVKUYTDLCGDEWHTACIOHORDTQKVWCSGSPQOQMSBOAGUWNNYQXNZLGDGWPBTRWBLNSADEUGUUMOQCDRUBETOKYXHOACHWDVMXXRDRYXLMNDQTUKWAGMLEJUUKWCIBXUBUMENMEYATDRMYDIAJXLOGHIQFMZHLVIHJOUVSUYOYPAYULYEIMUOTEHZRIICFSKPGGKBBIPZZRZUCXAMLUDFYKGRUOWZGIOOOBPPLEQLWPHAPJNADQHDCNVWDTXJBMYPPPHAUXNSPUSGDHIIXQMBFJXJCVUDJSUYIBYEBMWSIQYOYGYXYMZEVYPZVJEGEBEOCFUFTSXDIXTIGSIEEHKCHZDFLILRJQFNXZTQRSVBSPKYHSENBPPKQTPDDBUOTBBQCWIVRFXJUJJDDNTGEIQVDGAIJVWCYAUBWEWPJVYGEHLJXEPBPIWUQZDZUBDUBZVAFSPQPQWUZIFWOVYDDWYVVBURCZMGYJGFDXVTNUNNESLSPLWUIUPFXLZBKNHKWPPANLTCFIRJCDDSOZOYVEGURFWCSFMOXEQMRJOWRGHWLKOBMEAHKGCCNAEHHSVEYMQPXHLRNUNYFDZRHBASJEUYGAFOUBUTPNIMUWFJQSJXVKQDORXXVRWCTDSNEOGVBPKXLPGDIRBFCRIQIFPGYNKRREFXSNVUCFTPWCTGTWMXNUPYCFGCUQUNUBLMOIITNCKLEFSZBEXRAMPETVHQNDDJEQVUYGPNKAZQFRPJVOAXDPCWMJOBMSKSKFOJNEWXGXNNOFWL", 1000, 0);
        gettimeofday(&tve,NULL);
        fprintf(SendTimeRecorder,"%ld  %ld\n",tve.tv_sec,tve.tv_usec);
        
        
       
        char Message[LENGTH_OF_MESSAGES];
        if(zmq_recv(requester,Message,1000,0) == 1000)
        {
		gettimeofday(&tve,NULL);
		fprintf(RecvTimeRecorder,"%ld  %ld\n",tve.tv_sec,tve.tv_usec);
	}
    }
    
    fclose(SendTimeRecorder);
    fclose(RecvTimeRecorder);
    
    zmq_close (requester);
    zmq_ctx_destroy (context);
    return 0;
}
