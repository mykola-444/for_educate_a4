# https://www.youtube.com/watch?v=MI1beugmEFM
import os

os.chdir('C:/tools/test')

print(os.getcwd())

for f in os.listdir():
    # print(f)
    f_name, f_ext = (os.path.splitext(f))
    f_cours, f_num = (f_name.split('_'))

    f_num = f_num.strip().zfill(2)

    new_file = ('{}-{}{}'.format(f_num, f_cours, f_ext))

    os.rename(f, new_file)
