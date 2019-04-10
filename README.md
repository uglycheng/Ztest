# Ztest
Some test about zeromq

最开始使用PUB-SUB模型在同一台树莓派上发送接收消息(WithSR)，但是因为吞吐速率相对于传输消息的时延快太多，PUB—SUB模型的SUB方无法接收到每条消息，
在接收到前一条后一条之间的时间段内PUB发出的消息被丢弃，不适合做测试。

改用PUSH—PUll模型(WithSR_PUSH-PULL),可行。

WithoutSR中没有消息的接收发送，其他的代码相同，与前面两个文件夹对比更好反应单纯消息队列的性能。

RMT在一台surface上的Ubuntu虚拟机与树莓派之间传递接收消息，用PUSH_PUll模型，但由于在两台设备上分开计时，有些问题。

RMT_Req-Rep由树莓派Request，surface接收后Reply，在树莓派上计时，Req与Rep之间的时间除以2。并统计内存CPU占用率。

  
  

