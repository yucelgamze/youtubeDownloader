import pytube

url: str = input("enter the link of which video you would like to download: ")

path = " "

pytube.YouTube(url).streams.get_highest_resolution().download(path)