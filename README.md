# curl-exporter
I made it for testing proxy availability
# NOTE
change this line with your proxy ip and port :
result = os.popen("curl https://www.youtube.com/ -x IP:PORT -I | head -n 1 | awk '{print $2}'").read()
