import streamlit as st
from streamlit_echarts import st_echarts
import utils

# db_client = utils.SqlClient()

st.set_page_config(
    page_title="QA Job stat",
    page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'Get help': None,
                'About': 'Some description',
                'Report a Bug': None}
)

st.title("Статистика по рынку труда в тестировании ПО", anchor='Top')
st.subheader('Данные по вакансиям раздела "Тестирование" на HH.ru по'
             ' Москве с февраля 2019 г.  по настоящий момент.')

# st.markdown("""
# - [Количество вакансий](#Vacancy-qty)
# - [Заработная плата в зависимости от опыта](#Salary)
# - [Топ 50 работодателей по количеству вакансий](#Top_employers)
#
# Режимы работы
#
# Виды занятости
#
# Требуемый опыт работы
#
# Количество вакансий с указанной зарплатой
#
# 50 наиболее популярных тегов раздела "Ключевые навыки"
#
# Количество упоминаний языков программирования
#
# Фреймворки для юнит-тестирования
#
# Средства нагрузочного тестирования
#
# Инструменты мониторинга
#
# Фреймворки для реализации BDD-подхода
#
# Средства тестирования Web UI
#
# Инструменты тестирования мобильных приложений
#
# Системы управления тестированием, bugtracking system и т.п.
#
# Системы управления версиями
#
# Средства CI/CD
#
# "Облако тегов" на основе текстов вакансий
# """)

# tab1, tab2, tab3 = st.tabs(["По неделям", "По месяцам", "По дням недели"])
#
# with tab1:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#
# with tab2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#
# with tab3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# To create the sidebar
# st.sidebar.markdown('''
# [Оглавление](#Top)
# - [Количество вакансий](#Vacancy-qty)
# - [Зарплаты](#Salary)
# - [Топ 50 работодателей по количеству вакансий](#Top_employers)
# '''
#                     # , unsafe_allow_html=True
#                     )

options = {
    'baseOption': {
        'title':
            {
                'text': 'Языки программирования',
                'subtext': 'Количество упоминаний в текстах вакансий',
                'left': 'center'
            },
        'timeline': {
            # 'axisType': 'category',
            'orient': 'horizontal',
            'autoPlay': True,
            # 'inverse': True,
            'playInterval': 2000,
            # 'left': None,
            # 'right': None,
            'top': '12%',
            # 'bottom': 'top',
            'width': None,
            'height': 40,
            # 'symbol': 'none',
            'data': ['2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01']
        },
        'legend': {
            'top': 'bottom'
        },
        'calculable': True,
        'series': [{
            'name': "Name of series",
            'type': "pie",
            'center': ["50%", "50%"],
            'radius': "55%",
            'label': {'show': False},

        }]
    },
    'options': [
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'percentPrecision': 1,
         'series': [{'data': [{'name': 'Java', 'value': 1881}, {'name': 'Python', 'value': 1294}, {'name': 'C#', 'value': 572}, {'name': 'JavaScript', 'value': 512}, {'name': 'PHP', 'value': 335}, {'name': 'C++', 'value': 275}, {'name': 'Ruby', 'value': 159}, {'name': 'Kotlin', 'value': 145}, {'name': 'Perl', 'value': 86}, {'name': 'Groovy', 'value': 79}, {'name': 'Scala', 'value': 77}, {'name': 'Swift', 'value': 52}, {'name': ' Go ', 'value': 44}, {'name': 'TypeScript', 'value': 39}, {'name': 'VBScript', 'value': 20}, {'name': 'tcl', 'value': 11}, {'name': 'AutoIT', 'value': 8}]}]},
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'series': [{'data': [{'name': 'Java', 'value': 2691}, {'name': 'Python', 'value': 1774}, {'name': 'C#', 'value': 630}, {'name': 'JavaScript', 'value': 623}, {'name': 'Kotlin', 'value': 379}, {'name': 'PHP', 'value': 321}, {'name': 'C++', 'value': 282}, {'name': 'Swift', 'value': 171}, {'name': 'Groovy', 'value': 140}, {'name': 'Ruby', 'value': 132}, {'name': 'TypeScript', 'value': 105}, {'name': 'Scala', 'value': 92}, {'name': 'Perl', 'value': 73}, {'name': ' Go ', 'value': 54}, {'name': 'tcl', 'value': 16}, {'name': 'VBScript', 'value': 2}, {'name': 'AutoIT', 'value': 2}]}]},
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'series': [{'data': [{'name': 'Java', 'value': 4458}, {'name': 'Python', 'value': 3042}, {'name': 'JavaScript', 'value': 1102}, {'name': 'C#', 'value': 1014}, {'name': 'Kotlin', 'value': 717}, {'name': 'PHP', 'value': 524}, {'name': 'C++', 'value': 404}, {'name': 'TypeScript', 'value': 350}, {'name': 'Swift', 'value': 309}, {'name': 'Groovy', 'value': 181}, {'name': 'Scala', 'value': 174}, {'name': 'Ruby', 'value': 169}, {'name': ' Go ', 'value': 140}, {'name': 'Perl', 'value': 96}, {'name': 'tcl', 'value': 25}, {'name': 'VBScript', 'value': 12}, {'name': 'AutoIT', 'value': 3}]}]},
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'series': [{'data': [{'name': 'Java', 'value': 4007}, {'name': 'Python', 'value': 2837}, {'name': 'JavaScript', 'value': 838}, {'name': 'C#', 'value': 782}, {'name': 'Kotlin', 'value': 656}, {'name': 'PHP', 'value': 384}, {'name': 'TypeScript', 'value': 362}, {'name': 'C++', 'value': 311}, {'name': 'Swift', 'value': 285}, {'name': 'Groovy', 'value': 185}, {'name': 'Ruby', 'value': 138}, {'name': 'Scala', 'value': 138}, {'name': ' Go ', 'value': 90}, {'name': 'Perl', 'value': 54}, {'name': 'tcl', 'value': 17}, {'name': 'VBScript', 'value': 9}, {'name': 'AutoIT', 'value': 4}]}]}
    ],

}


