from http.server import BaseHTTPRequestHandler


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
