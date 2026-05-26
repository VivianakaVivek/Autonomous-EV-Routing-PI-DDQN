import PyPDF2

pdfs = ['DDQN M-2.pdf', 'DDQN M-3.pdf', 'DDQN M-4.pdf', 'Model M-5.pdf', 'Model M-6.pdf']
base_path = 'c:/Users/ASUS/OneDrive/Desktop/BTP/Research EV/'

with open('pdf_output_utf8.txt', 'w', encoding='utf-8') as f:
    for p in pdfs:
        f.write(f'\n--- {p} --- \n')
        reader = PyPDF2.PdfReader(base_path + p)
        for page in reader.pages:
            f.write(page.extract_text() + '\n')
