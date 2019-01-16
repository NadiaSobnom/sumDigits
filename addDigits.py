import os
import argparse

def cli():
    parser = argparse.ArgumentParser(description="Add digits of a string...") # App description

    parser.add_argument("--x", type=bool, default=False, help="Take hex value as input arg")
    parser.add_argument("--f", help="Take a file path as input arg")
    parser.add_argument("--inp", type=str, help="Input string arg")

    return parser.parse_args()

def main():
	args = cli() # get user inputs from command line
	result = None # final sum of digits
	inp = args.inp
	hex_val = args.x
	inp_file = args.f

	# inp or inp_file has to be provived. If inp_file is provided then
	# this script prioritizes and reads the file. Otherwise, it'll read
	# the inp string [--inp argument]	

	# Input string has to be converted to hex 
	if hex_val is True:
		inp = to_hex(inp)

	#if -f is sprecified to provide input-file
	if not inp_file:
		result = add_digits(inp)
	else:
		result = check_and_process_file(inp_file, hex_val)

	# Read a file (-f) and generated a list of results 
	if type(result) is list:
		if len(result) > 0:
			for item in result:
				print item
		# Empty file given in --f arg
		else: 
			print "Empty file provided: please add some string input\n"

	# Single output or an exception
	else:
		print result

def add_digits(inp):
	"""
	sum the digits of a string
	"""
	if not inp: return "No input string provided [--inp='abc123']\n"
	sm = 0 
	for ch in inp:
		if ch.isdigit():
			sm += int(ch)
	return sm

def to_hex(s):
	"""
	convert string to hex
	"""
	try:
		return s.encode("hex")
	except Exception as e:
		return str(e)

def check_and_process_file(path, is_hex=False):
	"""
	Validate file path and calculate digitsum
	for each input string in the file
	"""
	res = []
	try:
		with open(path, 'r') as ifile:
			for line in ifile:
				if is_hex: # string needs to converted to hex
					cur = add_digits(to_hex(line.strip()))
					res.append(cur)
				else:
					cur = add_digits(line)
					res.append(cur)
			ifile.close()

	except Exception as e:
		return "Failed to process file: Details - " + str(e) + "\n"
	return res	

def automate_test():
	"""
	Tests string in inputs list and assert with expected_results
	"""
	inputs = ["abc123", "qq", "bcfe677", "AfdfG294", "78456451315", "zzhjt583f", "0"]
	original_results = []
	expected_results = [6, 0, 20, 15, 49, 16, 0]
	expected_results_hex = [39, 16, 69, 74, 82, 82, 3]
	try:
		print "*************** AUTOMATED TEST CASES FOR STR AND HEX *****************\n"
		for i in range(len(inputs)):
			assert add_digits(inputs[i]) == expected_results[i] # For string in inputs
			assert add_digits(to_hex(inputs[i])) == expected_results_hex[i] # For hex string in inputs

		print "All tests passed for strings: " + str(inputs) + "\nOriginal and Expected results: " + str(expected_results) + "\nOriginal and Expected results in HEX: " + str(expected_results_hex) 

	except Exception as e:
		return "Failed automated test. Details: " + str(e) + "\n"

if __name__ == '__main__':
	main()

	# Activate line below to run autmated test.
	#automate_test()

