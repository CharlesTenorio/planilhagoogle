import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Planilha():
    '''Lista dados de um planilha do google docs'''
    def __init__(self, id_planilha):

        self.scope =['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('g-viralize-ee853d25a650.json'
                                                                          , self.scope)
        self.qtd_registros = 0
        self.gc = gspread.authorize(self.credentials)
        self.id_planilha = id_planilha
        self.wks = self.gc.open_by_key(self.id_planilha)

    def get_lista_lead(self):
        '''Retorna uma lista de todos os intens da planinha'''
        worksheet = self.wks.get_worksheet(0)
        list_of_lists = worksheet.get_all_values()
        return list_of_lists

    def get_qtd_registro(self):
        cont = len(self.get_lista_lead())
        return cont
