# Python-net-programming
Programming Assignment: Understanding Web Caching --A simulation
Submission: November 7th, 11.59 PM.
Goal: To understand the impact of web cache and implementation issues.
Project Deliverable: A network client that generates HTTP requests and a server that
simulates a real web server as well as a proxy web server
Specification 1: The client should generate around 100-1000 (not necessarily
unique/distinct) URL requests for each experiment in increments of 100: 100, 200,
300, 400,..., 1000. The client program should measure the time from the request
submission to the time that the entire response was received. The following table
should be displayed:
#Requests | Avg. Response Time | Median Response Time
100
200
300
..
...
Specification 2: The web server receives requests from the client and serves the
requests in the following manner.
Direct Mode: In Direct mode, the Web server acts like a distant webserver and takes
some "time" before responding to the client. The time that the server takes is to
simulate the real-life scenario of dealys like network delays, propagation delays
and processing delays.
Proxy Mode: In Proxy mode, the web server parses the HTTP request to generate the
query string. The web server then consults an index (the web cache) to see if that
request was previously made. If the request was previously made, then the web
server finds a match and responds to the client immediately. If the request not
previously made the web server adds the request to the cache after serving the
request in Direct mode (and adding all the necessary delays as well). For the
purposes of the experiments you can assume that the cache is infinite.
#Request | Mode of Response | Time Taken
1
2
3
...
...
200
Important implementation challenges to consider:
1. How to simulate the randomness of the web server (proxy vs direct mode)?
2. How to implement the web cache?
(Hint: DBMS course)
3. Different libraries have different time overheads. You can explore implementing
lookup etc using first principles and see the difference.
Deliverables
1. client<last4digitsrollnumber>.py and server<last4digitsrollnumber>.pyE.g., client0201.py, server0201.py
2. Any README file.
3. If you have made multiple implementations of the web cache you can submit either
multiple files as follows: client<last4digitsrollnumber>-1.py
E.g., client0201-1.py
and write down in the README file as to what you have done in such a file.
4. Hard deadline and file naming conventions. No other submission format is allowed
(zip, jpeg, pdf, doc etc).
5. Submission form will be shared with you. Please follow submission instructions
carefully.
