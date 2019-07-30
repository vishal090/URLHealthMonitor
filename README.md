# URLHealthMonitor

The URLHealthMonitor program is a python script that extracts the health check parameters from a URL and presents in a human readable format. This python script is automated and runs every 10 minutes and saves the result in a file. The resulted file can be further analyzed and important decisions can be made based on the health check parameters. The output file can be attached in an email and send it to IT analyst for further analysis.

<li>The name of the python script is - 'URLHealthMonitor.py' </li>
<li>The shell script which runs the above python script at following intervals - 'test.sh'</li>
<li>The output file which gets attached in an email - 'thread_count.txt'</li>

# How to install

<li>Install python3.6 on your Linux system using - sudo yum install -y python36u python36u-libs python36u-devel python36u-pip</li>
<li>Check the version of Python installed using - python3.6 -V</li>

# How to run the script

<li>Place the python script 'URLHealthMonitor.py' inside some directory, say - /root/environments/python_progs/URLHealthMonitor.py</li>
<li>Place the shell script 'test.sh' inside the same directory as the python script above</li>
<li>Make the 'test.sh' script as executable by providing the permission as - chmod +x test.sh</li>
<li>Run the shell script from terminal using - ./test.sh</li>

<h5><strong>Note</strong></h5>
<p>To terminate the script press Ctrl+C from terminal.</p>
