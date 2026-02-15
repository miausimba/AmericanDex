import os
import re

def replace_in_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return

    # Replacements for contents
    replacements = [
        (r'americandex', 'universedex'),
        (r'AmericanDex', 'UniverseDex'),
        (r'AMERICANDEX', 'UNIVERSEDEX'),
        (r'Americandex', 'Universedex'),
        (r'american', 'universe'),
        (r'American', 'Universe'),
        (r'AMERICAN', 'UNIVERSE'),
    ]

    new_content = content
    for pattern, replacement in replacements:
        new_content = re.sub(pattern, replacement, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated content in: {filepath}")

def rename_items(root_dir):
    # Rename directories and files
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files + dirs:
            old_path = os.path.join(root, name)
            new_name = name
            
            # Application of replacements to the name
            # We use a case-insensitive replacement for filenames if necessary,
            # but usually it's better to be specific.
            # However, the user asked to change EVERYTHING.
            
            new_name = new_name.replace('americandex', 'universedex')
            new_name = new_name.replace('AmericanDex', 'UniverseDex')
            new_name = new_name.replace('AMERICANDEX', 'UNIVERSEDEX')
            new_name = new_name.replace('Americandex', 'Universedex')
            new_name = new_name.replace('american', 'universe')
            new_name = new_name.replace('American', 'Universe')
            new_name = new_name.replace('AMERICAN', 'UNIVERSE')

            if new_name != name:
                new_path = os.path.join(root, new_name)
                # If new_path already exists (shouldn't really happen with topdown=False), handle it
                if os.path.exists(new_path):
                    print(f"Warning: {new_path} already exists, skipping rename of {old_path}")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

def process_all(root_dir):
    # First update content
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file == 'rename_to_universe.py':
                continue
            replace_in_content(os.path.join(root, file))
    
    # Then rename
    rename_items(root_dir)

if __name__ == "__main__":
    target_dir = r"c:\Users\USER\Downloads\dexprueba"
    process_all(target_dir)
