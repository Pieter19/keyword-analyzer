import argparse
import os

from keyword_analyzer.server import app

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Run server'
    )
    parser.add_argument('--port', '-p', help='use custom port', default=8001, type=int)
    parser.add_argument('--host', '-i', help='use custom host', default=None, type=str)
    args = parser.parse_args()
    port = args.port or os.environ.get('PORT')
    host = args.host or os.environ.get('HOST')

    app.run(host=host, port=port, debug=True)
