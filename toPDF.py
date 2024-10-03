from fpdf import FPDF
import unicodedata

variation = "western"

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'The Book of Mormon - ' + variation, 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Times', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, body)  # Use multi_cell for text wrapping
        # Remove the extra line break to make it more compact
        # self.ln()  # This line is removed

def clean_text(text):
    # Normalize text to remove special characters
    normalized_text = unicodedata.normalize('NFKD', text)
    return normalized_text.encode('ascii', 'ignore').decode('utf-8')  # Remove non-ASCII characters

def main():
    books = [
        {"numOfChapters": 22, "bookName": "1 Nephi", "urlName": "1-nephi"},
        {"numOfChapters": 33, "bookName": "2 Nephi", "urlName": "2-nephi"},
        {"numOfChapters": 7, "bookName": "Jacob", "urlName": "jacob"},
        {"numOfChapters": 1, "bookName": "Enos", "urlName": "enos"},
        {"numOfChapters": 1, "bookName": "Jarom", "urlName": "jarom"},
        {"numOfChapters": 1, "bookName": "Omni", "urlName": "omni"},
        {"numOfChapters": 1, "bookName": "Words of Mormon", "urlName": "words-of-mormon"},
        {"numOfChapters": 29, "bookName": "Mosiah", "urlName": "mosiah"},
        {"numOfChapters": 63, "bookName": "Alma", "urlName": "alma"},
        {"numOfChapters": 16, "bookName": "Helaman", "urlName": "helaman"},
        {"numOfChapters": 30, "bookName": "3 Nephi", "urlName": "3-nephi"},
        {"numOfChapters": 1, "bookName": "4 Nephi", "urlName": "4-nephi"},
        {"numOfChapters": 9, "bookName": "Mormon", "urlName": "mormon"},
        {"numOfChapters": 15, "bookName": "Ether", "urlName": "ether"},
        {"numOfChapters": 10, "bookName": "Moroni", "urlName": "moroni"}
    ]

    pdf = PDF()
    pdf.add_page()

    for book in books:
        pdf.chapter_title(book['bookName'])  # Use bookName from the Book object
        for chapter in range(1, book['numOfChapters'] + 1):
            path = f'bom-{variation}/{book["urlName"]}/{chapter}.txt'
            with open(path, 'r', encoding='utf-8') as file:
                verses = [line.strip() for line in file.readlines() if line.strip()]
            
            pdf.chapter_title(f"{book['bookName']} Chapter {chapter}")  # Chapter title
            for verse_num, verse in enumerate(verses, start=1):
                cleaned_verse = clean_text(f"{verse_num}. {verse}")  # Clean the verse text
                pdf.chapter_body(cleaned_verse)  # Verse number and text

    pdf.output(f"bom-{variation}.pdf")

main()
