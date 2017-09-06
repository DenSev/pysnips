import urllib

urls_list = open("E://new_5.txt", "r").readlines()
num_downloaded = 671.0

for url in urls_list.__getslice__(671, len(urls_list)-1):
    filename = url.split("/")
    filename = filename[filename.__len__() - 1]
    filename = filename.replace("\n", "")
    file_to_download = urllib.URLopener()
    file_to_download.retrieve(url, "D://mr-ndc/" + filename)
    num_downloaded += 1

    percent = num_downloaded / urls_list.__len__()

    print percent.__str__() + "%, num downloaded: " + num_downloaded.__str__()
