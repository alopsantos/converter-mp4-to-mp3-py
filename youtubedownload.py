from pytube import YouTube


arquivo = open(
    "youtube.txt")
produtos = arquivo.readlines()
arquivo.close()


for index in range(len(produtos)):
    produtos[index] = produtos[index].rstrip('\n')
    produto = produtos[index]
    print(produto)

    YouTube(produto).streams.first().download()
    yt = YouTube(produto)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download()
