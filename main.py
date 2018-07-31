#Import of necessary modules
#The subprocess module allows to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import subprocess
import sys

returnCode1 = subprocess.call(["pytest", "/home/polina/tests", "--log-file=/home/polina/fileForLogs", "--log-format=%(asctime)s %(levelname)s %(message)s", "--log-date-format=%Y-%m-%d %H:%M:%S", "-s", "--disable-warnings"])

#Print the return code of the pytest process
print("A return code of all the pytest process: ", returnCode1)
