### Extensions 

This code prompts the user to input a file name and determines the corresponding MIME type based on the file extension. Here's a breakdown of the code:

The user is prompted to enter a file name using the input() function. The message "File name:" is displayed to the user.

The lower() function is used to convert the user's input to lowercase, ensuring that the code can handle different casing variations.

The strip() function is applied to remove any leading or trailing whitespace from the input, ensuring that the comparison works correctly.

The code checks the file name using a series of conditional statements:

a. If the file name ends with ".gif" (e.g., "image.gif", "animated.gif"), the condition fileName.endswith(".gif") evaluates to True. In this case, the code executes the corresponding block and prints "image/gif".

b. If the file name ends with ".jpg" (e.g., "photo.jpg", "picture.jpg"), the condition fileName.endswith(".jpg") evaluates to True. The code then prints "image/jpg".

c. If the file name ends with "jpeg" (e.g., "image.jpeg", "photo.jpeg"), the condition fileName.endswith("jpeg") evaluates to True. The code then prints "image/jpeg".

d. If the file name ends with ".png" (e.g., "image.png", "logo.png"), the condition fileName.endswith(".png") evaluates to True. The code then prints "image/png".

e. If the file name ends with ".pdf" (e.g., "document.pdf", "report.pdf"), the condition fileName.endswith(".pdf") evaluates to True. The code then prints "image/pdf".

f. If the file name ends with ".txt" (e.g., "text.txt", "note.txt"), the condition fileName.endswith(".txt") evaluates to True. The code then prints "image/txt".

g. If the file name ends with ".zip" (e.g., "archive.zip", "compressed.zip"), the condition fileName.endswith(".zip") evaluates to True. The code then prints "image/zip".

h. If none of the above conditions are met, meaning the file name does not end with any of the specified extensions, the code executes the final else block and prints "application/octet-stream".

The purpose of this code is to determine the MIME type of a file based on its extension. The code covers several common file types but can be expanded to include additional MIME types and corresponding file extensions as needed.

