from stackapi import StackAPI
from datetime import datetime, timedelta

def stack_questions():
    to_date = datetime.today()
    from_date = to_date - timedelta(days=2)
    tag = 'Python'

    site = StackAPI('stackoverflow')
    questions = site.fetch('questions', fromdate = from_date, todate = to_date, tagged = tag, sort='creation')

    counter = 0

    for i in questions['items']:
        counter += 1
        print(f"""Otázka číslo: {counter}; {datetime.fromtimestamp(i['creation_date']).strftime('%Y-%m-%d %H:%M:%S')}
{i['tags']}
{i['title']}
{i['link']}
""")

stack_questions()
