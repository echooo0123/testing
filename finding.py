def find_username_in_file(file_path):
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if 'username' in line.lower():
                print(f'找到包含用户名的行（行号: {line_num}）: {line.strip()}')
     
file_path = 'C:\\Users\\jingyiYang\\Desktop\\work\\pytest\\text_1.txt'
find_username_in_file(file_path)

