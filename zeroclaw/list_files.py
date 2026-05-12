import os
files = os.listdir('/home/diogo/dev/library-docs/zeroclaw')
md_files = [f for f in files if f.endswith('.md') and f.startswith(('036', '037', '038', '039', '041', '042', '043', '044', '045'))]
for f in sorted(md_files):
    print(f)
