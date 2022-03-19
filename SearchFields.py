# You can add the following line to integrate PDFNetPython3
# into your solution from anywhere on your system so long as
# the library was installed successfully via pip

from asyncio.windows_events import NULL
from dataclasses import field
from doctest import OutputChecker
from gettext import NullTranslations
from PDFNetPython3 import *

# Load PDF file using PDFDoc and return doc object to caller
def loadPDF(input_file):
    print("Create PDF Doc object")
    doc = PDFDoc(input_file)
    doc.InitSecurityHandler()
    return doc

def closeConnection(doc):
    print("close connection")
    doc.Close()
    PDFNet.Terminate()

# Read All fields
def searchFieldValue(doc, field_name):
    print("in searchFieldValue")
    print("************* Search Filed using field_name *************")
    field = doc.GetField(field_name)
    if field != None:
        print("Field "+field_name +" found")
        print("Field name: " + field.GetName())
        print("Field partial name: " + field.GetPartialName())  
        
        
        sys.stdout.write("Field type: ")
        type = field.GetType()
        if type == Field.e_button:
            print("Button")
        elif type == Field.e_check:
            print("Check")
            sys.stdout.write("Field Value: ")
            print(field.GetValueAsBool())
        elif type == Field.e_radio:
            print("Radio")
            sys.stdout.write("Field Value: ")
            print(field.GetValue())
        elif type == Field.e_text:
            print("Text")
            if field.GetValue():
                sys.stdout.write("Field Value: ")
                print(field.GetValueAsString())
        elif type == Field.e_choice:
            print("Choice")
        elif type == Field.e_signature:
            print("Signiture")
        elif type == Field.e_null:
            print("Null")
        
    else:
        print("Field not found")
    
    print("*************************************************")
    
    


if __name__ == '__main__':
    # You need to initialize the PDFNet library 
    # Before calling any PDF related methods
    print("Initialize the PDFNet with demo key")
    PDFNet.Initialize("demo:1640580099013:7b471fbe030000000026f9b926d4c6fb8f1d7a7e00202e26ff16efd991")

    print("Specify input file location")
    
    
    input_file = "updated_pdf.pdf"

    doc = loadPDF(input_file)    

    if doc:
        print("call extract all fields")
        print("Search Filed(offer_prepared_date) value")
        searchFieldValue(doc, 'offer_prepared_date')
        searchFieldValue(doc, 'loan_cont_checkbox')

        print("close connection")
        doc.Close()
    
    else:
        print("no doc object created")

    print("Done")


