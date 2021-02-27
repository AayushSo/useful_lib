from random import choices,seed as randseed
#from secrets import choices
from string import ascii_lowercase, ascii_uppercase, digits
from math import ceil, log2

def chxor(*args): ## xor of ascii value characters
	## xor of:
	## 'a' with all characters in 'sequence_b' (or vice versa)
	## 'sequence_a' with 'sequence_b' character-wise
	##	'sequence_a' charcters each with itself
	if len(args)==2:
		a=args[0]
		b=args[1]
		if len(a)==1:
			return ''.join([ chr( ord(i) ^ ord(a) ) for i in b ])
		elif len(b)==1:
			return ''.join([ chr( ord(i) ^ ord(b) ) for i in a ])
		else:
			return ''.join([ chr( ord(i) ^ ord(j) ) for i,j in zip(a,b) ])
	elif len(args)==1:
		z=0
		for i in args[0]:
			z=z^ord(i)
		return chr(z)		

def TF_list_from_num(n,l=8,inv=False,force_l = False):
	## binary 0/1 representation of a number as False/True
	if not force_l : l = max(l,ceil(log2(n))) ## force output to be l bits long. If force_l is true and bits required it is longer, result is truncated
	s='{:0'+str(l)+'b}'
	a=inv
	b=not inv
	m=2**l
	return [b if i=='1' else a for i in list(s.format(int(n)%m))]

def rand_id(n, iSpl="",iUpper=True, iDigits=True,iLower=True,exclude = [], exclude_id=[],seed=None): #n-> number of characters iUpper-> include uppercase, iLower-> include lowercase iSpl-> include special characters as included as string
	#Generate a random sequence of alphanumeric + special characters
	if seed !=None: randseed(seed)
	v=''.join(iSpl)
	v+=iSpl
	if iUpper: v+=ascii_uppercase
	if iLower: v+=ascii_lowercase
	if iDigits: v+=digits
	if len(exclude)>0 :
		for i in exclude : ##no need to add try since .replace doesnt throw error if char is not present
			v = v.replace(i,'')
	mess = ''.join(choices(v,k=n))
	while mess in exclude_id: mess = ''.join(choices(v,k=n))
	return mess


def same_type(n,m=type(None)):
	if type(m) == type or m == type(None): # m is type 'type' / 'NoneType'
		return type(n)==m
	else : raise Exception

def isfloat(n): #n is a string type
	return type(n)==float

def input_num(mess="",type=0,error_message="error, try again:",max_tries=3,ret_type=None):	#0-> int 1-> float
	#input a number. 0 for int, 1 for float. In case of no match, retry a max number of times, else return None
	pass_flag=False
	trycount=1
	while not pass_flag:
		v=input(mess)
		if type==0 or type==1:
			try:
				return (int(v)) if type==0 else (float(v))
			except:
				trycount+=1
				if trycount> max_tries: pass_flag=True
				print(error_message)
		else:
			return ret_type
	print("Max tries reached. Returning error.")
	return ret_type
	
def prettydict(d,v=':'):
	if type(d) is dict:
		for i in d: print(i,v,d[i])
	else:
		for i in d.__dict__: print(i,v,d.__dict__[i])
