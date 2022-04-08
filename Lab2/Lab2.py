def count_of_inversions(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                counter += 1
    return counter


def gen_dict_from_main_user(lst):  # номер фільму : його місце у хітпараді на основі користувача з яким порівнюємо інших
    lst = lst[1:]
    dict_from_main = {a + 1: lst.index(a + 1) + 1 for a in range(len(lst))}
    return dict_from_main


def gen_dict_from_users(data, dct,
                        main_user_):  # номер фільму що відповідає-> : місце у хітпараді відносно головного користувача
    output_ = []
    for i in range(1, len(data)):
        lst = data[i][1:]
        dict_from_user = {lst[dct[a + 1] - 1]: dct[a + 1] for a in range(len(lst))}
        if main_user_ != data[i][0]:
            pair = [data[i][0], count_of_inversions(list(dict_from_user.keys()))]
            output_.append(pair)
        output_.sort(key=lambda x: x[1])
    return output_


def read_from_file(path_):
    data = []
    try:
        with open(path_, 'rt') as text_from_file:
            for line in text_from_file:
                data.append(list(map(int, line.split())))
            print(data)
            return data
    except FileNotFoundError:
        print("Incorrect path to file")


def write_to_file(output_, main_user_):
    path_ = "IP_12_Vasiliev_output.txt"
    output_str = str(main_user_) + "\n"
    for i in range(len(output_)):
        output_str += " ".join(map(str, output_[i])) + "\n"
    output_str += str(main_user_)
    with open(path_, 'wt') as text_in_file:
        text_in_file.write(output_str)



path = "input_10.txt"
info = read_from_file(path)
main_user = int(input("Input number of user:"))
number_of_users = info[0][0]
number_of_films = info[0][1]
dict_main = gen_dict_from_main_user(info[main_user])
output = gen_dict_from_users(info, dict_main, main_user)
print(output)
write_to_file(output, main_user)
