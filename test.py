#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")

print()

a=cgi.FieldStorage()
cmd=a.getvalue("s")
output=subprocess.getoutput("sudo "+cmd)

print(output)
