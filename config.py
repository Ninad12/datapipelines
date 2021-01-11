# Report columns rules
columns_rules = {
    'company': ['not_null'],
    'owner': ['not_null'],
    'gst_num': ['not_null', 'number'],
    'pan_num': ['not_null', 'number'],
    'mobile': ['not_null', 'number']
}

# All valid entities
valid_entities = ['ninad', 'mayur']

# All valid reports
valid_reports = ['joshi', 'modi']

# All valid Frequencies
Valid_Frequencies = ['monthly', 'weekly', 'daily', 'intraday']

Valid_Extensions = ['csv', 'json']

filename_template = 'EntityName_ReportName_Frequency_Timestamp.ext'