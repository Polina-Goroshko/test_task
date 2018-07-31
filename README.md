<b>Task</b>: design a set of test cases for owner/permission/content modification testing of NFS4 file system. 
Implement designed test cases as testing application (test suite). E.g. all tests are stored in “tests” folder 
and there is “main” file which run all tests and produces an output.

<b>Test cases</b>: https://kb.epam.com/display/FLKMWD/Test+task+documentation%3A+test+cases

<b>Necessary Python versions</b>: Python 3.5.2, pytest-3.6.4, py-1.5.4, pluggy-0.7.1

<b>Necessary environment</b>: a Linux-based computer (it should be a NFS-server), a Linux-based virtual machine (it should be a NFS-client) installed on it. They should be connected via a network. A Linux-based computer (a NFS-server) should have ssh. A Linux-based virtual machine should have ssh and 2 network adapters (NAT and a Host-only adapter named vboxnet0). A programme should be executed on a Linux-based computer (a NFS-server). 

<b>Necessary steps for NFS installation</b>:
  1. Install NFS on both a server (a Linux-based computer) and a client (a Linux-based virtual machine). On Ubuntu 16.04 (for example) you can do it with a command "sudo apt install nfs-kernel-server nfs-common"
  2. Check (on both a server and a client) if a NFS-server is correctly installed. You can do it with a command "rpcinfo -p | grep nfs"
  3. Check (on both a server and a client) if NFS is supported on a kernel level. You can do it with a command "cat /proc/filesystems | grep nfs". If it is not supported on a kernel level, run a command "modprobe nfs" to load a kernel's module manually


<b>Necessary steps for a programme execution</b>: 
  1. Prepare a Linux-based computer (as a NFS-server) and a Linux-based virtual machine (as a NFS-client) according with a necessary environment described above.  
  2. On a server (a Linux-based computer) create a directory /home/polina/Music
  3. On a server (a Linux-based computer) move a directiry named "tests" and a main.py file to /home/polina/Music
  4. On a server (a Linux-based computer) create a file /home/polina/fileForLogs. It is needed for storing logs
  5. On a server (a Linux-based computer) in /home/polina/Music run a command "python3 ./main.py"
  
 <b>Additional information</b>:
 When a command "python3 ./main.py" will be successfully run on a Linux-based computer (as a NFS-server) it will be asked (for 3 times. Each for an implemented test case. All in all there are 3 implemented test cases) to write some information to a standard input. Client IP means an IP (in my case enp0s8 was used) of a Linux-based virtual machine (a NFS-client). Client port - means write down yours (of a Linux-based virtual machine (a NFS-client)) if specified, if not - write down 22 (it is a default). Client user - means a user on a Linux-based virtual machine (a NFS-client), but not root. Client password - means a password of a user on a Linux-based virtual machine (a NFS-client). Server IP - means an IP (vboxnet0) of a Linux-based computer (a NFS-server).

<b>Logs can be checked here</b>: /home/polina/fileForLogs (on a server (a Linux-based computer))

