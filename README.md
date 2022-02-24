# Basic named entity recognizer for Georgian text
Non ML-based approach to extract named entities from Georgian text using Python.
Currently supported extractions are for countries and persons.
For better idea how accurate these extractions are, please see files in tests directory and do your own testing.

# Person extraction examples

### get persons
```python
from nerge import get_persons

p = get_persons(
    'უკრაინის პრეზიდენტი ვლადიმირ ზელენსკი საქართველოს პრეზიდენტ სალომე ზურაბიშვილს'
    ' მხარდაჭერისთვის მადლობას ქართულ ენაზე უხდის.'
)

print(p)
# result
['ვლადიმირ ზელენსკი', 'სალომე ზურაბიშვილი']
```

### get sex from name
```python
from nerge import get_sex

name = "გიორგი"
s = get_sex(name)

print(s)
# result
"M"
```

### basic(just letter-based) name/surname translation to English
```python
from nerge import translate_to_en

t = translate_to_en('კობა გვენეტაძე')

print(t)
# result
'Koba Gvenetadze'
```

### get person quotes from texts (not too accurate, but good enough in lots of places)
```python
from nerge import get_quotes

text = '''
"ტესტი", - განაცხადა გიორგი გიორგაძემ    
"PCR ტესტი 70 ლარად გვაქვს" აღნიშნა მარიამ მარიამიძემ
'''

quotes = get_quotes(text)

print(quotes)
# result
[
    {
        'person': 'გიორგი გიორგაძე',
        'quote': 'ტესტი',
        'match_case': 1
    },
    {
        'person': 'მარიამ მარიამიძე',
        'quote': 'PCR ტესტი 70 ლარად გვაქვს',
        'match_case': 1
    }
]
```




# Country extraction examples

### get countries
```python
from nerge import get_countries

# GET ISO-3166 2 letter country codes from given text

c = get_countries(
    "საქართველოს პრეზიდენტი შალვა ნათელაშვილი შეერთებული შტატების "
    "პრეზიდენტს საპრეზიდენტო სასახლეში დღეს უმასპინძლებს. შეხვედრას ასევე დაესწრებიან რუსი, "
    "ჩინელი, ფრანგი და დიდი ბრიტანელი დიპლომატები. შეხვედრის შემდეგ გაიმართება ამხანაგური "
    "საფეხბურთო მატჩი ბრაზილია-გერმანია, რომელსაც კორონავირუსის გავრცელების პრევენციის "
    "მიზნით მაყურებელი არ დაესწრება."
)

print(c)
# result
['BR', 'CN', 'DE', 'FR', 'GB', 'GE', 'RU', 'US']

```


### get meta information about country
```python
from nerge import get_country_meta

iso_alpha_2_code = "US"
m = get_country_meta(iso_alpha_2_code)

print(m)
# result
{
    "official_name": "United States of America (the)",
    "name_en": "United States of America",
    "name_ge": "ამერიკის შეერთებული შტატები",
    "alpha_3_code": "USA",
    "numeric_code": 840,
    "flag": "🇺🇸",
}
```


# supported python versions
Developed on version 3.8, should work on 3.6+

# limitations to be aware of

### get_persons
names and surnames list in __init__.py files are not written and checked by hand, so 
in this long lists there may be misplacement. They are fixed when discovered, 
if you see some of them, please make a pull request / let us know about it.

### get_quotes
This function is just simple pattern matching solution,
so errors like that may be an issue:

#### 1) Not logical results:

input:
```python
    '''
    "PCR ტესტი 70 ლარად?" ვკითხულობთ მარიამ მარიამიძისთვის მიწერილი შეტყობინებიდან  
    '''
```
output:
```python
    [{'person': 'მარიამ მარიამიძე', 'quote': 'PCR ტესტი 70 ლარად?', 'match_case': 1}]
```

Here the quote is not from this person, but according to our rules was identified so.

#### 2) Extraction will miss some text/not work if formatting, is not good enough, like missing quotes at some places, or in case of quotes in quotes, between quotes and previous words there are no separation characters, ex:
```python
    '''
    "111, 222, 333,"444 555" 666 777" - აცხადებს მარიამ მარიამიძე
    '''
```
output:
```python
    [{'person': 'მარიამ მარიამიძე', 'quote': ' 666 777', 'match_case': 1}]
```

look how comma and quote are together after 333 (,"), which causes not correct result,
but if there is a space between, result is correct:
```python
    '''
    "111, 222, 333, "444 555" 666 777" - აცხადებს მარიამ მარიამიძე
    '''
```
output:
```python
    [
        {
        'person': 'მარიამ მარიამიძე',
        'quote': '111, 222, 333, "444 555" 666 777',
        'match_case': 1
        }
    ]
```


Here result is shorter than it should be.

# Plans/Todos
We may decide to fix problems like that in the future with or without ML-based approaches.