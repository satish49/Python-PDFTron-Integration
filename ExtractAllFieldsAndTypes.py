# You can add the following line to integrate PDFNetPython3
# into your solution from anywhere on your system so long as
# the library was installed successfully via pip

from dataclasses import field
from doctest import OutputChecker
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
def extractAllFieldsFromPDF(doc):
    print("in extractAllFieldsFromPDF")
    print("************* Read all fields and types and print here *************")
    itr = doc.GetFieldIterator()
    while itr.HasNext():
        print("Field name: " + itr.Current().GetName())
        print("Field partial name: " + itr.Current().GetPartialName())        
        sys.stdout.write("Field type: ")
        type = itr.Current().GetType()
        if type == Field.e_button:
            print("Button")
        elif type == Field.e_check:
            print("Check")
        elif type == Field.e_radio:
            print("Radio")
        elif type == Field.e_text:
            print("Text")
        elif type == Field.e_choice:
            print("Choice")
        elif type == Field.e_signature:
            print("Signiture")
        elif type == Field.e_null:
            print("Null")
            
        print("------------------------------")
        itr.Next()
    print("*************************************************")
    
    


if __name__ == '__main__':
    # You need to initialize the PDFNet library 
    # Before calling any PDF related methods
    print("Initialize the PDFNet with demo key")
    PDFNet.Initialize("demo:1640580099013:7b471fbe030000000026f9b926d4c6fb8f1d7a7e00202e26ff16efd991")

    print("Specify input and outout file locations")
    input_file = "final_rpa_2021.pdf"

    doc = loadPDF(input_file)    

    if doc:
        print("call extract all fields")
        extractAllFieldsFromPDF(doc)

        print("close connection")
        doc.Close()
    
    else:
        print("no doc object created")

    print("Done")

