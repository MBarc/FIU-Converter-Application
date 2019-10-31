'''
This script is responsible for creating a final summary of the conversion process

Author: Michael Barcelo
'''
import xlwt #to be able to create an excel file and populate it with information

from information import extensions
from information import extensions_count
from converter import start_time
from converter import end_time
from converter import duration
from converter import successful
from converter import failed
from converter import not_attempted

info = open("info.txt", "r")

for i,line in enumerate(info):
	if i == 0:
		handler = line
	if i == 1:
		file_path = line
	if i == 2:
		feed_name = line
	if i == 3:
		group_name = line

#columns ; assign numbers to letters for easier programming
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

def addColor(name, hex_number, r, g, b):
	'''Registers new custom colors'''
	xlwt.add_palette_colour(name, hex_number)
	wb.set_colour_RGB(hex_number, r, g, b)

wb = xlwt.Workbook()

addColor("blue_title",0x21, 68, 114, 196)
addColor("blue_cell" , 0x22, 221, 235, 247)
addColor("green_title", 0x23, 146, 208, 80)
addColor("green_cell", 0x24, 198, 224, 180)
addColor("red_title", 0x25, 255, 0, 0)
addColor("red_cell", 0x26, 252, 228, 214)
addColor("yellow_title", 0x27, 255, 192, 0)
addColor("yellow_cell", 0x28, 255, 230, 153)

ws = wb.add_sheet('Conversion Report')

'''Column Widths'''
ws.col(n).width = 256 * 20 #20 characters wide (-ish)
ws.col(p).width = 256 * 20 
ws.col(r).width = 256 * 20
ws.col(t).width = 256 * 20

'''Row Heights'''
#ws.row(4).height = 256*20 #4 represents the X-location/row
#XLWT might have a default feature that automatically adjusts row height with a specified font size
#if this is not the case, then specify the row height for the first 1500 rows.
#might have to edit row height at the end of the script

