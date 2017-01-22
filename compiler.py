import re
import string
from argparse import *

def reversable(input):
	output = input
	pairs = [")(","><","][","}{"]
	for a,b in pairs:
		output = output.translate(string.maketrans(a+b,b+a))
	return output == input[::-1]

def fcTobf(source):
	source = re.sub("[^()<>[\]{}]","",source)
	for nilad,replacement in [("()","a"),("<>","b"),("[]","c"),("{}","d")]:
		source = source.replace(nilad,replacement)
	for x in range(8):
		source = source.replace("()<>[]{}"[x],"12345678"[x])
	#()
	source = source.replace("a","()")
	#(...)
	source = source.replace("1","([{}]")
	source = source.replace("2",")")
	#<>
	source = source.replace("b","<>")
	#<...>
	source = source.replace("3","<")
	source = source.replace("4",">")
	#[]
	source = source.replace("c","[()]")
	#[...]
	source = source.replace("5","[")
	source = source.replace("6","]")
	#{}
	source = source.replace("d","({}<({}<>)<>>)<>({}<>)")
	#{...}
	source = source.replace("7","(({}))(()){{}(({}<")
	source = source.replace("8",">)<({}[({})]<>)<>>)<>({}<>)}{}{}")
	return source

#Work in progress
def fcTosc(source):
	source = re.sub("[^()<>[\]{}]","",source)
	for nilad,replacement in [("()","a"),("<>","b"),("[]","c"),("{}","d")]:
		source = source.replace(nilad,replacement)
	for x in range(8):
		source = source.replace("()<>[]{}"[x],"12345678"[x])
	pass

if __name__ == "__main__":
	parser = ArgumentParser(description="The flackcats compiler")
	parser.add_argument("bfsource",metavar="source",action="store",help="Name of the file where the flakcats source code is contained.",type=file)
	parser.add_argument("dest",metavar="destination",action="store",help="Name of the destination where compiled code will be writen.",type=FileType("w"))
	args = parser.parse_args()
	args.dest.write(fcTobf(args.bfsource.read().strip()))
