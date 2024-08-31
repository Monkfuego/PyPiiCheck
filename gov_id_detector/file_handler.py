# gov_id_detector/file_handler.py

import PyPDF2
import openpyxl
import pytesseract
from PIL import Image

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join([page.extract_text() for page in reader.pages])
    return text

#def extract_text_from_docx(file_path):
 #   doc = docx.Document(file_path)
  #  text = '\n'.join([para.text for para in doc.paragraphs])
   # return text

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
       # return extract_text_from_docx(file_path)
       pass
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        return extract_text_from_image(file_path)
    elif file_path.endswith((".xls" , ".xlsx" , ".xlsm" , ".xlsb" , ".xltm" , ".xltx" , ".csv")):
        return extract_text_from_excel(file_path)
        

def extract_text_from_excel(file_path):
    dataframe = openpyxl.load_workbook(file_path)
    dataframe1 = dataframe.active
    for row in range(0, dataframe1.max_row):
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            print(col[row].value)
            
