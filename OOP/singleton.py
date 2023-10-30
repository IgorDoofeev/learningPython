class DataBase:
    __instance = None

    def __call__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        """Если атрибут instance принимает значение none то тогда мы создаем cls.__instance = super().__new__(cls) новый
        экземпляр класса а если instance не none и мы вернем адрес ранее созданого объекта"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        '''
        делаем __instance снова None. Если объект будет удален сборщиком мусора то мы его снова делаем None
        '''
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('закрытие соединения с бд')

    def read(self):
        return 'данные из БД'

    def write(self, data):
        print(f'запись в БД {data}')



db = DataBase('root', '1234', 80)
db2 = DataBase('root', '5678', 40)
print(id(db), id(db2))
db.connect()
db2.connect()