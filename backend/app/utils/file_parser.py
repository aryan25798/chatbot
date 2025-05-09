import textract

def parse_file(file_content: bytes):
    text = textract.process(file_content)
    return text.decode("utf-8")
