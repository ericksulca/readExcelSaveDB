from django.shortcuts import render

from django.http import HttpResponse
import json
import openpyxl

# Create your views here.
def Home(request):
    # Specify the path to your XLSX file
    file_path = './filesExcel/Lista_clientes.xlsx'

    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)

    # Get the active sheet (or a specific sheet by name: workbook['SheetName'])
    sheet = workbook.active

    # Iterate through rows and print cell values
    json_clientes = []
    cnt = 1
    for row in sheet.iter_rows(min_row=3,min_col=2):
        oCliente = {
            'cnt': cnt,
            'nombre': row[0].value,
            'direccion': row[1].value,
            'nro_documento': row[2].value,
            'telefono': row[3].value,
        }
        cnt += 1
        json_clientes.append(oCliente)
        print()
    #return HttpResponse(json.dumps({'exito':1}), content_type="application/json")
    return HttpResponse(json.dumps(json_clientes), content_type="application/json")

