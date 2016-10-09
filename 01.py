listaComentarios=[]

def agregarComentario(comentario):
    listaComentarios.append(comentario)


if __name__=="__main__":
    comentario=input("Como se sientes?")
    agregarComentario(comentario)
    recibirNotificaciones=input("Desea recibir notificaciones?")
    
    note=""
    if recibirNotificaciones=='si':
        note+=", recibirá notificaciones :)"
    else :
        note+=", no recibirá notificaciones :("

    print("Muchas gracias ",note)