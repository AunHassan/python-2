from urllib.request import Request, urlopen
from wsgiref import headers
url = "http://olympus.realpython.org/profiles"
domain = "http://olympus.realpython.org"
source_code = urlopen(
    Request(url,headers = {"user-Agent":"Mozilla/5.0"})
)
source = source_code.read().decode("utf-8")
print(source)
ref = source.find("href")
for i in range(source.count("href")):
    
    ref_start = source.find('"',ref)
    ref_end = source.find('"',ref_start+1)
    print(ref_start,ref_end)
    url1 = (domain+source[ref_start+1:ref_end])
    print(url1)
    ref = source.find("href",ref_end)
    source_code1 = urlopen(
        Request(url1,headers = {"user-Agent":"Mozilla/5.0"}))
    
    source1 = source_code1.read().decode("utf-8")
    print(source1,"\n-------------------------------------------------------------------------\n")
