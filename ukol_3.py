import csv
import pandas as pd

def data_correction():
    with open('phonebook.csv', 'w') as nf:
        with open ('phonebook_raw.csv', 'r') as file:
            reader = csv.reader(file)
            writer = csv.writer(nf)

            for row in reader:
                if len(row) == 7:
                    writer.writerow(row)
                else:
                    row.pop()
                    writer.writerow(row)
            
    df = pd.read_csv('phonebook.csv')
    cols = ['LASTNAME', 'FIRSTNAME', 'SECONDNAME']
    df['FULLNAME'] = df[cols].apply(lambda x: ','.join(x.dropna()), axis=1)
    df['FULLNAME'] = df['FULLNAME'].str.replace(',', ' ')
    df = df.assign(**{
        'LASTNAME': df['FULLNAME'].str.split().str[0],
        'FIRSTNAME': df['FULLNAME'].str.split().str[1],
        'SECONDNAME': df['FULLNAME'].str.split().str[2]
    })
    df.drop('FULLNAME', axis=1, inplace=True)

    pattern = '[^0-9]+'
    df['PHONE'] = df['PHONE'].str.replace(pattern, '')
    df['PHONE'] = df['PHONE'].str[4:11]
    df['PHONE'] = df['PHONE'].str.replace('^(\d{3})(\d{2})(\d{2})$', '+3 (123)-' + r'\1-\2-\3')

    agg_functions = {'SECONDNAME': 'first', 'ORGANIZATION': 'first', 'POSITION': 'first', 'PHONE': 'first', 'EMAIL': 'first'}
    df = df.groupby(['LASTNAME', 'FIRSTNAME'], sort=False).aggregate(agg_functions)

    df.to_csv('phonebook.csv', sep=',')
    
    return print(df)

data_correction()

