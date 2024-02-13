import os

def replace_string_in_files(root_path, old_string, new_string, extensions):
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()

                    # Replace all occurrences of old_string with new_string
                    content_new = content.replace(old_string, new_string)

                    # Only write if there is a change in content
                    if content != content_new:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(content_new)
                        print(f'Changes made in: {file_path}')
                except UnicodeDecodeError:
                    print(f'Encoding error in file: {file_path}, skipped.')
                except Exception as e:
                    print(f'Error reading file: {file_path}, Error: {e}')

# Path to the root directory where the search should begin
root_path = '/var/www/html/'

# Old and new strings
old_string = 'OLD.com'
new_string = 'NEW.net'

# File extensions to search for
extensions = ('.txt', '.php', '.css', '.js')

replace_string_in_files(root_path, old_string, new_string, extensions)
