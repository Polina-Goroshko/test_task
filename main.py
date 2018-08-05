#Import of necessary modules
#The subprocess module allows to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import subprocess
import sys
import os

currWorkDir = str(os.getenv("PWD"))

#Print the current working directory
print("Current working directory:", currWorkDir)

#Necessary variables
dirWithTests = "/tests"
fileWithLogsShortPath = "/fileForLogs"
fileWithLogsLongPath = currWorkDir + dirWithTests + fileWithLogsShortPath

#Print the name of a file where logs will be stored
print("Logs are stored here:", fileWithLogsLongPath)

#Create a file where logs will be stored
with open(fileWithLogsLongPath, 'w') as f:
    pass

#Run tests' execution
returnCode1 = subprocess.call(["pytest", "%s%s" % (currWorkDir, dirWithTests), "-s", "--log-file=%s" % (fileWithLogsLongPath), "--log-format=%(asctime)s %(levelname)s %(message)s", "--log-date-format=%Y-%m-%d %H:%M:%S", "--disable-warnings"])

#Print the return code of the pytest process
print("A return code of all the pytest process: ", returnCode1)
