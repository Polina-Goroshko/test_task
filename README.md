<b>Task</b>: design a set of test cases for owner/permission/content modification testing of NFS4 file system. 
Implement designed test cases as testing application (test suite). E.g. all tests are stored in “tests” folder 
and there is “main” file which run all tests and produces an output.

<b>Test cases</b>: https://kb.epam.com/display/FLKMWD/Test+task+documentation%3A+test+cases

<b>Necessary Python versions</b>: Python 3.5.2, pytest-3.6.4, py-1.5.4, pluggy-0.7.1

<b>Necessary environment</b>: a Linux-based computer (it should be a NFS-server), a Linux-based virtual machine (it should be a NFS-client) installed on it. They should be connected via a network. A Linux-based computer (a NFS-server) should have ssh. A Linux-based virtual machine should have ssh and 2 network adapters (NAT and a Host-only adapter named vboxnet0 (by default)). A programme should be executed on a Linux-based computer (a NFS-server). 

<b>Necessary steps for NFS installation</b>:
  1. To install NFS on both a server (a Linux-based computer) and a client (a Linux-based virtual machine) on Ubuntu 16.04 (for example) you can run a command "sudo apt install nfs-kernel-server nfs-common"
  2. Check (on both a server and a client) if a NFS-server is correctly installed. You can do it with a command "rpcinfo -p | grep nfs"
  3. Check (on both a server and a client) if NFS is supported on a kernel level. You can do it with a command "cat /proc/filesystems | grep nfs". If it is not supported on a kernel level, run a command "modprobe nfs" to load a kernel's module manually


<b>Necessary steps for a programme execution</b>: 
  1. Prepare a Linux-based computer (as a NFS-server) and a Linux-based virtual machine (as a NFS-client) according with a necessary environment described above.  
  2. Download a /tests directory and a main.py file 
  3. Paste them in one directory
  4. In a directory with a */tests directory and a main.py file open a terminal. Run there "python3 ./main.py"
  
 <b>Additional information</b>:
 When a command "python3 ./main.py" will be successfully run on a Linux-based computer (as a NFS-server) it will be asked (for 3 times. Each for an implemented test case. All in all there are 4 implemented test cases) to write some information to a standard input. Client IP means an IP (in my case enp0s8 was used) of a Linux-based virtual machine (a NFS-client). Client port - write down yours (of a Linux-based virtual machine (a NFS-client)) if specified, if not - write down 22 (it is a default). Client user - means a user on a Linux-based virtual machine (a NFS-client), but not root. Client password - means a password of a user on a Linux-based virtual machine (a NFS-client). Server IP - means an IP (vboxnet0) of a Linux-based computer (a NFS-server). There is a timeout (2 minutes) in the code after the main activity of each test fuction. It was made for the ability to check correctness of a test manually. During the timeout we can manually go to our virtual machine (a NFS-client) and check if a file is created or not, for example.
 
<b>Logs can be checked here</b>: /currWorkDir/dirWithTests/fileForLogs (on a server (a Linux-based computer), where currWorkDir means your cuurent working directory, dirWithTests means a directory called "tests", where there are all implemented test cases, fileForLogs it is just a name of file, where logs will be stored.

