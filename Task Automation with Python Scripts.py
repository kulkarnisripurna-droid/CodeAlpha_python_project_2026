import os
import shutil
import re
import requests

# Create folders
if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists("backup"):
    os.mkdir("backup")

# Webpage URL
url = "https://example.com"

# Download webpage content
response = requests.get(url)

# Save webpage content to a file
with open("data/webpage.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Webpage saved successfully!")

# Read saved file
with open("data/webpage.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Extract email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save emails to another file
with open("data/emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")

# Copy email file to backup folder
shutil.copy("data/emails.txt", "backup/emails_backup.txt")

print("Backup created successfully!")

# Display total emails found
print("Total Emails Found:", len(emails))