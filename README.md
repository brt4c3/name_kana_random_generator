# name_kana_random_generator
the goal: generate Japanese name randomly in CSV format

## Example usage:
```
csv_file_path1 = 'data1.csv'  #last_name 
csv_file_path2 = 'data2.csv'  #first_name
header_present = False

result = join_random_rows(csv_file_path1, csv_file_path2, header_present)

#result:['last_name_kanji', 'last_name_kana', 'first_name_kaniji', 'first_name_kana' ,'gender']
```

##Further study
I might end up upgrade this project as a full-size CSV file creator by providing the row size as an argument.
