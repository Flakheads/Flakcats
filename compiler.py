import re

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

