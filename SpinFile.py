# HeeSeo Lee(1527190), Andy Jeon (u1528909)
# https://github.com/UoU-UAC/a4-word-spinner-persona
# https://github.com/Andy615534/WordSpinnerProject

from Spinner import Spinner

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    text = ''.join([c for c in text if c.isalpha() or c.isspace()])
    return text

def main():
    essay_file = 'essay.txt'
    synonym_file = 'test-synonyms.txt'

    spinner = Spinner(synonym_file)
    original_text = process_text(essay_file)

    print("Original:", original_text)

    for i in range(1, 4):
        spun_text = spinner.spin_text(original_text)
        print(f"Option {i}:", spun_text)

if __name__ == "__main__":
    main()
