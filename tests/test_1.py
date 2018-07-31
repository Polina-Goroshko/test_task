#Import of necessary modules
import sys
import time

#The subprocess module allows to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import subprocess

#Paramiko is a Python implementation of the SSHv2 protocol, providing both client and server functionality. While it leverages a Python C #extension for low level cryptography, Paramiko itself is a pure Python interface around SSH networking concepts.
import paramiko

#The logging module defines functions and classes which implement a flexible event logging system for applications and libraries
import logging

#logging.basicConfig does basic configuration for the logging system. level set the root logger level to the specified level
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

#Getting necessary variables
print(" ")
clientIP = input("Client IP:")
clientPort = input("Client port:")
clientPort=int(clientPort)
clientUser = input("Client user:")
clientPassword = input("Client password:")
serverIP = input("Server IP:")

#Necessary constant variables
dirForExportName="/home/dirForTest/"
#ro -  disallow any request which changes the filesystem
#sync - the NFS server will not reply to requests before changes made by previous requests are written to disk
#no_subtree_check - this  option  disables  subtree  checking. If a subdirectory of a filesystem is exported, but the whole filesystem isn't then whenever a NFS request arrives, the server must  check  not  only  that  the  accessed  file is in the appropriate filesystem but also that it is in the exported tree. This check is called the subtree_check
paramForExport = "(ro,sync,no_subtree_check)"

