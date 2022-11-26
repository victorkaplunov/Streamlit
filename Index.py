import streamlit as st
from streamlit_echarts import st_echarts
import utils

# db_client = utils.SqlClient()

st.set_page_config(
    page_title="QA Job stat",
    page_icon="🧊",
    layout="wide",
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
st.sidebar.markdown('''
[Оглавление](#Top)
- [Количество вакансий](#Vacancy-qty)
- [Зарплаты](#Salary)
- [Топ 50 работодателей по количеству вакансий](#Top_employers)
'''
                    # , unsafe_allow_html=True
                    )

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

# st.header('Количество упоминаний языков программирования')
# st.markdown("""Количество упоминаний языков программирования""")

# data = db_client.languages()
data = [['Language', 'Popularity', 'Year'], ['Java', 1881, 2019], ['Python', 1294, 2019], ['JavaScript', 512, 2019], ['C#', 572, 2019], ['PHP', 335, 2019], ['C++', 275, 2019], ['Ruby', 159, 2019], ['Groovy', 79, 2019], [' Go ', 44, 2019], ['Scala', 77, 2019], ['Swift', 52, 2019], ['Kotlin', 145, 2019], ['TypeScript', 39, 2019], ['VBScript', 20, 2019], ['tcl', 11, 2019], ['Perl', 86, 2019], ['AutoIT', 8, 2019], ['Java', 2691, 2020], ['Python', 1774, 2020], ['JavaScript', 623, 2020], ['C#', 630, 2020], ['PHP', 321, 2020], ['C++', 282, 2020], ['Ruby', 132, 2020], ['Groovy', 140, 2020], [' Go ', 54, 2020], ['Scala', 92, 2020], ['Swift', 171, 2020], ['Kotlin', 379, 2020], ['TypeScript', 105, 2020], ['VBScript', 2, 2020], ['tcl', 16, 2020], ['Perl', 73, 2020], ['AutoIT', 2, 2020], ['Java', 4458, 2021], ['Python', 3042, 2021], ['JavaScript', 1102, 2021], ['C#', 1014, 2021], ['PHP', 524, 2021], ['C++', 404, 2021], ['Ruby', 169, 2021], ['Groovy', 181, 2021], [' Go ', 140, 2021], ['Scala', 174, 2021], ['Swift', 309, 2021], ['Kotlin', 717, 2021], ['TypeScript', 350, 2021], ['VBScript', 12, 2021], ['tcl', 25, 2021], ['Perl', 96, 2021], ['AutoIT', 3, 2021], ['Java', 3713, 2022], ['Python', 2652, 2022], ['JavaScript', 784, 2022], ['C#', 725, 2022], ['PHP', 367, 2022], ['C++', 287, 2022], ['Ruby', 130, 2022], ['Groovy', 172, 2022], [' Go ', 81, 2022], ['Scala', 129, 2022], ['Swift', 267, 2022], ['Kotlin', 600, 2022], ['TypeScript', 336, 2022], ['VBScript', 8, 2022], ['tcl', 17, 2022], ['Perl', 49, 2022], ['AutoIT', 4, 2022]]
options = {
    'title':
        {
        'text': 'Языки программирования',
        'subtext': 'Количество упоминаний в текстах вакансий',
        'left': 'center'
    },
    'tooltip': {
        'trigger': 'item'
    },
    'legend': {
        'top': 'bottom'
    },
    'dataset': [
        {'source': data},
        {
            'transform': [{
                'type': 'filter',
                'config': {'dimension': 'Year', 'value': 2019}
            },
                {
                    'type': 'sort',
                    'config': {'dimension': 'Popularity', 'order': 'desc'}
                }]
        },
        {
            'transform': [{
                'type': 'filter',
                'config': {'dimension': 'Year', 'value': 2020}
            },
                {
                    'type': 'sort',
                    'config': {'dimension': 'Popularity', 'order': 'desc'}
                }]
        },
        {
            'transform': [{
                'type': 'filter',
                'config': {'dimension': 'Year', 'value': 2021}
            },

                {
                    'type': 'sort',
                    'config': {'dimension': 'Popularity', 'order': 'desc'}
                }
            ],
        },
        {
            'transform': [{
                'type': 'filter',
                'config': {'dimension': 'Year', 'value': 2022}
            },

                {
                    'type': 'sort',
                    'config': {'dimension': 'Popularity', 'order': 'desc'}
                }],
        },
    ],
    'series': [
        {
            'type': 'pie',
            'radius': 50,
            'center': ['25%', '50%'],
            'datasetIndex': 1,
            'label': {'show': False}
        },
        {
            'type': 'pie',
            'radius': 50,
            'center': ['50%', '50%'],
            'datasetIndex': 2,
            'label': {'show': False}
        },
        {
            'type': 'pie',
            'radius': 50,
            'center': ['75%', '50%'],
            'datasetIndex': 3,
            'label': {'show': False}
        },
        {
            'type': 'pie',
            'radius': 50,
            'center': ['100%', '50%'],
            'datasetIndex': 4,
            'label': {'show': False}
        }
    ],
    'media': [
        {
            'query': {'minAspectRatio': 1},
            'option': {
                'title': [
                    {
                        'text': 'Языки программирования',
                        'subtext': 'Количество упоминаний в текстах вакансий',
                        'left': 'center'
                    },
                    {
                        'subtext': '2019',
                        'left': '20%',
                        'top': '75%',
                        'textAlign': 'center'
                    },
                    {
                        'subtext': '2020',
                        'left': '40%',
                        'top': '75%',
                        'textAlign': 'center'
                    },
                    {
                        'subtext': '2021',
                        'left': '60%',
                        'top': '75%',
                        'textAlign': 'center'
                    },
                    {
                        'subtext': '2022',
                        'left': '80%',
                        'top': '75%',
                        'textAlign': 'center'
                    }
                ],
                'series': [
                    {'center': ['20%', '50%']},
                    {'center': ['40%', '50%']},
                    {'center': ['60%', '50%']},
                    {'center': ['80%', '50%']}
                ]
            }
        },
        {
            'query': {'maxWidth': 500},
            'option': {
                'title': [
                    {
                        'text': 'Языки программирования',
                        'subtext': 'Количество упоминаний в текстах вакансий',
                        'left': 'center'
                    },
                    {
                        'subtext': '2019',
                        'left': '75%',
                        'top': '15%',
                        'textAlign': 'center'
                    },
                    {
                        'subtext': '2020',
                        'left': '75%',
                        'top': '35%',
                        'textAlign': 'center'
                    },
                    {
                        'subtext': '2021',
                        'left': '75%',
                        'top': '55%',
                        'textAlign': 'center'
                    },
                    {
                        'subtext': '2022',
                        'left': '75%',
                        'top': '75%',
                        'textAlign': 'center'
                    }
                ],
                'series': [
                    {'center': ['50%', '20%']},
                    {'center': ['50%', '40%']},
                    {'center': ['50%', '60%']},
                    {'center': ['50%', '80%']}
                ]
            }
        }
    ]
}
st_echarts(options=options,
           height='700px',
           renderer='svg')
