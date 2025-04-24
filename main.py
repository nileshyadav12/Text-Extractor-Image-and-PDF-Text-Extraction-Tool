import pytesseract
from PIL import Image
import fitz  # PyMuPDF for working with PDFs
import os


# https://github.com/UB-Mannheim/tesseract/wiki

#download the versionand install  -tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)


class TextExtractor:
    def __init__(self, tesseract_path=None):
        """
        Initialize the TextExtractor class.
        Optionally specify the path to the tesseract executable.
        """
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        else:
            # Default path (make sure to set Tesseract executable in the system PATH)
            pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Deepak\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    def extract_text_from_image(self, image_path):
        """Extract text from an image using OCR."""
        try:
            # Open the image file
            img = Image.open(image_path)
            # Use pytesseract to do OCR on the image
            extracted_text = pytesseract.image_to_string(img)
            return extracted_text
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

    def extract_text_from_pdf(self, pdf_path):
        """Extract text from a PDF."""
        try:
            extracted_text = ""
            # Open the PDF file
            doc = fitz.open(pdf_path)
            # Iterate through each page in the PDF
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                extracted_text += page.get_text()
            return extracted_text
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return None

    def extract_text(self, file_path):
        """Determine file type and extract text accordingly."""
        if not os.path.exists(file_path):
            print("The file does not exist.")
            return None

        # Get the file extension to determine the type (PDF, JPG, PNG)
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension in ['.jpg', '.jpeg', '.png']:
            print("Extracting text from image...")
            return self.extract_text_from_image(file_path)
        
        elif file_extension == '.pdf':
            print("Extracting text from PDF...")
            return self.extract_text_from_pdf(file_path)

        else:
            print("Unsupported file format. Please provide a JPG, PNG, or PDF file.")
            return None

# Example usage:
if __name__ == "__main__":
    # Specify the file path
    file_path = r"C:\Users\Deepak\Desktop\python\pan.jpeg"  # Replace with your file path pdf and image

    # Initialize the TextExtractor class
    extractor = TextExtractor()

    # Extract text from the specified file
    extracted_text = extractor.extract_text(file_path)

    # Display extracted text
    if extracted_text:
        print("Text extracted successfully:")
        print(extracted_text)
    else:
        print("No text found or unsupported file format.")
