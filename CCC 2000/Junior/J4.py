import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/brooks.in'
outt = absolute_path + '/brooks.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')




fin.close()
fout.close()