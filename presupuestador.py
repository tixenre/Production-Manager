import gspread
from gspread.models import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import costos
import math

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Presupuestador").sheet1  # Open the spreadhseet


headers = list(sheet.row_values(1))
nombre_col = 1
variante_col = 2
hs_col = 3
gr_col = 4
costo_col = 5
ganancia_col = 6
precio_col= 7


#range(10)
#range(len(sheet.col_values(1)))
for i in range(len(sheet.col_values(1))):
    a=sheet.cell(i+2,hs_col).numeric_value
    b=sheet.cell(i+2,gr_col).numeric_value

    sheet.update_cell(i+2,precio_col,math.ceil(costos.tiendanube(a,b)))
    sheet.update_cell(i+2,costo_col,math.ceil(costos.gasto(a,b)))
    sheet.update_cell(i+2,ganancia_col,math.ceil(costos.ganancia(a,b)))