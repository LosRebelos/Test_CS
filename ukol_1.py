import os

def merge_files():
    files = [f for f in os.listdir('Examples') if f.endswith('.txt')]
    d = {}

    for file in files:
        with open(f'Examples/{file}', 'r') as fi:
            line_count = len(fi.readlines())
            d[line_count] = file


    with open('merged_files.txt', 'w') as mf:
        for k in sorted(d):
            with open(f'Examples/{d[k]}', 'r') as f:
                mf.write(d[k] + '\n')
                mf.write(str(k) + '\n')
                mf.write(f.read() + '\n')
                mf.write('\n')
            
merge_files()