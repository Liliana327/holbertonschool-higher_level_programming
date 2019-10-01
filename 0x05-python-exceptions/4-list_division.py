#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    m_list = []
    for m in range(list_length):
        try:
            m_list.append(my_list_1[m] / my_list_2[m])
        except TypeError:
            print('''wrong type''')
            m_list.append(0)
        except ZeroDivisionError:
            print('''division by 0''')
            m_list.append(0)
        except IndexError:
            print('''out of range''')
            m_list.append(0)
        finally:
            pass
    return m_list
