-------------------------------- Add Digits in a string ----------------------------

This script adds the digits of a string and returns the sum. 

1. Input arguments:
	a. [--inp]: The input string provided by user. Usage: [--inp="abc123"] 
	b. [--x]: Converts inp (step 1) to hex if argument specified. Usage: [--x=True, default is False]
	c. [--f]: A file containing input strings. Usage: [--f="testCases.txt"]
	
	NOTE: Either a or c must be provided (unless automate_test() is activated). This is the input string that script will process.

2. How to build and run the program:
	Requirement: python 2.7+ needs to be installed
	
	a. Checkout code
    b. Open terminal and cd to sumDigits
 	c. Run: python addDigits.py -h. 
       This will show valid arguments (Step 1)
	d. Run: python addDigits.py --inp="abc123".
       Please replace "abc123" with the choice of your string. It should return the result (ex: 6)

 
3. Some test cases, command and their output
	Command                                                 Output        Command Description
	-------------------------------------------------------------------------------------------------------------
	a. python addDigits.py --inp="abc123"                      6          --inp argument takes input string
	b. python addDigits.py --inp="abc123" --x=True	           39         --x takes bool[True or False]
	c. python addDigits.py --f="testCases.txt"				   6          --f takes a file as input. tesCases.txt has some input strings	
															   0
															   20
															   15
															   49
															   16
															   0
	d. python addDigits.py --f="testCases.txt" --x=True        39          This processes same testCases.txt but strings converted to hex
															   16
															   69
															   74
															   82
															   82
															   3
	e. python addDigits.py --f="emptyTestCase.txt"             Empty file provided: please add some string input
	f. python addDigits.py                                     No input string provided [--inp='abc123']

4. Run Automated test
	To run automated test please activate line-110 or the last-line in addDigits.py file (sumDigits/addDigits.py -> automate_test()). It should run automated test for a list of regular string and and a list of hex vauled string
