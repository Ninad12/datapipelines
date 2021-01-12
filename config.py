# Report columns rules
columns_rules = {
    'company': ['not_null'],
    'owner': ['not_null'],
    'gst_num': ['not_null', 'number'],
    'pan_num': ['not_null', 'number'],
    'mobile': ['not_null', 'number']
}

# All valid entities
<<<<<<< HEAD
valid_entities = ['HSBC', 'Barclays']

# All valid reports
valid_reports = ['preformance', 'volumes']
=======
valid_entities = ['ninad', 'mayur']

# All valid reports
valid_reports = ['joshi', 'modi']
>>>>>>> bd2c27da9171260af67f17c0d62dff5822c2c3b9

# All valid Frequencies
Valid_Frequencies = ['monthly', 'weekly', 'daily', 'intraday']

<<<<<<< HEAD
=======
Valid_Extensions = ['csv', 'json']

>>>>>>> bd2c27da9171260af67f17c0d62dff5822c2c3b9
filename_template = 'EntityName_ReportName_Frequency_Timestamp.ext'