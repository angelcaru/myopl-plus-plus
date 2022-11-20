#!/usr/bin/python3

import basic, sys, os

def main():
	if len(sys.argv) > 1:
		dyr, fn = os.path.split(sys.argv[1])
		os.chdir(dyr)
		with open(fn, "r") as f:
			code = f.read()
		_, error = basic.run(fn, code)
		if error:
			print(error.as_string(), file=sys.stderr)
			exit(1)
		exit()
	while True:
		text = input('myopl++ > ')
		if text.strip() == "": continue
		result, error = basic.run('<stdin>', text)

		if error:
			print(error.as_string(), file=sys.stderr)
		elif result:
			real_result = result.elements[0]
			if len(result.elements) != 1:
				real_result = result
			print(repr(real_result))
			basic.global_symbol_table.set("_", real_result)

if __name__ == "__main__":
	main()
