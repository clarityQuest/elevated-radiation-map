"""
Simple development server for the geiger-map project.
Serves static files and handles database saves with automatic archiving.

Usage: python server.py
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json, os, shutil, sys

PORT = 8080
DB_PATH = 'database.json'
ARCHIVE_PATH = os.path.join('archive', 'database.json')


class Handler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        path = self.path.split('?')[0]
        if path == '/api/save':
            try:
                length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(length)
                data = json.loads(body.decode('utf-8'))

                # Validate basic structure
                if 'opengeiger' not in data or 'forum' not in data:
                    raise ValueError('Missing "opengeiger" or "forum" key')

                # Back up current database to archive/
                os.makedirs('archive', exist_ok=True)
                if os.path.exists(DB_PATH):
                    shutil.copy2(DB_PATH, ARCHIVE_PATH)

                # Write new database
                with open(DB_PATH, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

                og = len(data.get('opengeiger', []))
                fm = len(data.get('forum', []))
                print(f'  Saved database.json ({og} opengeiger, {fm} forum entries). Backup -> archive/database.json')

                self._json(200, {'ok': True})
            except Exception as e:
                print(f'  Save error: {e}')
                self._json(500, {'error': str(e)})
        else:
            self.send_response(404)
            self._cors()
            self.end_headers()

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def _json(self, code, obj):
        body = json.dumps(obj).encode('utf-8')
        self.send_response(code)
        self._cors()
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Suppress tile/asset noise, show only API and page requests
        path = args[0] if args else ''
        if any(x in path for x in ['.png', '.css', '.min.js', 'leaflet']):
            return
        print(' ', fmt % args)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('', PORT), Handler)
    print(f'Geiger Map server running at http://localhost:{PORT}')
    print(f'  Map:    http://localhost:{PORT}/')
    print(f'  Editor: http://localhost:{PORT}/editor.html')
    print('Press Ctrl+C to stop.\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
        sys.exit(0)
