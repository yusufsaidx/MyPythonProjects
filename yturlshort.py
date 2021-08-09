print("YOUTUBE URL KISALTICI")
url = input("Youtube url'sini başında http ve www olmadan yazın.")
url2 = url
url = url[19:33]
shrt_url = "https://"+"youtu.be"+url
print(url2+"\n"+shrt_url)