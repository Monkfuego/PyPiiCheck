import fitz  # PyMuPDF for PDF handling
import PyPDF2
import openpyxl
import pytesseract
from PIL import Image

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using PyPDF2."""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join([page.extract_text() for page in reader.pages])
    return text

def extract_text_from_image(file_path):
    """Extract text from an image file using Tesseract OCR."""
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_excel(file_path):
    """Extract text from an Excel file using openpyxl."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    text = []
    for row in sheet.iter_rows(values_only=True):
        text.append(' '.join([str(cell) for cell in row if cell]))
    return ' '.join(text)

def extract_text(file_path):
    """Extract text based on file type."""
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        return extract_text_from_image(file_path)
    elif file_path.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb', '.xltm', '.xltx', '.csv')):
        return extract_text_from_excel(file_path)
    else:
        raise ValueError("Unsupported file type for text extraction.")

def extract_image_from_file(file_path):
    """Extract images from a PDF file or return the image file path."""
    if file_path.endswith('.pdf'):
        doc = fitz.open(file_path)
        extracted_images = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = f"extracted_image_{page_num + 1}_{img_index + 1}.{image_ext}"
                
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_bytes)
                extracted_images.append(image_filename)
        return extracted_images  # Return list of extracted image filenames
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        return [file_path]  # Return the image file path as a list
    else:
        raise ValueError("Unsupported file type for image extraction.")
