import time

name = input("Enter your name:")
print("Welcome" + name +"\n you will now see new articles here")
print("Extracting hyperlinks...")
time.sleep(2)
print()
content_string=get_content_string("https://www.nytimes.com/section/technology")


