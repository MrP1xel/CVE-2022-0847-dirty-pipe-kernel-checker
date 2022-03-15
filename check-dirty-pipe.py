#!/bin/python3
import platform
import sys

if len(sys.argv) < 2:
 kernel_version = (platform.release())
else:
 kernel_version = sys.argv[1]


def is_kernel_vulnerable(kernel_version):
 kernel1 = int((kernel_version.split("-")[0].split("."))[0])
 kernel2 = int((kernel_version.split("-")[0].split("."))[1])
 kernel3 = int((kernel_version.split("-")[0].split("."))[2])
 kernel= (kernel1,kernel2,kernel3)
 vulnerable = True
 if kernel[0] < 5:
  vulnerable = False
 else:
  if kernel[0] == 5 and kernel[1] < 8:
   vulnerable = False
  if kernel[0] == 5 and kernel[1] == 10 and kernel[2] >= 102:
   vulnerable = False
  if kernel[0] == 5 and kernel[1] == 15 and kernel[2] >= 25:
   vulnerable = False
  if kernel[0] == 5 and kernel[1] == 16 and kernel[2] >= 11:
   vulnerable = False
 return vulnerable 

print("Is your system vulnerable to CVE: ", is_kernel_vulnerable(kernel_version))
