
def save_report(data):
    # GOOD: Using 'with' ensures the file closes automatically
    with open('report.txt', 'w') as f:
        f.write(data)
