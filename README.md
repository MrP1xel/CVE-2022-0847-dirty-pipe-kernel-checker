# CVE-2022-0847-dirty-pipe-kernel-checker
Python script to check if your kernel is vulnerable to Dirty pipe CVE-2022-0847

You can execute directly the script on your system and it will find your kernel version

But you can execute the script with as argument a kernel version to check (3 digit kernel version, like 5.10.103)

./check-dirty-pipe.py 5.10.103

and it will print if this version is vulnerable or not:
Is your system vulnerable to CVE:  False
