import streamlit as st
from streamlit_echarts import st_echarts


st.set_page_config(
    page_title="QA Job stat",
    page_icon="🧊",
    initial_sidebar_state="collapsed",
    menu_items={'Get help': None,
                'About': 'Some description',
                'Report a Bug': None}
)

options = {
    'baseOption': {
        'title':
            {
                'text': 'Языки программирования',
                'subtext': 'Количество упоминаний в текстах вакансий',
                'left': 'center'
            },
        'timeline': {
            'orient': 'horizontal',
            'autoPlay': False,
            'playInterval': 2000,
            'top': '12%',
            'width': '60%',
            'height': 40,
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
         'series': [{'data': [{'name': 'Java', 'value': 1881}, {'name': 'Python', 'value': 1294},
                              {'name': 'C#', 'value': 572}, {'name': 'JavaScript', 'value': 512},
                              {'name': 'PHP', 'value': 335}, {'name': 'C++', 'value': 275},
                              {'name': 'Ruby', 'value': 159}, {'name': 'Kotlin', 'value': 145},
                              {'name': 'Perl', 'value': 86}, {'name': 'Groovy', 'value': 79},
                              {'name': 'Scala', 'value': 77}, {'name': 'Swift', 'value': 52},
                              {'name': ' Go ', 'value': 44}, {'name': 'TypeScript', 'value': 39},
                              {'name': 'VBScript', 'value': 20}, {'name': 'tcl', 'value': 11},
                              {'name': 'AutoIT', 'value': 8}]}]},
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'series': [{'data': [{'name': 'Java', 'value': 2691}, {'name': 'Python', 'value': 1774},
                              {'name': 'C#', 'value': 630}, {'name': 'JavaScript', 'value': 623},
                              {'name': 'Kotlin', 'value': 379}, {'name': 'PHP', 'value': 321},
                              {'name': 'C++', 'value': 282}, {'name': 'Swift', 'value': 171},
                              {'name': 'Groovy', 'value': 140}, {'name': 'Ruby', 'value': 132},
                              {'name': 'TypeScript', 'value': 105}, {'name': 'Scala', 'value': 92},
                              {'name': 'Perl', 'value': 73}, {'name': ' Go ', 'value': 54},
                              {'name': 'tcl', 'value': 16}, {'name': 'VBScript', 'value': 2},
                              {'name': 'AutoIT', 'value': 2}]}]},
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'series': [{'data': [{'name': 'Java', 'value': 4458}, {'name': 'Python', 'value': 3042},
                              {'name': 'JavaScript', 'value': 1102}, {'name': 'C#', 'value': 1014},
                              {'name': 'Kotlin', 'value': 717}, {'name': 'PHP', 'value': 524},
                              {'name': 'C++', 'value': 404}, {'name': 'TypeScript', 'value': 350},
                              {'name': 'Swift', 'value': 309}, {'name': 'Groovy', 'value': 181},
                              {'name': 'Scala', 'value': 174}, {'name': 'Ruby', 'value': 169},
                              {'name': ' Go ', 'value': 140}, {'name': 'Perl', 'value': 96},
                              {'name': 'tcl', 'value': 25}, {'name': 'VBScript', 'value': 12},
                              {'name': 'AutoIT', 'value': 3}]}]},
        {'title': {'text': 'Языки программирования',
                   'subtext': 'Количество упоминаний в текстах вакансий'},
         'tooltip': {'formatter': '{b} {d}%'},
         'series': [{'data': [{'name': 'Java', 'value': 4007}, {'name': 'Python', 'value': 2837},
                              {'name': 'JavaScript', 'value': 838}, {'name': 'C#', 'value': 782},
                              {'name': 'Kotlin', 'value': 656}, {'name': 'PHP', 'value': 384},
                              {'name': 'TypeScript', 'value': 362}, {'name': 'C++', 'value': 311},
                              {'name': 'Swift', 'value': 285}, {'name': 'Groovy', 'value': 185},
                              {'name': 'Ruby', 'value': 138}, {'name': 'Scala', 'value': 138},
                              {'name': ' Go ', 'value': 90}, {'name': 'Perl', 'value': 54},
                              {'name': 'tcl', 'value': 17}, {'name': 'VBScript', 'value': 9},
                              {'name': 'AutoIT', 'value': 4}]}]}
    ],

}


st_echarts(options=options,
           height='600px',
           renderer='svg')

data = [['Language', 'Popularity', 'Year'], ['Java', 1881, 2019], ['Python', 1294, 2019],
        ['JavaScript', 512, 2019], ['C#', 572, 2019], ['PHP', 335, 2019], ['C++', 275, 2019],
        ['Ruby', 159, 2019], ['Groovy', 79, 2019], [' Go ', 44, 2019], ['Scala', 77, 2019],
        ['Swift', 52, 2019], ['Kotlin', 145, 2019], ['TypeScript', 39, 2019],
        ['VBScript', 20, 2019], ['tcl', 11, 2019], ['Perl', 86, 2019], ['AutoIT', 8, 2019],
        ['Java', 2691, 2020], ['Python', 1774, 2020], ['JavaScript', 623, 2020],
        ['C#', 630, 2020], ['PHP', 321, 2020], ['C++', 282, 2020], ['Ruby', 132, 2020],
        ['Groovy', 140, 2020], [' Go ', 54, 2020], ['Scala', 92, 2020], ['Swift', 171, 2020],
        ['Kotlin', 379, 2020], ['TypeScript', 105, 2020], ['VBScript', 2, 2020], ['tcl', 16, 2020],
        ['Perl', 73, 2020], ['AutoIT', 2, 2020], ['Java', 4458, 2021], ['Python', 3042, 2021],
        ['JavaScript', 1102, 2021], ['C#', 1014, 2021], ['PHP', 524, 2021], ['C++', 404, 2021],
        ['Ruby', 169, 2021], ['Groovy', 181, 2021], [' Go ', 140, 2021], ['Scala', 174, 2021],
        ['Swift', 309, 2021], ['Kotlin', 717, 2021], ['TypeScript', 350, 2021],
        ['VBScript', 12, 2021], ['tcl', 25, 2021], ['Perl', 96, 2021], ['AutoIT', 3, 2021],
        ['Java', 3713, 2022], ['Python', 2652, 2022], ['JavaScript', 784, 2022], ['C#', 725, 2022],
        ['PHP', 367, 2022], ['C++', 287, 2022], ['Ruby', 130, 2022], ['Groovy', 172, 2022],
        [' Go ', 81, 2022], ['Scala', 129, 2022], ['Swift', 267, 2022], ['Kotlin', 600, 2022],
        ['TypeScript', 336, 2022], ['VBScript', 8, 2022], ['tcl', 17, 2022], ['Perl', 49, 2022],
        ['AutoIT', 4, 2022]]
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
                        'top': '76%',
                        'textAlign': 'center'
                    }
                ],
                'series': [
                    {'center': ['50%', '15%']},
                    {'center': ['50%', '35%']},
                    {'center': ['50%', '55%']},
                    {'center': ['50%', '76%']}
                ]
            }
        }
    ]
}
st_echarts(options=options,
           height='700px',
           renderer='svg')
