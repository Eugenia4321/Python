#4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


url_list = ['https://gb.ru/lessons/284812','https://gb.ru/lessons/2848123','https://gb.ru/lessons/rwerw','https://gb.ru/lessons/qwe']
print(f'список URL различных сайтов: {url_list}')
result_list = list(map(lambda i: i.split('//')[1],url_list))
result_list = list(map(lambda i: i.split('/')[0],result_list))
print(f'список доменных имен сайтов {result_list}')