#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rec_concat(list_of_lists, _concat=[]):
    return _concat if not list_of_lists else rec_concat(list_of_lists[1:], _concat=_concat+list_of_lists[0])
    # # unpack
    # # list of lists empty
    # if not list_of_lists:
    #     return _concat
    # else:
    #     return rec_concat(list_of_lists[1:], _concat=_concat+list_of_lists[0])



if __name__ == "__main__":

    a = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['k', 'l', 'm', 'n', 'o'],
        ['p', 'q', 'r', 's', 't'],
        ['u', 'v', 'w', 'x', 'y'],
        ['z', 1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]

    print('start')
    print(a)
    res = rec_concat(a)
    print('result')
    print(res)
