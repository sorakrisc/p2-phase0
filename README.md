# p2-phased0

James u5880068
Fon   u5880077

It operates on the command-line. You interact with it using a command-line interface (CLI). The program
will be run as follows (don't forget to chmod +x):
    ./punch -n <numRequests> -c <maxConcurrent> <url>

Explanation: This program will make a total of numRequests requests, but the number of concurrent
requests at a moment is at most maxConcurrent. The target service to connect to is url. This is a
well-formed URL, though it may specify a port different from the default.

clients(the program)
_______________________________
\    //\    //\    //\    //
 \  //  \  //  \  //  \  //      TCP SOCKET
  \//    \//    \//    \//
_______________________________
server

MY NOTE:
run file with time
time ./punch -n 100000 -c 100 http://lgu1.fishcluster.local:9000/fire

Upload file to web
scp -P 2207 punch u5880068@10.27.8.20:~/