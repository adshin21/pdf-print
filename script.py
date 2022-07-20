import pandas as pd
from copy import deepcopy

# -- Constants -- #
rows_to_remove = [0, 1, 6, 8, 9, 10]
heading_row = 11
heading_col_remove = [8, 9, 10, 12, 13] 
after_heading_row_remove = [9, 10, 11]
# --------------- #

def process_list(l):
	return list(filter(lambda x: True if x else False, l))

def get_raw_data(file_path="file.xls"):
	df = pd.read_excel(file_path)
	df = df.fillna('')
	
	deep_copied_value = deepcopy(df.values)
	number_of_rows = len(deep_copied_value)
	
	clean_value = [process_list(row_data) for row_data in deep_copied_value]
	
	out_put = []
	for i in range(number_of_rows):
		heading_row_out = clean_value[i][:]
		if i in rows_to_remove:
			continue
		elif i == heading_row:
			heading_row_out = []
			for j in range(len(clean_value[i])):
				if j in heading_col_remove:
					continue
				heading_row_out.append(clean_value[i][j])
		elif i >= number_of_rows - 2:
			heading_row_out = clean_value[i][:]
		elif i > heading_row:
			heading_row_out = []
			for j in range(len(clean_value[i])):
				if j in after_heading_row_remove:
					continue
				heading_row_out.append(clean_value[i][j])
		out_put.append(heading_row_out)
	return out_put, number_of_rows


def main(file_path):
	print("\n\nFILE is => ", file_path)
	data, number_of_rows = get_raw_data(file_path)
	before_table_data = data[:5]
	table_data = data[5: -2]
	after_table_data = data[-2: ]


	from create_pdf import create_pdf
	create_pdf(file_path=file_path,  before_table=before_table_data[:], table=table_data[:], after_table=after_table_data[:])
	#for i in data:
	#	print(*i, sep=', ')

