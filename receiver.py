from http.server import HTTPServer, BaseHTTPRequestHandler


class Hook(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        print("Webhook received:", body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    HTTPServer(("", 8000), Hook).serve_forever()
