data = 'myprogram.exe'
sub_str_1= data[5:9]
middle= data[int(len(data)/2)]
extension= data[data.index('.'):len(data)]
print(sub_str_1, middle, extension, sep='\n')
