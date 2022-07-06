from fpdf import FPDF 


class PDF(FPDF):
	
	def header(self):
		title_string = 'RECURRING DEPOSIT INSTALLMENT REPORT'
		# logo
		self.image('image.png', 6, 4, 50, 20)
		self.ln(1)
		self.set_font('helvetica', 'B', 12)
		title_width = self.get_string_width(title_string)
		left_margin = (self.w - title_width) / 2 + 6
		self.set_x(left_margin)
		self.cell(0, 10, title_string, ln=True, align='C')
		self.ln(5)
	
	def write_before_table(self, before_table_data=[]):
		self.set_x(0)
		self.set_font('helvetica', '', 10)
		for row in before_table_data:
			row_string = '  '.join(row)
			self.cell(0,8,row_string, ln=True, align='C')
		self.ln()

	def write_after_table(self, after_table=[]):
		self.set_font('helvetica', 'B', 12)
		c = 0 
		next_x = 0
		for i in after_table:
			self.set_x(0)
			self.set_fill_color(224, 235, 255)
			if c == 0:
				# Just to compansate 2 with fill colour
				self.cell(2, 8, "", fill=True)
				
				self.cell(150, 8, i[0], fill=True)
				self.set_x(150)
				self.cell(150, 8, i[1], fill=True)
			else:				
				self.set_x(3)	
				self.cell(0, 8, i[0], fill=False)
				self.set_x(160)
				self.cell(0, 8, i[1], fill=False)
			c += 1
			self.ln()
		
	def create_table(self, table_data, title='', data_size=10, title_size=12,
					 align_data='L', align_header='L', cell_width='even',
					 x_start='x_default', emphasize_data=[], emphasize_style=None,
					 emphasize_color=(0, 0, 0)):
		"""
		table_data: 
					list of lists with first element being list of headers
		title: 
					(Optional) title of table (optional)
		data_size: 
					the font size of table data
		title_size: 
					the font size fo the title of the table
		align_data: 
					align table data
					L = left align
					C = center align
					R = right align
		align_header: 
					align table data
					L = left align
					C = center align
					R = right align
		cell_width: 
					even: evenly distribute cell/column width
					uneven: base cell size on lenght of cell/column items
					int: int value for width of each cell/column
					list of ints: list equal to number of columns with the widht of each cell / column
		x_start: 
					where the left edge of table should start
		emphasize_data:  
					which data elements are to be emphasized - pass as list 
					emphasize_style: the font style you want emphaized data to take
					emphasize_color: emphasize color (if other than black) 

		"""
		default_style = self.font_style
		if emphasize_style == None:
			emphasize_style = default_style

		# default_font = self.font_family
		# default_size = self.font_size_pt
		# default_style = self.font_style
		# default_color = self.color # This does not work

		# Get Width of Columns
		def get_col_widths():
			col_width = cell_width
			if col_width == 'even':
				col_width = self.epw / len(data[
											   0]) - 1  # distribute content evenly   # epw = effective page width (width of page not including margins)
			elif col_width == 'uneven':
				col_widths = []

				# searching through columns for largest sized cell (not rows but cols)
				for col in range(len(table_data[0])):  # for every row
					longest = 0
					for row in range(len(table_data)):
						cell_value = str(table_data[row][col])
						value_length = self.get_string_width(cell_value)
						if value_length > longest:
							longest = value_length
					col_widths.append(longest + 4)  # add 4 for padding
				col_width = col_widths

				### compare columns 

			elif isinstance(cell_width, list):
				col_width = cell_width  # TODO: convert all items in list to int		
			else:
				# TODO: Add try catch
				col_width = int(col_width)
			return col_width

		# Convert dict to lol
		# Why? because i built it with lol first and added dict func after
		# Is there performance differences?
		if isinstance(table_data, dict):
			header = [key for key in table_data]
			data = []
			for key in table_data:
				value = table_data[key]
				data.append(value)
			# need to zip so data is in correct format (first, second, third --> not first, first, first)
			data = [list(a) for a in zip(*data)]

		else:
			header = table_data[0]
			data = table_data[1:]

		line_height = self.font_size * 2.5

		col_width = get_col_widths()
		self.set_font(size=title_size)

		# Get starting position of x
		# Determin width of table to get x starting point for centred table
		if x_start == 'C':
			table_width = 0
			if isinstance(col_width, list):
				for width in col_width:
					table_width += width
			else:  # need to multiply cell width by number of cells to get table width 
				table_width = col_width * len(table_data[0])
			# Get x start by subtracting table width from pdf width and divide by 2 (margins)
			margin_width = self.w - table_width
			# TODO: Check if table_width is larger than pdf width

			center_table = margin_width / 2  # only want width of left margin not both
			x_start = center_table
			self.set_x(x_start)
		elif isinstance(x_start, int):
			self.set_x(x_start)
		elif x_start == 'x_default':
			x_start = self.set_x(self.l_margin)

		# TABLE CREATION #

		# add title
		if title != '':
			self.multi_cell(0, line_height, title, border=0, align='j', ln=3,
							max_line_height=self.font_size)
			self.ln(line_height)  # move cursor back to the left margin

		self.set_font(size=data_size)
		# add header
		y1 = self.get_y()
		if x_start:
			x_left = x_start
		else:
			x_left = self.get_x()
		x_right = self.epw + x_left
		if not isinstance(col_width, list):
			self.set_x(0)
			for datum in header:
				self.set_fill_color(224, 235, 255)
				self.multi_cell(col_width, line_height, datum, border=0,
								align=align_header, ln=3,
								max_line_height=self.font_size, fill=True)
				x_right = self.get_x()
			self.ln(line_height)  # move cursor back to the left margin
			y2 = self.get_y()
			self.line(x_left, y1, x_right, y1)
			self.line(x_left, y2, x_right, y2)

			for row in data:
				self.set_x(0)
				for datum in row:
					if datum in emphasize_data:
						self.set_text_color(*emphasize_color)
						self.set_font(style=emphasize_style)
						self.multi_cell(col_width, line_height, datum, border=0,
										align=align_data, ln=3,
										max_line_height=self.font_size)
						self.set_text_color(0, 0, 0)
						self.set_font(style=default_style)
					else:
						self.multi_cell(col_width, line_height, datum, border=0,
										align=align_data, ln=3,
										max_line_height=self.font_size)  # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
				self.ln(line_height)  # move cursor back to the left margin

		else:
			# This else I'm using to modify as per pdf requirements
			# this is being used in header generation while col_width is a list argument
			self.set_x(0)
			for i in range(len(header)):
				self.set_fill_color(224, 235, 255)
				datum = header[i]
				self.set_font(style="B")
				self.multi_cell(col_width[i], line_height * 1.25 , datum, border=0,
								align=align_header, ln=3,
								max_line_height=self.font_size, fill=True)
				x_right = self.get_x()
			self.ln(line_height)  # move cursor back to the left margin
			y2 = self.get_y()
			self.line(x_left, y1, x_right, y1)
			self.line(x_left, y2 + 2, x_right, y2 + 2)
			
			# setting some gap between header and data
			self.set_y(y2 + 2)
			self.set_font(style='')

			for i in range(len(data)):
				self.set_x(0)
				row = data[i]
				for i in range(len(row)):
					datum = row[i]
					if not isinstance(datum, str):
						datum = str(datum)
					adjusted_col_width = col_width[i]
					if datum in emphasize_data:
						self.set_text_color(*emphasize_color)
						self.set_font(style=emphasize_style)
						self.multi_cell(adjusted_col_width, line_height, datum,
										border=0, align=align_data, ln=3,
										max_line_height=self.font_size)
						self.set_text_color(0, 0, 0)
						self.set_font(style=default_style)
					elif isinstance(align_data, list):
						self.multi_cell(adjusted_col_width, line_height, datum,
										border=0, align=align_data[i], ln=3,
										max_line_height=self.font_size)  # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
					else:
						self.multi_cell(adjusted_col_width, line_height, datum,
										border=0, align=align_data, ln=3,
										max_line_height=self.font_size)  # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
				self.ln(line_height)  # move cursor back to the left margin
		y3 = self.get_y()
		self.line(x_left, y3, x_right, y3)


def create_pdf(file_name="hello_world", before_table=[], table=[], after_table=[]):	
	pdf = PDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	pdf.write_before_table(before_table)
	#pdf.write_table_data(table)
	
	# Adding two empty columns at begingin and end will remove if needed
	for i in range(len(table)):
		table[i] = [""] + table[i] + [""]
	pdf.create_table(
		table, 
		data_size=10, 
		cell_width=[2, 27, 28, 35, 23, 23, 19, 15, 15, 21, 2], 
		x_start=0, 
		align_data=["", "", "", "", "", "", "C", "C", "C", "", ""])
	pdf.write_after_table(after_table)
	pdf.output(f'/Users/adityak.umar/xl/output/{file_name}.pdf')
