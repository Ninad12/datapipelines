# Report columns rules
columns_rules = {
    'entity': ['not_null'],
    'report_name': ['not_null'],
    'num1': ['not_null', 'number'],
    'num2': ['not_null', 'number'],
    'num3': ['not_null', 'number']
}

# All valid entities
valid_entities = ['HSBC', 'Barclays']

# All valid reports
valid_reports = ['preformance', 'volumes']


# All valid Frequencies
Valid_Frequencies = ['monthly', 'weekly', 'daily', 'intraday']

Valid_Extensions = ['csv', 'json']

filename_template = 'EntityName_ReportName_Frequency_Timestamp.ext'