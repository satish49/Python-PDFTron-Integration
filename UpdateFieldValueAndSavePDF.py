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
def updateFieldValue(doc, field_name, new_value, output_file):
    print("in updateFieldValue")
    print("************* Read all fields and types and print here *************")
    field = doc.GetField(field_name)
    if field != None:
        print("Field "+field_name +" found")
        print("Existing Value of filed")
        if field.GetValue():
            print("Value "+ field.GetValue())
        else:
            print("no value found")
            if field.GetType() == Field.e_text:
                print("set text value")
                field.SetValue(new_value)
                print("save pdf to "+output_file)
                doc.RefreshFieldAppearances()
                doc.Save(output_file, 0)
            elif field.GetType() == Field.e_check:
                print("set True for checkbox ")
                field.SetValue(new_value)
            else:
                print("field type is "+field.GetType())
    else:
        print("Field not found")
    
    print("*************************************************")
    
    


if __name__ == '__main__':
    # You need to initialize the PDFNet library 
    # Before calling any PDF related methods
    print("Initialize the PDFNet with demo key")
    PDFNet.Initialize("demo:1640580099013:7b471fbe030000000026f9b926d4c6fb8f1d7a7e00202e26ff16efd991")

    print("Specify input and outout file locations")
    input_file = "final_rpa_2021.pdf"
    output_file = "updated_pdf.pdf"

    doc = loadPDF(input_file)    

    if doc:
        print("call extract all fields")
        print("Update Filed(offer_prepared_date) value")
        updateFieldValue(doc, 'offer_prepared_date', "2022-03-21", output_file)
        updateFieldValue(doc, 'loan_cont_checkbox', True, "updated_check.pdf")

        print("save pdf to "+output_file)
        doc.RefreshFieldAppearances()
        doc.Save(output_file, 0)

        print("close connection")
        doc.Close()
    
    else:
        print("no doc object created")

    print("Done")


