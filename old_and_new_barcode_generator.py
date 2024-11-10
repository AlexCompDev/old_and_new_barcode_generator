import random as ra


class Bar:
    def __init__(self):
        self.old_barcodes = []  # Список для хранения старых баркодов

    def convert_base10_to_base36(self, n):
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base36 = ""
        while n > 0:
            n, remainder = divmod(n, 36)
            base36 = alphabet[remainder] + base36
        return base36

    def generate_old_barcode(self):
        # Генерация старого баркода
        version = "22N"
        alkcode_base10 = ra.randint(0, 36**13 - 1)
        alkcode_base36 = self.convert_base10_to_base36(alkcode_base10).ljust(13, "0")
        jobcode = self.generate_jobcode()
        mark_number = str(ra.randint(0, 999999)).zfill(6)
        signature = "".join(
            ra.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(31)
        )
        return version + alkcode_base36 + jobcode + mark_number + signature

    def generate_jobcode(self):
        org_code_base10 = ra.randint(0, 36**4 - 1)
        org_code = self.convert_base10_to_base36(org_code_base10).ljust(4, "0")
        year_digit = str(ra.randint(0, 9))
        month = str(ra.randint(1, 12)).zfill(2)
        day = str(ra.randint(1, 28)).zfill(2)
        task_number = str(ra.randint(1, 999)).zfill(3)
        return org_code + year_digit + month + day + task_number

    def generate_new_barcode(self):
        # Генерация нового баркода
        mark_type = "".join(ra.choice("0123ABCD") for _ in range(3))
        mark_series = "".join(ra.choice("0123ABCD") for _ in range(3))
        mark_number = "".join(ra.choice("0123456789") for _ in range(8))
        egaiss_info = "".join(ra.choice("0123456789") for _ in range(7))
        signature = "".join(
            ra.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(129)
        )
        return mark_type + mark_series + mark_number + egaiss_info + signature

    def getold(self, n):
        return [self.generate_old_barcode() for _ in range(n)]

    def getnew(self, n):
        return [self.generate_new_barcode() for _ in range(n)]


# Пример использования
if __name__ == "__main__":
    bar = Bar()

    # Генерация случайного количества новых и старых баркодов от 1 до 15
    num_new_barcodes = ra.randint(1, 15)
    num_old_barcodes = ra.randint(1, 15)

    # Генерация новых баркодов
    new_barcodes = bar.getnew(num_new_barcodes)
    print("Новые баркоды:")
    print(new_barcodes)

    # Генерация старых баркодов
    old_barcodes = bar.getold(num_old_barcodes)
    print("Старые баркоды:")
    print(old_barcodes)
