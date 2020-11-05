import xlsxwriter
# demo.xlsx 이름의 Excel 파일을 생성한다. 해당 Excel의 pointer는 'workbook' 이다. 
workbook = xlsxwriter.Workbook('demo.xlsx')
""" workbook이 가리키는 Excel 파일에 sheet 를 추가한다. 
    추가하는 sheet 이름은 별도로 설정할 수 있고, 없으면 Default 이름이 들어간다."""
worksheet = workbook.add_worksheet() # default 'sheet1' 로 생성함
worksheet = workbook.add_worksheet('my_sheet') # my_sheet란 이름의 sheet를 생성함

# A열의 폭(행넓이)를 20으로 한다. 
worksheet.set_column('A:A', 20)
# 0열의 높이(열높이)를 17.5로 한다.
worksheet.set_row(0,17.5)

# add_formt으로 다양한 서식을 적용할 수 있으며 여러 서직을 나열 후 한번에 적용가능하다.
bold = workbook.add_format({'bold': True})

# A1 Cell에 Hello를 입력한다.
worksheet.write('A1', 'Hello')

# A2 Cell에 World를 입력하면서 bold 를 적용한다. bold는 위에서 적용한 bold format 문을 의미한다.
worksheet.write('A2', 'World', bold)

worksheet.write_url('A5', 'http://www.python.org/')

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)      # 같은의미로는 worksheet.write(A3,123) 이다. 
worksheet.write(3, 0, 123.456) # 같은의미로는 worksheet.write(A4,123.456)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png') # B5열에 logo.png를 삽입함.

workbook.close()