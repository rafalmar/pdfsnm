import os
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
 
""" 
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format(output_filename))
""" 

 
def pdf_splitter(path, scope):
	fname = os.path.splitext(os.path.basename(path))[0]
	
	pdf = PdfFileReader(path)
	
	if scope=="explode":
	
		for page in range(pdf.getNumPages()):
			pdf_writer = PdfFileWriter()
			pdf_writer.addPage(pdf.getPage(page))
	 
			output_filename = '{}_page_{}.pdf'.format(
				fname, page+1)
	 
			with open(output_filename, 'wb') as out:
				pdf_writer.write(out)
	 
			print('Created: {}'.format(output_filename))
			
	else:
		scope=re.split("[, \!?;]+", scope)
		for i in range(len(scope)):
			element=re.split("[:-]+", scope[i])
			if len(element)==1:
				element[0]=int(element[0])
				element.append(int(element[0])+1)
			else:
				element=[int(element[j]) for j in range(len(element))]
				element[-1]=element[-1]+1
			scope[i]=list(range(*element))
		
		
		pdf_writer = PdfFileWriter()
		print(scope)
		
		
		for i in scope:
			for j in i:
				pdf_writer.addPage(pdf.getPage(j-1))   #TU SPRAWDZIC
		
		output_filename="wybrane_od"+str(scope[0][0])+"do"+str(scope[-1][-1])+".pdf"
		with open(output_filename, 'wb') as out:
				pdf_writer.write(out)
	 
		print('Created: {}'.format(output_filename))
		

if __name__ == '__main__':

	zakres=sys.argv[1]
	#zakres="1, 4-6, 5; 7 8, 10:15"
	path = sys.argv[2]
	pdf_splitter(path, zakres)