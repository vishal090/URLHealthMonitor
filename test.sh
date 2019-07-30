rm -f thread_count.txt
while( true ); do
  /root/environments/python36/bin/python URLHealthMonitor.py >> thread_count.txt
  sleep 600
done
