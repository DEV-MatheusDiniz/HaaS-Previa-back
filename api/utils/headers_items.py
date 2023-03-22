def headersItems( data ):

    headers = []

    items = []

    for item in data:

        items.append(item['js_contabilizado'])

        for js_contabilizado in item['js_contabilizado']:

            listaIndex = []

            for index in js_contabilizado:

                listaIndex.append({"text": index, "value": index})

            headers.append(listaIndex)

            break

        items.append(item['js_nao_contabilizado'])

        for js_contabilizado in item['js_nao_contabilizado']:

            listaIndex = []

            for index in js_contabilizado:

                listaIndex.append({"text": index, "value": index})

            headers.append(listaIndex)

            break

        items.append(item['js_condicional'])

        for js_contabilizado in item['js_condicional']:

            listaIndex = []

            for index in js_contabilizado:

                listaIndex.append({"text": index, "value": index})

            headers.append(listaIndex)

            break

        items.append(item['js_diversidade'])

        for js_contabilizado in item['js_diversidade']:

            listaIndex = []

            for index in js_contabilizado:

                listaIndex.append({"text": index, "value": index})

            headers.append(listaIndex)

            break

    return { "headers": headers, "items": items }
