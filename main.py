import requests,json, xlsxwriter




if __name__ == "__main__":
    seller_id = ["GAUSS+ONLINE", "ALTAVISTA+COMPUTACION"]
    site_id = "MLA"


    row=1
    col=0
    libro = xlsxwriter.Workbook("log.xlsx")
    hoja = libro.add_worksheet()
    columnas = ["Id", "Titulo", "Categoria_Id", "Vendedor"]
    hoja.write_row("B1", columnas)


    for seller in seller_id:
        url = "https://api.mercadolibre.com/sites/" + site_id + "/search?nickname=" + seller
        response = requests.get(url)
        lista = []
        if response.status_code == 200:
            payloads = response.json()

            #aAgrega los resultados de la peticion a una lista
            for element in payloads["results"]:
                log = (element["id"], element["title"], element["category_id"])
                lista.append(log)
            #Usa la lista para escribir un excel.
            for id, title, category_id in lista:
                hoja.write(row, col+  1, id)
                hoja.write(row, col + 2, title)
                hoja.write(row, col + 3, category_id)
                hoja.write_string(row,col+4, seller)
                row += 1
        #Muestra el mensaje de error
        else:
            payloads = response.json()
            print(payloads)

    libro.close()



