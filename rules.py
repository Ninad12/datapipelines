def null_check(rule, column_data):
	if 'not_null' in rule:
			#return True if str(column_data).strip() != '' else False
			 return '' if str(column_data).strip() != '' else 'for null_check'
	#return true
	return ''

def number_check(rule, column_data):
	if 'number' in rule:
		#return str(column_data).strip().isnumeric()
		if str(column_data).strip().isnumeric():
			return '' 
	return 'for number'