import os

directory = '/home/joemull/git/memory-alpha/content/old-docs'

chars_to_replace = ['_', ' ']
char_to_use = '-'

print("Renaming files now!")
for root, dirs, files in os.walk(directory):
    print(f"root: {root}")
    print(f"dirs: {dirs}")
    print(f"files: {files}")

    for current_filename in files:
        for char in chars_to_replace:
            new_filename = current_filename.replace(char, char_to_use)
            if current_filename != new_filename:
                print(f"current filename: {current_filename}")
                print(f"    new filename: {new_filename}")
                os.rename(
                    os.path.join(root, current_filename),
                    os.path.join(root, new_filename)
                )

print("All done!")
