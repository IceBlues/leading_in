import pyautogui
import pyperclip

import file_factory


class Filler:
    def __init__(self, mode):
        self.mode = mode
        self.content = None

    def get_fill_list(self):
        if self.mode == '2':
            data_res, self.content = file_factory.get_diff_list_from_files()
        else:
            data_res, self.content = file_factory.get_striped_list_from_file("data.txt")

        return data_res, self.content

    def fill(self):
        if self is None:
            print(r"[ERROR] 数据列表未获取")
        else:
            for line in self.content:
                pyautogui.click()
                pyperclip.copy(line.data)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')

    def export_tata_code(self):
        code_template = open("code_template", encoding="UTF-8").read()
        msg = ''
        for index in range(len(self.content)):
            if index == 0:
                msg += str(self.content[index])
            else:
                msg += str(', ' + str(self.content[index]))

        msg = '[' + msg + ']'
        code_template = code_template.replace("${data}", msg)
        pyperclip.copy(code_template)
        print("已复制代码到剪贴板!")
