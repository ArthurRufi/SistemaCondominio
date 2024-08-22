def validacaoDeCaractere(argumento):
    
    antiCaractere = ["'", ".", "-", "_", ";", 'FROM', 'DELETE']
    if argumento in antiCaractere:
        print ('xxxxxx')
        return False
    else:
        return True
    

#adicionar logica para duplicacao no banco de dados
    