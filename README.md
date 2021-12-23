# ip-magic
Python3 script to generate IP Address Blocks 


**General Usage**

```bash
usage: ip-block-generator.py [-h] [-r READ] [-w WRITE] [-s START] [-e END] [-o OUTPUT]

Generate IP Address Blocks Based on Start and End IP Address

optional arguments:
  -h, --help            show this help message and exit
  -r READ, --read READ  .csv input
  -w WRITE, --write WRITE
                        Write result to File Default: False
  -s START, --start START
                        IP Address that Starts the Block Range
  -e END, --end END     IP Address that Ends the Block Range
  -o OUTPUT, --output OUTPUT
                        File to write to
```

**Generate a Block Of IP Address based on a Start & End Range**

```bash
python3 ip-block-generator.py -s 5.83.240.0 -e 5.83.255.255  
```

Example Output
```
.........
5.83.255.243
5.83.255.244
5.83.255.245
5.83.255.246
5.83.255.247
5.83.255.248
5.83.255.249
5.83.255.250
5.83.255.251
5.83.255.252
5.83.255.253
5.83.255.254
[*] Generated 4095 IP Adresses.

```

**Generate a Block Of IP Address based on a Start & End Range and Write it to a file in to ``/output`` directory**

```bash
python3 ip-block-generator.py -s 5.83.240.0 -e 5.83.255.255 -w true -o myFile.txt 


```

Example Output
```
[*] Generated 4095 IP Adresses. File Written to /home/kali/scripts/ip-magic/output/myFile.txt

```


**Generate IP Blocks for a List of IP ranges**

```bash
python3 ip-block-generator.py -r ip.ie.csv   

```
The Output of this command is always written to a file in the output directory the naming convention is ```${owner}.{assigned}``` i.e. ```VodafoneIrelandLimited.22-06-07``` 


### Notes


#### CSV File Processing 

csv files must be stored in the ```/csv``` directory of this project. If you are planning to read from .csv files
ensure that the files have the appropriate headers ```start,end,total,assigned,owner```. Below is an example of a valid ```.csv``` file that can be processed by this app. 

**Example CSV File**

```csv
start,end,total,assigned,owner
5.83.240.0,5.83.255.255,4096,15-06-12,Eurona-Brisknet Ltd
5.179.32.0,5.179.63.255,8192,07-08-12,Virgin Media Ireland Limited
31.13.64.0,31.13.127.255,16384,18-04-11,Facebook Ireland Ltd
31.200.128.0,31.200.191.255,16384,28-04-11,Three Ireland (Hutchison) limited
37.228.192.0,37.228.255.255,16384,11-04-12,Virgin Media Ireland Limited
46.7.0.0,46.7.255.255,65536,06-09-10,Virgin Media Ireland Limited
46.22.128.0,46.22.143.255,4096,25-11-10,Blacknight Internet Solutions Limited
```


#### Output Files

All output files for this app are written to the projects ```/output``` directory if you want to do some ```magic``` around 
writing files to your custom location its better to just pipe the output to your desired file locations.   

**example**

```bash
python3 ip-block-generator.py -s 5.83.240.0 -e 5.83.255.255  > your/path/way/to/the/file/file.name

```
