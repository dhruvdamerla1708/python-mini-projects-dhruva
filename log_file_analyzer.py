import string

def analyze_log_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('❌ File not found:', filename)
        return

    total_lines = len(lines)
    total_words = 0
    total_chars = 0
    word_freq = {}
    unique_words = set()

    error_count = 0
    warning_count = 0
    info_count = 0

    for line in lines:
        clean_line = line.strip()
        total_chars += len(clean_line)
        words = clean_line.translate(str.maketrans('', '', string.punctuation)).lower().split()
        total_words += len(words)
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
            unique_words.add(word)

        # Simple log level detection
        if 'error' in words:
            error_count += 1
        if 'warning' in words:
            warning_count += 1
        if 'info' in words:
            info_count += 1

    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_words[:5]

    # Display Summary
    print('\n📁 Log File Analyzer')
    print('----------------------------')
    print(f'Enter log filename: {filename}\n')
    print(f'✅ Total Lines       : {total_lines}')
    print(f'🧾 Total Words       : {total_words:,}')
    print(f'🔠 Total Characters  : {total_chars:,}')
    print(f'🔁 Total Unique Words: {len(unique_words)}')
    print(f'💥 Error Entries     : {error_count}')
    print(f'⚠️  Warning Entries   : {warning_count}')
    print(f'ℹ️  Info Entries      : {info_count}\n')

    # Save summary to file
    with open('summary_report.txt', 'w') as f:
        f.write('📁 Log File Analyzer Summary\n')
        f.write('----------------------------\n')
        f.write(f'Total Lines       : {total_lines}\n')
        f.write(f'Total Words       : {total_words}\n')
        f.write(f'Total Characters  : {total_chars}\n')
        f.write(f'Total Unique Words: {len(unique_words)}\n')
        f.write(f'Error Entries     : {error_count}\n')
        f.write(f'Warning Entries   : {warning_count}\n')
        f.write(f'Info Entries      : {info_count}\n\n')
        
    print('\n✅ Summary saved to: summary_report.txt')

# Run the analyzer
if __name__ == '__main__':
    filename = input('Enter log filename: ')
    analyze_log_file(filename)
