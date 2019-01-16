-------------------------------- ADD DIGITS IN STRING ----------------------------

This script adds the digits of a string and returns the sum. 

Input arguments:
1. [--inp]: The input string provided by user. Usage: [--inp="abc123"] 
2. [--x]: Converts inp (step 1) to hex if argument specified. Usage: [--x=True, default is False]
3. [--f]: A file containing input strings. Usage: [--f="testCases.txt"]
	
	NOTE: Either a or c must be provided (unless automate_test() is activated). This is the input string that script will process.

How to build and run the program:
	Requirement: python 2.7+ needs to be installed
	
1. Checkout code
2. Open terminal and cd to sumDigits
3. Run: python addDigits.py -h. This will show valid arguments (Step 1)
4. Run: python addDigits.py --inp="abc123". Please replace "abc123" with the choice of your string. It should return the result (ex: 6)

 
Some test cases, command and their output
1. Command: python addDigits.py --inp="abc123"           Output: 6      
2. Command: python addDigits.py --inp="abc123" --x=True	 Output: 39    
3. Command: python addDigits.py --f="testCases.txt"	     Output: 6 0 20 15 49 16 0
4. python addDigits.py --f="testCases.txt" --x=True      Output: 39 16 69 74 82 82 3
5. python addDigits.py --f="emptyTestCase.txt"           Output: Empty file provided: please add some string input
6. python addDigits.py                                   Output: No input string provided [--inp='abc123']

Run Automated test
	To run automated test please activate line-110 or the last-line in addDigits.py file (sumDigits/addDigits.py -> automate_test()). It should run automated test for a list of regular string and and a list of hex vauled string
