from http.server import HTTPServer, BaseHTTPRequestHandler
from ssl import SSLContext, PROTOCOL_TLS_SERVER


class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        content_length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(content_length)
        print(data.decode())


if __name__ == "__main__":
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()
    address = getenv("WEBHOOK_ADRESS")
    certfile = getenv("WEBHOOK_CERTFILE")
    keyfile = getenv("WEBHOOK_KEYFILE")

    server = HTTPServer((address, 443), WebhookHandler)
    context = SSLContext(PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile, keyfile)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    print("Running...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print("Closed")
