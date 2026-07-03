import re
import time

def main():
    # Get current Unix timestamp
    timestamp = str(int(time.time()))
    print(f"Current Unix timestamp: {timestamp}")

    # Read README.md
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all instances of v=YYYY-MM-DD or v=timestamp with the new timestamp
    new_content = re.sub(r'v=\d{4}-\d{2}-\d{2}|v=\d+', f'v={timestamp}', content)

    # Write back to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ README.md cache busters updated.")

if __name__ == '__main__':
    main()
