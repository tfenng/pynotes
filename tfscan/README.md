# pycmd

## tfscan
Scan text files in one directory with specified file extension names, sum lines and file size as report info.


### Run commands samples

    ./tfscan.py /home/tom go
    
    ./tfscan.py /home/jerry go py
    
    ./tfscan.py /home/michey go py js

### Output sample
       .........
       4,825      254	src/github.com/temoto/robotstxt/google_test.go
       5,728      227	src/github.com/temoto/robotstxt/robotstxt.go
         906       36	src/github.com/temoto/robotstxt/scanner_test.go
       3,419      185	src/github.com/temoto/robotstxt/scanner.go
       7,102      269	src/github.com/temoto/robotstxt/parser.go
TOTAL: 33,353,748 bytes IN 1,455,884 lines IN 1,926 files


### About performance

It costs 5 seconds to scan about 50k text files / 18M lines/ 625Mb total-file-size.

(On my desktop PC: i5-7600K,  nvme SSD)


### Notice
change the first line if your python3 is not in the default path