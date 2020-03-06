# -*- coding: utf-8 -*-
# Download-Install (Python 3 version)

from urllib.request import urlopen
import subprocess as sp
DOWNLOAD_URL = "https://cdn1.evernote.com/win6/public/Evernote_6.23.2.8859.exe"
DOWNLOAD_DST = "C:\Temp\evernote.exe"
def download(url, dst_file):
    content = urlopen(url).read()
    outfile = open(dst_file, "wb")
    outfile.write(content)
    outfile.close()
def install(prog):
    process = sp.Popen("C:\Temp\evernote.exe /quiet", shell=True)
    process.wait()
def main():
    download(DOWNLOAD_URL, DOWNLOAD_DST)
    install(DOWNLOAD_DST)
if __name__ == "__main__":
    main()