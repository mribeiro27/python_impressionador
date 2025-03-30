def descobrir_servidor(email):
    # Ao invés de botar todos as condições no try, iremos isolar a linha que pode dar o erro que conhecemos. O else só roda caso o try tiver rodado sem problemas
    try:
        posicao_a = email.index('@')
    except:
        raise ValueError("E-mail digitado não possui '@'. Digite seu e-mail novamente.")
    else:
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
        

email = input('Qual o seu e-mail? ')
print(descobrir_servidor(email))
