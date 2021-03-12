import pathlib


def get_striped_list_from_file(path_str):
    data_striped_list = []
    data_file_res, target_file = __get_data_file(path_str)
    if data_file_res is True:
        target_list = target_file.readlines()
        target_file.close()
        for target_index in range(len(target_list)):
            word_data_arr = target_list[target_index].strip().split(" ")
            if len(word_data_arr) > 0 and word_data_arr[0] != '':
                word_str = word_data_arr[0]
                word_difficult = 0
                if len(word_data_arr) > 1:
                    word_difficult = int(word_data_arr[1])
                    if word_difficult < 0 or word_difficult > 2:
                        word_difficult = 0

                word = WordData(word_str, word_difficult)
                if word not in data_striped_list:
                    data_striped_list.append(word)
    else:
        data_striped_list = None
    return data_file_res, data_striped_list


def __get_data_file(path_str):
    data_path = pathlib.Path(path_str)
    res = True
    if data_path.exists():
        data_file = open(data_path.name, encoding="UTF-8")
    else:
        data_file = None
        res = False
    return res, data_file


def get_diff_list_from_files():
    content = []
    res1, data_list = get_striped_list_from_file("data.txt")
    res2, old_data_list = get_striped_list_from_file("data_old.txt")

    for line in data_list:
        if line not in old_data_list:
            content.append(line)

    return res1 and res2, content


class WordData:
    def __init__(self, data, difficult):
        self.data = data
        self.difficult = difficult

    def __eq__(self, other):
        res = False
        if self.data == other.data:
            res = True
        return res

    def __str__(self):
        return '["' + self.data + '", ' + str(self.difficult) + ']'
