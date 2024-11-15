import re

class TextProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.text = ""
        self.words = []
        self.ukrainian_words = []
        self.english_words = []
    def load_text(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.text = file.read()
        except FileNotFoundError:
            print("Файл не знайдено.")
        except Exception as e:
            print("Помилка при завантаженні тексту:", str(e))

    def extract_first_sentence(self):
        if self.text:
            first_sentence = re.split(r'(?<=[.!?])\s', self.text)[0]
            return first_sentence
        return ""
    def find_words(self):
        if self.text:
            self.words = re.findall(r'\b[а-яїєіїґa-z]+\b', self.text.lower())
    def classify_words(self):
        self.ukrainian_words = sorted([word for word in self.words if re.match(r'^[а-яїєіїґ]+$', word)])
        self.english_words = sorted([word for word in self.words if re.match(r'^[a-z]+$', word)])
    def print_results(self):
        first_sentence = self.extract_first_sentence()
        if first_sentence:
            print("Перше речення:")
            print(first_sentence)

        if self.ukrainian_words:
            print("\nУкраїнські слова:")
            print(', \n'.join(self.ukrainian_words))
        
        if self.english_words:
            print("\nАнглійські слова:")
            print(', \n'.join(self.english_words))

        print("\nЗагальна кількість слів:", len(self.words))
def main():
    processor = TextProcessor('filename.txt')
    processor.load_text()
    processor.find_words()
    processor.classify_words()
    processor.print_results()
if __name__ == "__main__":
    main()
