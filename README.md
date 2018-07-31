Task: design a set of test cases for owner/permission/content modification testing of NFS4 file system. 
Implement designed test cases as testing application (test suite). E.g. all tests are stored in “tests” folder 
and there is “main” file which run all tests and produces an output.

Test cases: https://kb.epam.com/display/FLKMWD/Test+task+documentation%3A+test+cases

Necessary environment: Python 3.5.2, pytest-3.6.4, py-1.5.4, pluggy-0.7.1

Necessary steps for a programme execution: 
  1. Prepare a Linux-based computer (as a NFS-server) and a Linux-based virtual machine (as a NFS-client) installed on it
  2. NFS installed on both a server (a Linux-based computer) and a client (a Linux-based virtual machine). On Ubuntu 16.04 (for example) you can do it with a command "sudo apt install nfs-kernel-server nfs-common"
  3. Check (on both a server and a client) if a NFS-server is correctly installed. You can do it with a command "rpcinfo -p | grep nfs"
  4. Check (on both a server and a client) if NFS is supported on a kernel level. You can do it with a command "cat /proc/filesystems | grep nfs". If it is not supported on a kernel level, run a command "modprobe nfs" to load a kernel's module manually
  5. On a server (a Linux-based computer) create a directory /home/polina/Music
  6. On a server (a Linux-based computer) move a directiry named "tests" and a main.py file to /home/polina/Music
  7. On a server (a Linux-based computer) create a file /home/polina/fileForLogs. It is needed for storing logs
  8. On a server (a Linux-based computer) in /home/polina/Music run a command "python3 ./main.py"

Logs can be checked here: /home/polina/fileForLogs

