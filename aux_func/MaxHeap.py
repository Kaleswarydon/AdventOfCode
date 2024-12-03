def _get_child_index(data: list, ind: int, right: bool = False) -> int | None:
    tmp = ((ind + 1) * 2) - int(not right)
    return tmp if tmp < len(data) else None


def _get_parent_index(ind: int):
    tmp = (ind - 1) // 2
    return tmp if tmp > -1 else None


def _bubble_up(data):
    current = len(data) - 1
    while current:
        parent_ind = _get_parent_index(current)
        if data[parent_ind] < data[current]:
            _swap(data, parent_ind, current)
            current = parent_ind
        else:
            break


def _bubble_down(data):
    current = 0
    while current is not None:
        try:
            left_index = _get_child_index(data, ind=current)
            left_child = data[left_index]
            right_index = _get_child_index(data, ind=current, right=True)
            right_child = data[right_index]
        except Exception as e:
            break
        swap_index = left_index if max(left_child, right_child) == left_child else right_index
        if data[current] < data[swap_index]:
            _swap(data, current, swap_index)
            current = swap_index
        else:
            break



def _swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


def heap_insert(data, item: int):
    data.append(item)
    _bubble_up(data)


def heap_pop(data):
    if data[0] > data[-1]:
        _swap(data, 0, -1)
    res = data.pop()
    _bubble_down(data)
    return res