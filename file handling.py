# mkdir -> to create a new folder / directory
 
# rmdir -> to remove any folder / directory 

# File 
# x -> this mode will only create the file and if already FileExistsError we  will get an error back
# w -> agar file exists nahi kar rhi hai so this mode will create one and insert the File
# a -> add the text at the last 
# r  -> read the content inside of the file 
# # mode1: x-> just to create the file 
# open ("Garba.txt","X")

# # mode 2: W -> if there is any content inside the file so the new one will replace old one
# # file = open ("Garba.txt","w")
# file.write ("kehlo garba khub kehlo din raat khelo ")


# #cmode 3 : a -> add the text at the last 
# file = open ("Garba.text","a")
# file.write ("\n This message is newly added")

# # mode 4 : r -> read the content inside of 
# file = open ("garba.txt","r")
# print(file.read())

# with open ("Sample.txt","W") as file:
#     'file . write ("This is new file") # no one can assice 

# crud -> Create , Read , Update , delete
# os.remove ("garba.tet")
# print ("pressn 1 for creating a new file:")
# print("press 2 for reading any file:")
# print("press 3 for updating any file:")
# print("press 4 for deleting any file":)



