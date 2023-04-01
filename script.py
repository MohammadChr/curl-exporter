import os
import time
from prometheus_client import start_http_server, Gauge

g = Gauge('curl_result', 'Result of curl command')

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9998)

    while True:
        result = os.popen("curl https://www.youtube.com/ -x IP:PORT -I | head -n 1 | awk '{print $2}'").read()
        g.set(result)
        time.sleep(120)
