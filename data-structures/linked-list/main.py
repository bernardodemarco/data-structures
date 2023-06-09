from LinkedList import LinkedList


linked_list = LinkedList(10)

print(f'LENGTH = {linked_list.length}')
print(f'EMPTY = {linked_list.is_empty()}\n')

try:
    linked_list.remove_first()
except:
    print('Cannot remove items from an empty list\n')

linked_list.insert_at_end(16)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

# removed_element = linked_list.remove_first()
# print(f'REMOVED = {removed_element}')
# print(f'LENGTH = {linked_list.length}')
# print(f'{linked_list}\n')

removed_element = linked_list.remove_last()
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'{linked_list}\n')

linked_list.insert_at_start(6)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'{linked_list}\n')

linked_list.insert_at_start(8)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'{linked_list}\n')

linked_list.insert_at_start(10)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'{linked_list}\n')

linked_list.insert_at_end(20)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_at_end(40)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_after(40, 41)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_after(6, 6.1)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

try:
    linked_list.insert_after(2, 6.1)
except Exception as err:
    print('error!', err)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_before(10, 9)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_before(40, 39)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')


try:
    linked_list.insert_before(1, 1.5)
except Exception as err:
    print('error!', err)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert(6, 15.8)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')


try:
    linked_list.insert(10, 10.01)
except Exception as err:
    print('error!', err)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

retrieved_element = linked_list.get_at_position(2)
print(f'RETRIEVED = {retrieved_element}')

retrieved_element = linked_list.get_at_position(linked_list.length - 1)
print(f'RETRIEVED = {retrieved_element}')

retrieved_element = linked_list.get_at_position(6)
print(f'RETRIEVED = {retrieved_element}')

retrieved_element = linked_list.get_at_position(1)
print(f'RETRIEVED = {retrieved_element}')

retrieved_element = linked_list.get_at_position(linked_list.length)
print(f'RETRIEVED = {retrieved_element}')

try:
    retrieved_element = linked_list.get_at_position(0)
except:
    print('index is out of range')

try:
    retrieved_element = linked_list.get_at_position(linked_list.length + 1)
except:
    print('index is out of range again')


removed_element = linked_list.remove_first()
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

removed_element = linked_list.remove_first()
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

retrieved_element = linked_list.get_element(15.8)
print(f'RETRIEVED = {retrieved_element}')
retrieved_element = linked_list.get_element(39)
print(f'RETRIEVED = {retrieved_element}')

try:
    print(linked_list.get_element(16))
except Exception as err:
    print('ERROR', err)

print(f'{linked_list}\n')

removed_element = linked_list.remove_last()
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

removed_element = linked_list.remove_at_position(3)
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

removed_element = linked_list.remove_at_position(1)
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

removed_element = linked_list.remove_at_position(linked_list.length)
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

removed_element = linked_list.remove_at_position(linked_list.length - 1)
print(f'REMOVED = {removed_element}')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

try:
    linked_list.remove_at_position(linked_list.length + 1)
except Exception as err:
    print('error!', err)

try:
    linked_list.remove_at_position(0)
except Exception as err:
    print('error!', err)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert(1, 1)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert(linked_list.length + 1, linked_list.length + 1)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert(linked_list.length + 1, linked_list.length + 1)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

try:
    linked_list.insert(0, 1.5)
except:
    print('error! index out of range')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

try:
    linked_list.insert(linked_list.length + 2, 1.5)
except:
    print('error! index out of range')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_after(5, 5.5)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_before(15.8, 5.5)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_before(5.5, 5.45)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.remove(5.5)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_after(5.5, 5.55)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')
