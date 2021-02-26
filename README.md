# useful_lib
## A bunch of small useful python functions

1.  chxor
    > _Description:_ Returns XOR of ASCII values of a (list of) character(s)
    - Input : a , b(optional) (strings)
   - Case 1 : Only 'a'(string) is specified
     *  returns a single char that is the XOR of all characters in a, i.e. a[0]^a[1]^...a[-1]
   - Case 2 : 'a' is a  string, 'b' is a single char (UPDATE : Works for the vice versa case also)
     *  returns a string where each character of 'a' is XOR'd with 'b' , i.e. a[0]^b , a[1]^b, .... , a[-1]^b
   - Case 3 : both 'a' and 'b' are strings
     *  returns character-wise XOR of characters in 'a' and 'b'. If length of 'a' and 'b' differ, the larger string is truncated to match the length of the smaller one

2.  TF_list_from_num
    > _Description:_ Converts an input number into l-bit list of True/False values. 
    
    > Parameters :
    > * l = length of binary number. Default 8. E.g. if input n=3 , result is [False,False,False,False,False,False,True,True]
    > * inv = invert True/False. Default False. E.g. if inv = True for n=3 , result is [True,True,True,True,True,True,False,False]
    > * force_l = force output length to be 'l' bits long. Default False. Used when the default binary length of input is longer than 'l' bits. E.g. if l=3 and force_l = True then for n= 15 output is  [True,True,True]. If force_l was False it would have been [True,True,True,True] 
     - Input : n (integer)
     - Output : list-type 

3.  rand_id
    > _Description:_ Generate a random sequence of alphanumeric + special characters 
    
    > Parameters :
    > * iSpl = Any additional special characters to use. Default ""
    > * iUpper = Include uppercase alphabets (A-Z) also. Default True
    > * iLower = Include lowercase alphabets(a-z) also. Default True
    > * iDigits = Include digits (0-9) also. Default True
    > * exclude_id = List of all specific ID's to exclude. Useful to excluded already generated / default random ID's. Default []
    > * exclude = List of all specific characters to exclude. Case sensitive. Default []
    > * seed = seed for initial randseed. Default None (i.e. no seed used)
     - Input : n (integer) = length of random ID to generate
     - Output : mess = generated random ID

4.  same_type
    > _Description:_ Compare if type of input n is same as m (m is a type type, i.e. m=list) Essentially returns type(n)== m
    
    > Parameters :
    > * m = type to compare type(n) against. Default NoneType
     - Input : n = input to compare m against
     - Output : True/False (raises Exception if m is not type 'type'/'NoneType' )

5.  is_float
    > _Description:_ Essentially returns type(n)== float
     - Input : n = input to check
     - Output : True/False 

6.  input_num
    > _Description:_  Cleanly input an integer/ float
    
    > Parameters :
    > * mess = Message to display on asking user for input/ Default ""
    > * type = 0 for integer, 1 for float. Default 0
    > * error_message = message to display if input is not a number. Default "error, try again:"
    > * max_tries = maximum wrong imputs from user before returning ret_type
    > * ret_type = what to return if user fails to give valid input in max_tries. Default None
     - Input : _None_
     - Output : Value input from user / ret_type in case max_tries is reached

7.  pretty_dict
    > _Description:_ Prints dicts in a clean way. Also used to print object.\_\_dict\_\_
    
    > Parameters :
    > * v = seperator between key and value of dict
     - Input : d = input dict (or object with .\_\_dict\_\_ attribute) to print
     - Output : _None_ (raises AttributeError if d is neither dict nor object with attribute \_\_dict\_\_ )



