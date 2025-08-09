def analyze_log_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        total = len(lines)
        error = warning = info = 0

        for line in lines:
            line = line.strip().lower()
            if 'error' in line:
                error += 1
            elif 'warning' in line:
                warning += 1
            elif 'info' in line:
                info += 1

        # Determine the most frequent type
        types = {'ERROR': error, 'WARNING': warning, 'INFO': info}
        most_frequent = max(types, key=types.get)

        print(f"\n--- Log File Summary ---")
        print(f"Total Entries      : {total}")
        print(f"Info Entries       : {info}")
        print(f"Warning Entries    : {warning}")
        print(f"Error Entries      : {error}")
        print(f"-------------------------")
        print(f"Most Frequent Type : {most_frequent}")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Main
filename = input("Enter log filename: ")
analyze_log_file(filename)
