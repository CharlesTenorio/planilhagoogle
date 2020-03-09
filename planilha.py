import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Planinha():
    '''Lista dados de um planilha do google docs'''
    def __init__(self, id_planilha):

        self.scope =['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('viralizeplanilha-25f139a16dde.json'
                                                                          , self.scope)
        self.qtd_registros = 0
        self.gc = gspread.authorize(self.credentials)
        self.id_planilha = id_planilha
        self.wks = self.gc.open_by_key(self.id_planilha)

    def lista_lead(self):
        '''Retorna uma lista de todos os intens da planinha'''
        worksheet = self.wks.get_worksheet(0)
        list_of_lists = worksheet.get_all_values()
        return list_of_lists
