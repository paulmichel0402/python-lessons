contacts = { 
'Paul' : {'phone' : '434-989-4986', 'twitter': '@pauljmichel', 'github': '@paulmichel0402'},

'Steph' : {'phone' : '703-338-4616', 'twitter' : '@nguyenist', 'github' : '@nguyenist'}
}

for key, value in contacts.items():
	#print key, value
	print key + '\'s contact information is: \n', 'Phone: ', value.get('phone'), '\nTwitter: ', value.get('twitter'), '\nGithub: ', value.get('github'), '\n'