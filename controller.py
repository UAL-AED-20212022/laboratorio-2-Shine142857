from models.LinkedList import LinkedList

def RPI(minha_lista, comando):
    minha_lista.insert_at_start(comando[1])
    return minha_lista

def RPF(minha_lista, comando):
    minha_lista.insert_at_end(comando[1])
    return minha_lista

def RPDE(minha_lista, comando):
    minha_lista.insert_after_item(comando[2],comando[1])
    return minha_lista

def RPAE(minha_lista, comando):
    minha_lista.insert_before_item(comando[2],(comando[1]))
    return minha_lista

def RPII(minha_lista, comando):
    minha_lista.insert_at_index(int(comando[2]),comando[1])
    return minha_lista

def VNE(minha_lista,comando):
    return minha_lista.get_count()

def VP(minha_lista, comando):
    return minha_lista.search_item(comando[1])

def EPE(minha_lista, comando):
    return minha_lista.delete_at_start()

def EUE(minha_lista, comando):
    minha_lista.delete_at_end()
    return minha_lista

def EP(minha_lista, comando):
    minha_lista.delete_element_by_value(comando[1])
    return minha_lista