'''General Information Chart'''
#ws.write_merge(top_row, bottom_row, left_column, right_column, 'Long Cell')
ws.write(7, b, "Handler", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_title; font: bold on, color black; align: horiz left; borders: left medium, right medium, top medium, bottom medium"))
ws.write_merge(7, 7, c, g, handler, xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold off, color black; align: horiz right; borders: left no_line, right medium, top medium, bottom thin"))
ws.write(8, b, "Directory", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_title; font: bold on, color black; align: horiz left; borders: left medium, right medium, top medium, bottom medium"))
ws.write_merge(8, 8, c, g, file_path, xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold off, color black; align: horiz right; borders: left no_line, right medium, top no_line, bottom thin"))
ws.write(9, b, "Group", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_title; font: bold on, color black; align: horiz left; borders: left medium, right medium, top medium, bottom medium"))
ws.write_merge(9, 9, c, g, group_name, xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold off, color black; align: horiz right; borders: left no_line, right medium, top no_line, bottom thin"))
ws.write(10, b, "Feed", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_title; font: bold on, color black; align: horiz left; borders: left medium, right medium, top medium, bottom medium"))
ws.write_merge(10, 10, c, g, feed_name, xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold off, color black; align: horiz right; borders: left no_line, right medium, top no_line, bottom medium"))

'''Directory Information'''
ws.write_merge(6, 6, i, k, "Directory Information", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_title; font: bold on, color black; align: horiz center; borders: left medium, right medium, top medium, bottom medium"))
ws.write(7, i, " ", xlwt.easyxf("pattern: pattern solid, fore_color blue_cell; border: left medium, right thin, top no_line, bottom thin"))
ws.write(7, j, " ", xlwt.easyxf("pattern: pattern solid, fore_color blue_cell; border: left no_line, right thin, top no_line, bottom thin"))
ws.write(7, k, "Count", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold on, color black; align: horiz center; borders: left no_line, right medium, top medium, bottom thin"))

row = 8 #applies to the following for loop; starts writing at this X-location/row
total = 0 #placeholder for the following for loop ; keeps track of the sum
for i in range(len(extensions)):
	for extension in extensions:
		for count in extensions_count:
			ws.write(row, j, extension, xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold off, color black; align: horiz left; borders: left thin, right thin, top thin, bottom thin")) #extension
			ws.write(row, k, count, xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color yellow_cell; font: bold off, color black; align: horiz left; borders: left thin, right medium, top thin, bottom thin")) #amount of videos per extension

			row += 1 # sets for the variable for the next passthrough in the for loop
			total += int(count) #adds the amount of each extension to the total

ws.write_merge(8, len(extensions) + 8, i, i, "Extensions", xlwt.easyxf("font: name Calibri, height 220; pattern: pattern solid, fore_color blue_cell; font: bold on, color black; align: horiz left; borders: left medium, right thin, top thin, bottom thin"))

ws.write(len(extensions) + 9, i, xlwt.write("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left medium, right thin, top thin, bottom thin"))
ws.write(len(extensions) + 9, j, xlwt.write("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left medium, right thin, top thin, bottom thin"))
ws.write(len(extensions) + 9, k, xlwt.write("font: name Calibri, height 220; pattern solid, fore_color yellow_cell; borders: left medium, right thin, top thin, bottom thin"))

ws.write(len(extensions) + 10, i, xlwt.write("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left medium, right thin, top thin, bottom medium"))
ws.write(len(extensions) + 10, j, "Total", xlwt.write("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left thin, right thin, top thin, bottom medium"))
ws.write(len(extensions) + 10, k, total, xlwt.write("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left thin, right medium, top thin, bottom medium"))

#worksheet.write(0, 0, "Hello World", xlwt.easyxf("pattern: pattern solid, fore_color yellow; font: color white; align: horiz right"))

'''Conversion Information'''
ws.write_merge(6, 6, m, n, "Conversion Information", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color blue_title;bold on; borders: left medium, right medium, top medium, bottom medium"))
ws.write(7, m, "Start Time", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color blue_cell; bold off; borders: left mediu, right thin, top no_line, bottom thin"))
ws.write(7, n, start_tine, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color yellow_cell; bold off; borders: left thin, right medium, top medium, bottom thin"))
ws.write(8, m, "End Time", xlwt.easyxf("font:name Calibri, height 220; pattern solid, fore_color blue_cell; bold off; borders: left medium, right thin, top thin, bottom thin"))
ws.write(8, n, end_time, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color yellow_cell; bold off;borders: left thin, right medium, top thin, bottom thin"))
ws.write(9, m, "Duration", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color blue_cell; bold off; borders: left medium, right thin, top thin, bottom thin"))
ws.write(9, m, duration, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color yellow; bold off; borders: left thin, right medium, top thin, bottom thin"))
ws.write(10, m, " ", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left medium, right thin, top thin, bottom, thin"))
ws.write(10, n, " ", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color blue_cell; borders: left thin, right medium, top thin, bottom, thin"))
ws.write(11, m, "Successful", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color green_title; borders: left medium, right thin, top thin, bottom thin"))
ws.write(11, n, len(successful), xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color green_cell; borders: left thin, right medium, top thin, bottom thin"))
ws.write(12, m, "Failed", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color red_title; borders: left medium, right thin, top thin, bottom medium"))
ws.write(12, n, len(failed), xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color red_cell; borders: left thin, right medium, top thin, bottom medium"))

'''Successful List'''
ws.write(6, p, "Successful List", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color green_title; borders: left medium, right medium, top medium, bottom medium"))

row = 7 
for i in range(len(successful)):
	for converted in successful:

		if i == len(successful): #checks to see if row is the last iteration in list ; this cell must have different borders
			ws.write(row, p, converted, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color green_cell; borders: left medium, right medium, top no_line, bottom medium"))
									                
		ws.write(row, p, converted, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color green_cell; borders: left medium, right medium, top no_line, bottom thin"))

			row += 1


'''Failed List'''
ws.write(6, p, "Failed List", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color red_title; borders: left medium, right medium, top medium, bottom medium"))

row = 7 
for i in range(len(failed)):
	for failed_conversion in failed:

		if i == len(failed): #checks to see if row is the last iteration in list ; this cell must have different borders
			ws.write(row, p, failed_conversion, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color red_cell; borders: left medium, right medium, top no_line, bottom medium"))
									                
		ws.write(row, r, failed_conversion, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color red_cell; borders: left medium, right medium, top no_line, bottom thin"))

			row += 1

'''Not Attempted'''
ws.write(6, t, "Not Attempted", xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color yellow_title; borders: left medium, right medium, top medium, bottom medium"))

row = 7 
for i in range(len(not_attempted)):
	for file in not_attempted:

		if i == len(not_attempted): #checks to see if row is the last iteration in list ; this cell must have different borders
			ws.write(row, p, failed_conversion, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color yellow_cell; borders: left medium, right medium, top no_line, bottom medium"))
								                
		ws.write(row, t, file, xlwt.easyxf("font: name Calibri, height 220; pattern solid, fore_color yellow_cell; borders: left medium, right medium, top no_line, bottom thin"))

		row += 1

wb.save("Report.xls")
