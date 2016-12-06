import TatumHandler
import SocketServer

PORT = 8000

Handler = TatumHandler.HTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

