# Test how docker works with restart option
## Steps:
1. Start the container
2. Open a console, ane watch status with: 'watch docker ps -a'
3. On the host, input following script to test with 
   normal quit, exit with error, stop container and docker service restart: 
  3.1 -> echo 'GET /quit HTTP/1.1' | nc localhost 8000
  3.2 -> echo 'GET /error HTTP/1.1' | nc localhost 8000
  3.3 -> docker stop python-http-server
  3.4 -> sudo service docker restart

 
  
