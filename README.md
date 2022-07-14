# CUCKOO SANDBOX AUTO REPORT
![](https://user-images.githubusercontent.com/50067697/178905264-0e466a9a-be32-4698-a6c7-94eb55119a05.gif)

Before starting, you should install the Cuckoo Sandbox.   
Cuckoo Sandbox Github : <https://github.com/cuckoosandbox>
#   
This is a Crawler to get Cuckoo Sandbox Report autometically.   
You can get the report to JSON.   

* __First, you should install Library for execute Crawler.__
```
pip install selenium
pip install chromedriver-autoinstaller
``` 
* __Second, set your environment infomation.__  
``` 
#Cuckoo Sandbox path is usually /home/"your_name"/.cuckoo, but you should check this path.
path = '/home/ubuntu/.cuckoo/storage/analyses/' + str(file_count) + '/reports/report.json'
``` 
* __Third, you should insert the malware path in "your_file_path"__

Optionally you can send the report information to database using SQL.
