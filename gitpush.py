import os

os.system("git init") # Initialize a git repository
os.system("git add .") # Add all files to the repository
os.system("git commit -m 'Handwrittings'") # Commit the changes
os.system("git remote add origin https://github.com/tecsantoshkumar/Handwrittings.git") # Add a remote repository
os.system("git push -u origin master") # Push the changes to the remote repository
