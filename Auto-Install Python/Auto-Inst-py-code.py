# -*- coding: utf-8 -*-
# Download-Install (Python 3 version)123

from urllib.request import urlopen
import subprocess as sp
DOWNLOAD_URL1 = r"https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe"
DOWNLOAD_DST1 = r"C:\Temp\python.exe"

DOWNLOAD_URL2 = r"https://aka.ms/win32-x64-user-stable"
DOWNLOAD_DST2 = r"C:\Temp\vscode.exe"

def download(url, dst_file):
    content = urlopen(url).read()
    outfile = open(dst_file, "wb")
    outfile.write(content)
    outfile.close()

def install():
    process = sp.Popen(r"C:\Temp\python.exe /quiet", shell=True)
    process = sp.Popen(r"C:\Temp\vscode.exe /quiet", shell=True)
    process.wait()
def main():
    download(DOWNLOAD_URL1, DOWNLOAD_DST1)
    download(DOWNLOAD_URL2, DOWNLOAD_DST2)
    install()
if __name__ == "__main__":
    main()