def setup():
	#Return a logger with the specified name. All calls to this function with a given name return the same logger instance
	log1 = logging.getLogger('logger')
	#1. On a server create a directory /home/dirForTest/ with a command "sudo mkdir /home/dirForTest/"
	try:
		log1.info("Trying to execute 'sudo mkdir /home/dirForTest/' on a server")
		#Execute a child program in a new process
		proc2 = subprocess.Popen(["sudo", "mkdir", "/home/dirForTest/"], stdin=subprocess.PIPE)
		proc2.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode2=proc2.wait()
		log1.info("Return code of 'sudo mkdir /home/dirForTest/' on a server: %s", returnCode2)

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		#“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'mkdir /home/dirForTest/' failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'mkdir /home/dirForTest/' failed. ValueError")

	#A high-level representation of a session with an SSH server. This class wraps Transport, Channel, and SFTPClient to take care of most aspects of authenticating and opening channels
	client = paramiko.SSHClient()
	#Set policy to use when connecting to servers without a known host key. A policy is a “policy class” (or instance thereof) namely some subclass of MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy, WarningPolicy, or a user-created subclass.
	#A host key is known when it appears in the client object’s cached host keys structures
	#AutoAddPolicy() - policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
	#HostKeyes object is a representation of an OpenSSH-style “known hosts” file
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		#Connect to an SSH server and authenticate to it. The server’s (client in our case) host key is checked against the system host keys (see load_system_host_keys) and any local host keys (load_host_keys). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see set_missing_host_key_policy). The default policy is to reject the key and raise an SSHException
		client.connect(hostname=clientIP, port=clientPort, username=clientUser, password=clientPassword)
	#SSHException - exception raised by failures in SSH2 protocol negotiation or logic errors
	except paramiko.ssh_exception.SSHException:
		log1.error("SSHException: can't establish an SSH connection with a server")
	
	log1.info("Connect with client successful")	
	

	#-----1.1 On a server change permissions on a directory /home/dirForTest/ with a command "sudo chmod ugo+rwx /home/dirForTest/"
	try:
		log1.info("Trying to execute 'sudo chmod ugo+rwx /home/dirForTest/' on a server")
		#Execute a child program in a new process
		proc7 = subprocess.Popen(["sudo", "chmod","ugo+rwx", "/home/dirForTest/"], stdin=subprocess.PIPE)
		proc7.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode7=proc7.wait()
		log1.info("Return code of 'sudo chmod ugo+rwx /home/dirForTest/' on a server: %s", returnCode7)

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		#“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'sudo chmod ugo+rwx /home/dirForTest/' failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'sudo chmod ugo+rwx /home/dirForTest/' failed. ValueError")

	#A high-level representation of a session with an SSH server. This class wraps Transport, Channel, and SFTPClient to take care of most aspects of authenticating and opening channels
	client = paramiko.SSHClient()

	#Set policy to use when connecting to servers without a known host key. A policy is a “policy class” (or instance thereof) namely some subclass of MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy, WarningPolicy, or a user-created subclass.
	#A host key is known when it appears in the client object’s cached host keys structures
	#AutoAddPolicy() - policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
	#HostKeyes object is a representation of an OpenSSH-style “known hosts” file
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		#Connect to an SSH server and authenticate to it. The server’s (client in our case) host key is checked against the system host keys (see load_system_host_keys) and any local host keys (load_host_keys). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see set_missing_host_key_policy). The default policy is to reject the key and raise an SSHException
		client.connect(hostname=clientIP, port=clientPort, username=clientUser, password=clientPassword)

	#SSHException - exception raised by failures in SSH2 protocol negotiation or logic errors
	except paramiko.ssh_exception.SSHException:
		log1.error("SSHException: can't establish an SSH connection with a server")
	
	log1.info("Connect with client successful")	

	#2. Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
	stdin, stdout, stderr = client.exec_command('mkdir /home/$USER/dirForMount/')

	#Return the exit status from the process on the server. This is mostly useful for retrieving the results of an exec_command. If the command hasn’t finished yet, this method will wait until it does, or until the channel is closed. If no exit status is provided by the server, -1 is returned.
	if stdout.channel.recv_exit_status() != 0:
		log1.error("A command 'mkdir /home/$USER/dirForMount on a client failed")	
	else:
		log1.info("A command 'mkdir /home/$USER/dirForMount on a client passed")

	#Close this SSHClient and its underlying Transport. An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates, and then creates stream tunnels, called channels, across the session
	client.close()
	log1.info("Connect with client closed")
	
	#3. On a server clean a /etc/exports file
	try:
		#Execute a child program in a new process
		proc3 = subprocess.Popen(["sudo", "cp", "/dev/null", "/etc/exports"], stdin=subprocess.PIPE)
		proc3.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode3=proc3.wait()
		log1.info("Return code of 'cp /dev/null /etc/exports on a server: %s", returnCode3)
		#Check a return code
		if (returnCode3 != 0):
			log1.error("A command 'cp /dev/null /etc/exports' on a server failed")

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'cp /dev/null /etc/exports' failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'cp /dev/null /etc/exports' failed. ValueError")

	log1.info("/etc/exports was successfully cleared")

	#4. On a server assemble a name of a directory for export, a clientIP value and necessary options (ro, which means a read-only mode) into a string variable called permForExport
	permForExport = dirForExportName + " " + clientIP  + paramForExport
	try:
		permForExport
	#NameError raised when a local or global name is not found. 
	except NameError:
		log1.error("permForExport is not created. NameError")

#create fileTest

#5. On a server create fileTest
	try:
		#Execute a child program in a new process
		proc4 = subprocess.Popen(["sudo", "touch", "/home/dirForTest/fileTest"], stdin=subprocess.PIPE)
		proc4.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode4=proc4.wait()
		log1.info("Return code of 'touch /home/dirForTest/fileTest' on a server: %s", returnCode4)
		#Check a return code
		if (returnCode4 != 0):
			log1.error("A command 'touch /home/dirForTest/fileTest' on a server failed")

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'touch /home/dirForTest/fileTest' failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'touch /home/dirForTest/fileTest' failed. ValueError")

