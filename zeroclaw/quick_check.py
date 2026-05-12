import os, sys
md_files = [f for f in os.listdir('.') if f.endswith('.md')]
open('QUICK_RESULT.txt','w').write('\n'.join(md_files) if md_files else 'NO_MD_FILES')
