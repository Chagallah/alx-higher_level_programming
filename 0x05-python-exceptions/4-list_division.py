#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val_1 = int(my_list_1[i])
            val_2 = int(my_list_2[i])
            result.append(val_1 / val_2)
        except ValueError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            result.append(div)
            return (result)
