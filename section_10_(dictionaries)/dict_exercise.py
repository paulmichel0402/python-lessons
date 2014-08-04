contacts = { 
'Paul' : {'phone' : '434-555-5555', 'twitter': '@pauljmichel', 'github': '@paulmichel0402'},

'Steph' : {'phone' : '703-555-5555', 'twitter' : '@nguyenist', 'github' : '@nguyenist'}
}

for key, value in contacts.items():
	#print key, value
	print key + '\'s contact information is: \n', 'Phone: ', value.get('phone'), '\nTwitter: ', value.get('twitter'), '\nGithub: ', value.get('github'), '\n'