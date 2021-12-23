# ip-block-generator

import csv
import os
import argparse

homedir =os.getcwd()

parser = argparse.ArgumentParser(description='Generate IP Address Blocks Based on Start and End IP Address')
parser.add_argument('-r','--read',   help='.csv input', type=str)
parser.add_argument('-w','--write',  help='Write result to File Default: False', default=False)
parser.add_argument('-s','--start',  help='IP Address that Starts the Block Range', type=str)
parser.add_argument('-e','--end',    help='IP Address that Ends the Block Range', type=str)
parser.add_argument('-o','--output', help='File to write to', type=str)

args = parser.parse_args()

read = True if args.read !=None  else False

inputfile = f"{homedir}/csv/{args.read}" if args.read !=None  else None

def verify_ip_address( start, end ):
	import socket, struct
	try:
		socket.inet_aton(start)
		socket.inet_aton(end)
		return True
	except:
		return False

def generate_ip_block(start, end ):
	import socket, struct
	start = struct.unpack('>I', socket.inet_aton(start))[0]
	end = struct.unpack('>I', socket.inet_aton(end))[0]
	return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

def write_block(args, str_data, data):
	if args.write:
		outfile = args.output if args.output !=None  else args.start
		f = open(f"{homedir}/output/{outfile}","w")
		f.write(str_data)
		f.close()
		print(f"[*] Generated {len(data)} IP Adresses. File Written to {homedir}/output/{outfile}")
	else:
		print(str_data)
		print(f"[*] Generated {len(data)} IP Adresses.")




def write_blocks(args):
	inputfile=  f"{homedir}/csv/{args.read}"
	with open(inputfile, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			startaddr = row['start']
			endaddr   = row['end']
			count = row['total']
			owner = row['owner']
			assigned=row['assigned'].replace("/","-")
			data = "\n".join(generate_ip_block(startaddr,endaddr))
			outfile =owner.replace(" ","");
			f = open(f"{homedir}/output/{outfile}.{assigned}","w")
			f.write(data)
			f.close()

if read:
	write_blocks(args)
else:
	if args.start != None and args.end != None:
		isvalid = verify_ip_address(args.start,args.end)
		if isvalid :
			data = generate_ip_block(args.start,args.end)
			str_data = "\n".join(generate_ip_block(args.start,args.end))
			write_block(args, str_data, data)
		else:
			print(f"[!] Error Invalid IP Adress provided")
	else:
		print(f"[!] Missing required Input Star IP and End IP Adress")








		





