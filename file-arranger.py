import os

# Get path from txt file
f = open("path.txt", "r")
myPath = f.readline() + "\\"
#print (myPath)

# Create empty list for extensions to be added
extensionsList = []

# Get names and extensions of files
myFiles = os.listdir(myPath)

for files in myFiles:
    #print("\nfile = ", files)
    splittedFile = os.path.splitext(files) # Split name of file and extension
    #print("splitted File = ", splittedFile)
    if splittedFile[1] != '':
        extensionsList.append(splittedFile[1]) # Add extensions to list

#print("\nExtensions list: ", extensionsList)

# Convert extensions list to dictionary in order to remove duplicates and then back to another list
uniqueExtensionsList = list(dict.fromkeys(extensionsList))

print("------------")

# Create folders according to unique extensions list
for unique in uniqueExtensionsList:
    try:
        os.mkdir(myPath + unique)
        print("Folder %s created!" % unique)
    except:
        print("Folder %s already exists" % unique)

print("------------")

# Move files to matching folder
for files in myFiles:
    splittedFile2 = os.path.splitext(files)
    if splittedFile2[1] != '':
        os.replace(myPath + files, myPath + splittedFile2[1] + "\\" + files)
        print("File %s moved to %s folder!" % (files, splittedFile2[1]))

print("------------")