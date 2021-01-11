def null_check(rule, column_data):
	if 'not_null' in rule:
			return True if str(column_data).strip() != '' else False
	return True

def number_check(rule, column_data):
	if 'number' in rule:
		return str(column_data).strip().isnumeric()
	return True