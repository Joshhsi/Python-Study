# -*- coding: utf-8 -*-
# Download-Install (Python 3 version)123

from urllib.request import urlopen
import subprocess as sp
DOWNLOAD_URL = "https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe"
DOWNLOAD_DST = "C:\Temp\python.exe"

def download(url, dst_file):
    content = urlopen(url).read()
    outfile = open(dst_file, "wb")
    outfile.write(content)
    outfile.close()

def install():
    process = sp.Popen("C:\Temp\python .exe /quiet", shell=True)
    process.wait()
def main():
    download(DOWNLOAD_URL, DOWNLOAD_DST)
    install()
if __name__ == "__main__":
    main()