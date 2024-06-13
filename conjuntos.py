Calabria = set({"Catanzaro", "Cosenza", "Crotona", "Reggio de Calabria", "Vibo Valentia"})
Campania = set({"Avellino", "Benevento", "Caserta", "Napoli", "Salerno"})
Lacio = set({"Frosinone", "Latina", "Rieti", "Roma", "Viterbo"})
Liguria = set({"Genova", "Imperia", "La Spezia", "Savona"})
Lucania = set({"Matera", "Potenza"})
Molise = set({"Campobasso", "Isernia"})
Toscana = set({"Arezzo", "Florencia", "Grosseto", "Livorno", "Lucca", "Massa-Carrara", "Pisa"})
Pistoia = set({"Prato", "Siena"})
Umbria = set({"Perusa", "Terni"})
Veneto = set({"Belluno", "Padua", "Rovigo", "Treviso", "Venecia", "Verona", "Vicenza"})
# La siguiente tupla nos servirá para poder utilizar cada uno de los conjuntos en un bucle,
# además del nombre del conjunto en modo texto para poder mostrarlo en pantalla.
tuplaregiones = (Calabria, "Calabria", Campania, "Campania", Lacio, "Lacio",
Liguria, "Liguria", Lucania, "Lucania", Molise, "Molise", Toscana, "Toscana",
Pistoia, "Pistoia", Umbria, "Umbria", Veneto, "Veneto")


def localiza(region):
    if provincia in region:
        return True
    else:
        return False


def formapais(regi):
    regi.remove(provincia)
    print("\nSus provincias son (excepto la que ha indicado):")
    for nombre in regi:
        print(nombre.ljust(20), end="")
    Italia = set()
    Italia.update(Calabria, Campania, Lacio, Liguria, Lucania, Molise, Toscana, Pistoia, Umbria, Veneto)
    print("\n\nLas provincias de Italia en conjunto son:")
    for nombre in Italia:
        print(nombre.ljust(20), end="")

provincia = input("Escriba la provincia italiana: ")
region = ""
contador = 0
# Vamos obteniendo cada conjunto para localizar en su interior la
# provincia indicada, gracias a la tupla definida anteriormente
while contador < len(tuplaregiones):
    if localiza(tuplaregiones[contador]):
        region = tuplaregiones[contador]
        txtregion = tuplaregiones[contador + 1]
    contador = contador + 2
# Si la variable region no ha cambiado su valor inicial, significa que no se ha encontrado la provincia indicada.
if region == "":
    print("\nLa región de %s no se ha encontrado." % provincia)
else:
    print("\nLa región de %s es %s" % (provincia, txtregion))
    formapais(region)