#6. On a server create a someFile. The aim - not empty directory for
	try:
		#Execute a child program in a new process
		proc5 = subprocess.Popen(["sudo", "touch", "/home/dirForTest/someFile"], stdin=subprocess.PIPE)
		proc5.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode5=proc5.wait()
		log1.info("Return code of 'touch /home/dirForTest/someFile' on a server: %s", returnCode5)
		#Check a return code
		if (returnCode5 !=0):
			log1.error("A command 'touch /home/dirForTest/someFile' on a server failed. Return code is NOT 0")
		
	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'touch /home/dirForTest/someFile' on a server failed. OSError")
	
	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'touch /home/dirForTest/someFile' on a server failed. ValueError")

#8. write permForExports, which contains permissions, to /home/dirForTest/fileWithRights

	file1 = open("/home/dirForTest/fileWithRights", "w")
	file1.write(str(permForExport))
	file1.close()

#9. cp /home/dirForTest/fileWithRights to /etc/exports

	try:
		#Execute a child program in a new process
		proc8 = subprocess.Popen(["sudo", "cp", "/home/dirForTest/fileWithRights", "/etc/exports"], stdin=subprocess.PIPE)
		proc8.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode8=proc8.wait()
		log1.info("Return code of 'cp /home/dirForTest/fileWithRights /etc/exports' on a server: %s", returnCode8)
		#Check a return code
		if (returnCode8 !=0):
			log1.error("A command 'cp /home/dirForTest/fileWithRights /etc/exports' on a server failed. Return code is NOT 0")

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'cp /home/dirForTest/fileWithRights /etc/exports' on a server failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'cp /home/dirForTest/fileWithRights /etc/exports' on a server failed. ValueError")
	
	log1.info("/home/dirForTest/fileWithRights is successfully coped to /etc/exports")


#10. On a server with a command "sudo exportfs -a" update an export table

	try:
		#Execute a child program in a new process
		proc9 = subprocess.Popen(["sudo", "exportfs", "-a"], stdin=subprocess.PIPE)
		proc9.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode9=proc9.wait()
		log1.info("Return code of 'sudo exportfs -a on a server: %s", returnCode9)
		#Check a return code
		if (returnCode9 != 0):
			log1.error("A command 'sudo exportfs -a' on a server failed. The exit status of a command is NOT 0")

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'sudo exportfs -a' on a server failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'sudo exportfs -a' on a server failed. ValueError")

	log1.info("A command 'sudo exportfs -a' on a server is successfully executed")


#11. On a client mount /dirForTest/, that is on a server, to /dirForMount/, that is on a client, with a command "sudo mount serverIP:/dirForTest/ /dirForMount/"
	
