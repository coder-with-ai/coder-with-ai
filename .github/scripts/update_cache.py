import re
import datetime

def main():
    # Get today's date in UTC
    today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    print(f"Today's UTC date: {today}")

    # Read README.md
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all instances of v=YYYY-MM-DD with today's date
    new_content = re.sub(r'v=\d{4}-\d{2}-\d{2}', f'v={today}', content)

    # Write back to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ README.md cache busters updated.")

if __name__ == '__main__':
    main()
