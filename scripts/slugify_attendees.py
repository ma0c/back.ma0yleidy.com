INVITEES_LIST = """ma0
leidy
Angie y Walter
Nancy
Blanca y Elvia
Jenid
Libardo y Gloria
Estefanía y Juan Carlos
Silaney y Robinson
Rosa y Adrian
Eric
Cristian
Camilo
Raquel y Camilo
Sebastián Perez
Sofía y David
Ruben y Sergio
Tefa
Nando y Alejandra
Johan
Carolina
Maria Isabel
Carlos y Laura
Ana María
Duber
Bryan y Lorena
Gessiel
Karem
Johana y Mafe
Kevin y Sofia
Juan Carlos y Samuel
Andrea y Carlos
Ivan y Juanes
Wilson y Noelbi
Juan Esteban Bedoya
Nuri Jorge y Jorgito
Robinson y Danny
Samuel y Maria
Hellen
Estefanía y Kathe
Rodrigo
Mari
Gladis
Jose David y Marjorie
Carlos  Andres y Esposa
Yazmin y Nore
Brandon
Javier
Julian
Nates
Zulma
Maria y Alfonso
Dany Mauricio
Juan Esteban Sierra
Walter y Esposa
Maria
Bernice"""


def get_cleaned_invitees_list(invitees_list):
    cleaned_invitees = []
    for invitee in invitees_list.splitlines():
        cleaned_invitee = (
            invitee.strip()
                .replace(" ", "-")
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .lower()
        )
        if cleaned_invitee:
            cleaned_invitees.append(cleaned_invitee)
    return cleaned_invitees


if __name__ == "__main__":
    # print(get_cleaned_invitees_list(INVITEES_LIST))
    print(dict(zip(get_cleaned_invitees_list(INVITEES_LIST), INVITEES_LIST.splitlines())))