#A high-level representation of a session with an SSH server. This class wraps Transport, Channel, and SFTPClient to take care of most aspects of authenticating and opening channels
	client = paramiko.SSHClient()

	#Set policy to use when connecting to servers without a known host key. A policy is a “policy class” (or instance thereof) namely some subclass of MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy, WarningPolicy, or a user-created subclass.
	#A host key is known when it appears in the client object’s cached host keys structures
	#AutoAddPolicy() - policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
	#HostKeyes object is a representation of an OpenSSH-style “known hosts” file
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		#Connect to an SSH server and authenticate to it. The server’s (client in our case) host key is checked against the system host keys (see load_system_host_keys) and any local host keys (load_host_keys). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see set_missing_host_key_policy). The default policy is to reject the key and raise an SSHException
		client.connect(hostname=clientIP, port=clientPort, username=clientUser, password=clientPassword)

	#SSHException - exception raised by failures in SSH2 protocol negotiation or logic errors
	except paramiko.ssh_exception.SSHException:
		log1.error("SSHException: can't establish an SSH connection with a server")
	
	log1.info("Connect with client successful")
	log1.info("Begin mounting")
	#Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
	stdin, stdout, stderr = client.exec_command("echo %s | sudo -S mount %s:/home/dirForTest/ /home/$USER/dirForMount/" % (clientPassword, serverIP))
	log1.info("%s", stderr.read())	
	log1.info("Exit status of mounting %s", stdout.channel.recv_exit_status())
	
  #Return the exit status from the process on the server. This is mostly useful for retrieving the results of an exec_command. If the command hasn’t finished yet, this method will wait until it does, or until the channel is closed. If no exit status is provided by the server, -1 is returned.
	if stdout.channel.recv_exit_status() != 0:
		log1.error("A command 'echo %s | sudo -S mount %s:/home/dirForTest/ /home/$USER/dirForMount/" % (clientPassword, serverIP)' failed. The exit status of a command is NOT 0")	
	else:
		log1.info("A command 'echo %s | sudo -S mount %s:/home/dirForTest/ /home/$USER/dirForMount/" % (clientPassword, serverIP)' passed")

	#Close this SSHClient and its underlying Transport. An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates, and then creates stream tunnels, called channels, across the session
	client.close()
	log1.info("Connect with client closed")

	
def testTest1():
	log1 = logging.getLogger('logger')
	client = paramiko.SSHClient()

	#Set policy to use when connecting to servers without a known host key. A policy is a “policy class” (or instance thereof) namely some subclass of MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy, WarningPolicy, or a user-created subclass.
	#A host key is known when it appears in the client object’s cached host keys structures
	#AutoAddPolicy() - policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
	#HostKeyes object is a representation of an OpenSSH-style “known hosts” file
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		#Connect to an SSH server and authenticate to it. The server’s (client in our case) host key is checked against the system host keys (see load_system_host_keys) and any local host keys (load_host_keys). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see set_missing_host_key_policy). The default policy is to reject the key and raise an SSHException
		client.connect(hostname=clientIP, port=clientPort, username=clientUser, password=clientPassword)

	#SSHException - exception raised by failures in SSH2 protocol negotiation or logic errors
	except paramiko.ssh_exception.SSHException:
		log1.error("SSHException: can't establish an SSH connection with a server")

	log1.info("Connect with client successful")
	log1.info("Begin touch a file")
#12. Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
	stdin, stdout, stderr = client.exec_command("echo %s | sudo -S touch /home/$USER/dirForMount/cinema" % (clientPassword))
	log1.info("End touch a file")
	time.sleep(120)
	log1.info("%s", stderr.read())	
	log1.info("Exit status of touch a file %s", stdout.channel.recv_exit_status())

	#Return the exit status from the process on the server. This is mostly useful for retrieving the results of an exec_command. If the command hasn’t finished yet, this method will wait until it does, or until the channel is closed. If no exit status is provided by the server, -1 is returned.
	if stdout.channel.recv_exit_status() != 0:
		log1.error("A command 'echo %s | sudo -S touch /home/$USER/dirForMount/cinema" % (clientPassword)' failed. The exit status of a command is NOT 0")	
	else:
		log1.info("A command 'echo %s | sudo -S touch /home/$USER/dirForMount/cinema" % (clientPassword)' passed")

	log1.info("Exit status of 'echo %s | sudo -S touch /home/$USER/dirForMount/cinema" % (clientPassword)': %s ", stdout.channel.recv_exit_status())
	#Close this SSHClient and its underlying Transport. An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates, and then creates stream tunnels, called channels, across the session
	client.close()
	log1.info("connect with client closed")

	assert stdout.channel.recv_exit_status() != 0


def teardown():

	client = paramiko.SSHClient()
	log1 = logging.getLogger('logger')

	#Set policy to use when connecting to servers without a known host key. A policy is a “policy class” (or instance thereof) namely some subclass of MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy, WarningPolicy, or a user-created subclass.
	#A host key is known when it appears in the client object’s cached host keys structures
	#AutoAddPolicy() - policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
	#HostKeyes object is a representation of an OpenSSH-style “known hosts” file
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		#Connect to an SSH server and authenticate to it. The server’s (client in our case) host key is checked against the system host keys (see load_system_host_keys) and any local host keys (load_host_keys). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see set_missing_host_key_policy). The default policy is to reject the key and raise an SSHException
		client.connect(hostname=clientIP, port=clientPort, username=clientUser, password=clientPassword)

	#SSHException - exception raised by failures in SSH2 protocol negotiation or logic errors
	except paramiko.ssh_exception.SSHException:
		log1.error("SSHException: can't establish an SSH connection with a server")

	log1.info("Connect with client successful")
	
#13. Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
	stdin, stdout, stderr = client.exec_command("echo %s | sudo -S umount /home/$USER/dirForMount/" % (clientPassword))

	#Return the exit status from the process on the server. This is mostly useful for retrieving the results of an exec_command. If the command hasn’t finished yet, this method will wait until it does, or until the channel is closed. If no exit status is provided by the server, -1 is returned.
	if stdout.channel.recv_exit_status() != 0:
		log1.info("A command 'echo 'echo %s | sudo -S umount /home/$USER/dirForMount/" % (clientPassword)' failed. The exit status of a command is NOT 0. It is: %s", stdout.channel.recv_exit_status())	
	else:
		log1.info("A command 'echo %s | sudo -S umount /home/$USER/dirForMount/" % (clientPassword)' passed.")

	#Close this SSHClient and its underlying Transport. An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates, and then creates stream tunnels, called channels, across the session
	client.close()
	log1.info("Connect with client closed")

#14. Delete /home/dirForTest/' on a server
	try:
		#Execute a child program in a new process
		proc10 = subprocess.Popen(["sudo", "rm", "-rf", "/home/dirForTest/"], stdin=subprocess.PIPE)
		proc10.communicate()
		#Wait for child process to terminate. Set and return returncode attribute
		returnCode10=proc10.wait()
		log1.info("Return code of 'rm -rf /home/dirForTest/' on a server: %s", returnCode10)
		#Check a return code
		if (returnCode10 != 0):
			log1.error("A command 'rm -rf /home/dirForTest/' on a server failed. The exit status of a command is NOT 0")

	#OSError exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or 		“disk full” (not for illegal argument types or other incidental errors).	
	except OSError:
		log1.error("A command 'rm -rf /home/dirForTest/' on a server failed. OSError")

	#ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value
	except ValueError:
		log1.error("A command 'rm -rf /home/dirForTest/' on a server failed. ValueError")	
	
	client = paramiko.SSHClient()

	#Set policy to use when connecting to servers without a known host key. A policy is a “policy class” (or instance thereof) namely some subclass of MissingHostKeyPolicy such as RejectPolicy (the default), AutoAddPolicy, WarningPolicy, or a user-created subclass.
	#A host key is known when it appears in the client object’s cached host keys structures
	#AutoAddPolicy() - policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it
	#HostKeyes object is a representation of an OpenSSH-style “known hosts” file
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		#Connect to an SSH server and authenticate to it. The server’s (client in our case) host key is checked against the system host keys (see load_system_host_keys) and any local host keys (load_host_keys). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see set_missing_host_key_policy). The default policy is to reject the key and raise an SSHException
		client.connect(hostname=clientIP, port=clientPort, username=clientUser, password=clientPassword)

	#SSHException - exception raised by failures in SSH2 protocol negotiation or logic errors
	except paramiko.ssh_exception.SSHException:
		log1.error("Cannot establish an SSH connection with a server. SSHException")
	
	log1.info("Connect with client successful")
#15. Delete /home/$USER/dirForMount' on a client
	#Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
	stdin, stdout, stderr = client.exec_command('rm -rf /home/$USER/dirForMount')

	#Return the exit status from the process on the server. This is mostly useful for retrieving the results of an exec_command. If the command hasn’t finished yet, this method will wait until it does, or until the channel is closed. If no exit status is provided by the server, -1 is returned.
	if stdout.channel.recv_exit_status() != 0:
		log1.error("A command 'rm -rf /home/$USER/dirForMount' failed. The exit status of a command is NOT 0")	
	else:
		log1.info("A command 'rm -rf /home/$USER/dirForMount' passed")

	#Close this SSHClient and its underlying Transport. An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates, and then creates stream tunnels, called channels, across the session
	client.close()
	log1.info("Connect with client closed")
