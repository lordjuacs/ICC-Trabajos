import data_base


def menu(user_answer):
    user_answer = user_answer.lower()
    if user_answer == '1' or user_answer == 'compare':
        print_data_base()
        print('===== Comparison =====')
        matriz = figure_reader()
        if matriz != 0:
            comparison_function(matriz)
        menu(input('Answer: '))
    elif user_answer == '2' or user_answer == 'save':
        matriz = figure_reader()
        save_figure(matriz)
        menu(input('Answer: '))
    elif user_answer == '':
        print('')
    else:
        print('Hey that is not an answer')
        menu(input('Answer: '))


def figure_reader():
    print('Enter your figure and press enter: ', end='\n')

    matriz_request = []
    counter = 0

    while True:
        item = input()
        if item != '':
            matriz_request.append(list(item))
            if len(matriz_request[0]) != len(matriz_request[counter]):
                print('Figure wrong inserted, your first line defines the dimensions of your figure. Please make sure to fill all your lines with space')
                return 0
            counter += 1
        else:
            break

    return matriz_request


def comparison_function(matriz_request):
    rows = len(matriz_request)
    columns = len(matriz_request[0])
    counter = 0

    for matriz in data_base.data_base:
        score = 0
        if rows == len(matriz) and columns == len(matriz[0]):
            for row in range(rows):
                for item in range(columns):
                    if matriz[row][item] == matriz_request[row][item]:
                        score += 1
        else:
            score = 0
        percentage = round((score / (rows * columns)) * 100, 2)
        if percentage == 100:
            print('Figure ' + str(counter + 1) + ' is equal to the original figure.', end=' ')
        elif percentage >= 80:
            print('Figure ' + str(counter + 1) + ' is almost equal to the original figure.' , end=' ')
        elif 0 < percentage < 80:
            print('Figure ' + str(counter + 1) + ' differs from the original figure.', end=' ')
        elif percentage == 0:
            print('Figure ' + str(counter + 1) + ' cannot be compared.', end=' ')
        print('Similarity percentage:', percentage, '%')
        counter += 1


def save_figure(matriz):
    if matriz != 0:
            data_base.data_base.append(matriz)
            print('Remember: when finished, this figure will be deleted')
            print('Succesful save')


def save_figure_txt(matriz):
    f = open("figures/" + str(len(matriz)) + '_' + str(len(matriz[0])) + '.txt', "w+")
    for rows in matriz:
        for item in rows:
            f.write(item)
        f.write("\n")
    f.write("\n")
    f.close()


def print_data_base():
    for i in range((len(data_base.data_base))):
        print("Figure " + str(i+1) + ":")
        print('\n')
        for x in data_base.data_base[i]:
            print("".join(x))
        print('\n')
