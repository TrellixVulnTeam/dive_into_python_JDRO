import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
        except ValueError:
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra



def is_valid_photo_file_name(photo_file_name):
    array = photo_file_name.split('.')
    return len(array) == 2 and len(array[0]) > 0 and array[1] in ('jpg', 'jpeg', 'png', 'gif')

def is_digit(string_number):
    try:
        float(string_number)
        return True
    except:
        return False

def is_valid_row(car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra):
    if car_type == 'car':
        return bool(brand) and is_digit(passenger_seats_count) and is_valid_photo_file_name(photo_file_name) and is_digit(carrying)
    elif car_type == 'truck':
        return bool(brand) and is_valid_photo_file_name(photo_file_name) and is_digit(carrying)
    elif car_type == 'spec_machine':
        return bool(brand) and is_valid_photo_file_name(photo_file_name) and is_digit(carrying) and bool(extra)
    else:
        return False

def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
            except ValueError:
                continue

            if not is_valid_row(car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra):
                continue

            if car_type == 'car':
                car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
            elif car_type == 'truck':
                car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
            elif car_type == 'spec_machine':
                car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))

    return car_list
