class SoftVersion:

    def __init__(self):
        self.current_version = None

    @property
    def version(self):
        return self.current_version

    @version.setter
    def version(self, new_version: str):
        parse_data = new_version.split('.')
        if len(parse_data) != 3:
            raise ValueError("Невірний формат версії. Має бути 3-х цифри!")
        else:
            for i in range(0, len(parse_data)):
                try:
                    k = int(parse_data[i])
                except Exception:
                    print("Невірний формат версії. Введено не лише цифри!")
                if k not in range(0, 256):
                    raise ValueError("Невірний формат версії. (XXX.XXX.XXX, де XXX = 0..255)")
                else:
                    self.current_version = new_version


aidis = SoftVersion()
aidis.version = '123.1'
print(aidis.version)