st_echarts(options=options,
           height='600px',
           # width='400px',
           renderer='svg')


st.header('Количество вакансий', anchor='Vacancy-qty')

data = [['Неделя', 'количество вакансий'],
        ['52', 201], ['1', 643], ['2', 1494],
        ['3', 1542], ['4', 1532], ['5', 1542],
        ['6', 1611], ['7', 1539], ['8', 1385],
        ['9', 1391], ['10', 1065], ['11', 1237],
        ['12', 1083], ['13', 1084], ['14', 1111],
        ['15', 1022], ['16', 928], ['17', 875],
        ['18', 712], ['19', 784], ['20', 907],
        ['21', 859], ['22', 870], ['23', 825],
        ['24', 765], ['25', 813], ['26', 705],
        ['27', 707], ['28', 695], ['29', 673],
        ['30', 717], ['31', 749], ['32', 746],
        ['33', 726], ['34', 694], ['35', 731],
        ['36', 713], ['37', 720], ['38', 682],
        ['39', 675], ['40', 724], ['41', 762],
        ['42', 742], ['43', 648], ['44', 0],
        ['45', 0], ['46', 0]]

options = {
    'title': {
        'text': 'по неделям'
    },
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    "dataset": {
        "source": data
    },
    "xAxis": {"type": "value"},
    "yAxis": {"type": "category",
              'axisTick': {'show': False}},
    "series": [{"type": "bar"}]
}
st_echarts(options=options, height='600px')

data = [['Месяц', '2019', '2020', '2021', '2022'],
        ['январь', 0, 1400, 1417, 2321],
        ['февраль', 0, 1476, 1581, 2509],
        ['март', 1836, 1393, 1886, 2191],
        ['апрель', 2085, 1043, 1933, 1777],
        ['май', 1978, 1072, 1759, 1587],
        ['июнь', 1925, 1091, 2049, 1513],
        ['июль', 2064, 1160, 2175, 1410],
        ['август', 1615, 1303, 2234, 1539],
        ['сентябрь', 1250, 1411, 2410, 1433],
        ['октябрь', 1445, 1491, 2417, 1428],
        ['ноябрь', 1340, 1484, 2429, 0],
        ['декабрь', 1221, 1344, 2250, 0]]

options = {
    'title': {
        'text': 'по месяцам и годам'
    },
    'legend': {
        'orient': 'horizontal',
        'align': 'left',
        'center': 0,
        'top': 'bottom'
    },
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    "dataset": {
        "source": data
    },
    "xAxis": {},
    "yAxis": {"type": "category",
              'axisTick': {'show': False},
              'axisLabel': {'rotate': 50},
              },
    "series": [{"type": "bar"}, {"type": "bar"},
               {"type": "bar"}, {"type": "bar"}]
}
st_echarts(options=options, height='500px', width='115%',
           renderer='svg')

st.header('Зарплаты', anchor='Salary')
st.markdown("""Текст и графики про зарплаты""")

st.header('Топ 50 работодателей по количеству вакансий', anchor='Top_employers')
st.markdown("""Текст и графики про зарплаты""")




