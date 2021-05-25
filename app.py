import csv

# Leemos el csv
with open('./test_files/intest.csv', newline='') as csvfile:
    data = csv.reader(csvfile)

    output = {}
    fields = []
    
    for row in data:
        #separamos por los ;
        arr = row[0].split(';')
        
        #creamos el diccionario.
        try:
            if (arr[0] in output):
               output[arr[0]] += float(arr[2])
            else:
                output[arr[0]] = float(arr[2])
        except:
            fields.append(arr[0])
            fields.append(arr[2])
            
#guardamos los datos en un csv nuevo
csv_file=open('out.csv','w')
write=csv.writer(csv_file,delimiter=';')
write.writerow(fields)
for data,value in output.items():
    write.writerow((data,str(round(value,3))))
