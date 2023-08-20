def crear_playlist(lineas, genero):
    playlist = []
    for linea in lineas:
        cancion = linea.split(";")
        # [0] -> nombreCancion
        # [1] -> Artistas(Artista1-Artista2-...)
        # [2] -> Album
        # [3] -> Generos(Genero1-Genero2-...)
        # [4] -> Duracion(Min:Seg)
        generos = cancion[3].split("-")
        if genero in generos:
            playlist.append(cancion[0])
    return playlist


lineas = ['Despacito;Luis Fonsi-Daddy Yankee;Vida;Reggaeton-Pop latino;3:47\n',
'Clandestino;Shakira-Maluma;El Dorado;Pop latino-Reggaeton;3:16\n',
'Spring Day;BTS;You Never Walk Alone;Kpop;4:34\n',
'Mr. Brighside;The Killers;Hot Fuss;Rock alternativo-Pop rock;3:43\n',
'Love The Way You Lie;Eminem-Rihanna;Recovery;Hip hop-Pop;4:23\n',
'Please Please Me;The Beatles;Please Please Me;Rock and roll;2:00\n',
"Sweet Child o' Mine;Guns N' Roses;Appetite for Destruction;Rock alternativo;5:56\n",
'I Like It;Cardi B-Bad Bunny-J Balvin;Invision of Privacy;Trap latino;4:13\n',
'Ciega, Sordomuda;Shakira;¿Donde estan los ladrones?;Pop latino;4:28\n']
print(crear_playlist(lineas, "Pop"))
