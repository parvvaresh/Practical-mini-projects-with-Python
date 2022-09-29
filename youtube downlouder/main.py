from pytube import YouTube


link = input("Enter the link: ")


def dl(link):
    yt = YouTube(link)
    print("-->information")
    print("---->Title: ",yt.title)
    print("---->Number of views: " ,yt.views)
    print("---->Length of video: ",yt.length,"secend")
    print("---->Description: ",yt.description)
    print("---->Ratings: ",yt.rating)
    user = input("are you download this video ?? [Y/N]")

    if user.upper() == "Y":
        
        ys = yt.streams.get_highest_resolution()

        print("Downloading...")
        ys.download()
        print("Download completed!!")
        

dl(link)