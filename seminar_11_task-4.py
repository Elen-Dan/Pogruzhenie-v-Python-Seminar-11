'''
Задание № 4
- Доработаем класс Архив из задачи 2.
- Добавьте методы представления экземпляра для программиста и для пользователя.
'''

class Archive:
    '''Класс Архив, который хранит пару свойств.
    '''
    __instance = None

    def __init__(self, num: int, text: str):
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        '''
        При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
        - list-архивы также являются свойствами экземпляра
        '''
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        '''метод представления экземпляра
        '''
        return f'Текст = {self.text}, число = {self.num}, архив текст = {self.text_list}, архив чисел = {self.num_list}'

    def __repr__(self):
        '''метод представления экземпляра
        '''
        return f'Текст = {self.text}, число = {self.num}'

if __name__ == '__main__':
    new_arch = Archive(1, 'test')
    # print(new_arch.num_list)
    # print(new_arch.text_list)
    print(repr(new_arch))
    print(Archive.__doc__)
    print(Archive.__new__.__doc__)
    print(Archive.__str__.__doc__)
    print(Archive.__repr__.__doc__)

   # new_arch_1 = Archive(2, 'Hello!')
   # print(new_arch_1.num_list)
   # print(new_arch_1.text_list)

   # new_arch_2 = Archive(3, 'world')
   # print(new_arch_2.num_list)
   # print(new_arch_2.text_list)