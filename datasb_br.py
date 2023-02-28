from datetime import datetime, timedelta

class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano =[
            'Janeiro', 'Fevereiro', 'Março',
            'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        lista_dia_semana = [
        'Segunda', 'Terça', 'Quarta',
        'Suinta', 'Sexta', 'Sábado', 'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return lista_dia_semana[dia_semana]

    def format_data(self):
        print('')
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro