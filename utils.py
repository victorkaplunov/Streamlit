from datetime import date, timedelta
import sqlalchemy as sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import select
today = date.today() - timedelta(days=6)
first_day_of_current_year = date(date.today().year, 1, 1)


def years_tuple():
    return 2019, 2020, 2021, 2022


# class SqlClient:
#     def __init__(self):
#         self.engine = sqlalchemy.create_engine(
#             'sqlite:///testdb.db',
#             connect_args={'check_same_thread': False},
#             encoding='utf8'
#         )
#         self.connection = self.engine.connect()
#         self.metadata = sqlalchemy.MetaData()
#         self.charts = sqlalchemy.Table('charts', self.metadata,
#                                        autoload=True, autoload_with=self.engine
#                                        )
#
#     def languages(self):
#         """Отдает один идентификатор новости (первой по счету)."""
#         with Session(bind=self.connection.engine) as session:
#             response = session.execute(
#                 select(self.charts.columns.data,
#                        self.charts.columns.popularity,
#                        self.charts.columns.year)
#                 .where(self.charts.columns.chart_name == 'languages')) \
#                 .all()
#         response_list_of_lists = list([['Language', 'Popularity', 'Year']])
#         for row in response:
#             response_list_of_lists.append([
#                 row['data'], row['popularity'], row['year']]
#             )
#         output = list(response_list_of_lists)
#         print(output)
#         return output


def get_vacancy_count_by_year(cursor):
    month_tuples = (('01', 'январь', '31'), ('02', 'февраль', "29"), ('03', 'март', '31'),
                    ('04', 'апрель', '30'), ('05', 'май', '31'), ('06', 'июнь', '30'),
                    ('07', 'июль', '31'), ('08', 'август', '31'), ('09', 'сентябрь', '30'),
                    ('10', 'октябрь', '31'), ('11', 'ноябрь', '30'), ('12', 'декабрь', '31'))

    year_tuple = years_tuple()
    head_time_series = [['Месяц']]
    output_list = []
    for y in year_tuple:
        head_time_series[0].append(str(y))
        for n, month in enumerate(month_tuples):
            # Запрашиваем количество вакансий за месяц
            sql = f'''
            SELECT DISTINCT id FROM calendar WHERE data 
            BETWEEN "{str(y)}-{month[0]}-01T00:00:00+03:00" and "{str(y)}-{month[0]}-{month[2]}T23:59:59+03:00";'''
            cursor.execute(sql)
            vacancies_tuple = (cursor.fetchall())
            if str(y) == '2019':
                # Данные за февраль неполные, поэтому вместо них пишем ноль
                if month[1] == 'февраль':
                    output_list.append([month[1], 0])
                else:
                    output_list.append([month[1], len(vacancies_tuple)])
            else:
                output_list[n].append(len(vacancies_tuple))
    output_list = head_time_series + output_list
    return output_list