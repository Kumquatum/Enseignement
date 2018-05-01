#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


class BinaryTree:
    def __init__(self, root_value):
        if root_value is None:
            raise TypeError('Node cannot be "None"')
        self.data = root_value
        self.left = None
        self.right = None

    def set_left(self, value):
        self.left = BinaryTree(value)

    def set_right(self, value):
        self.right = BinaryTree(value)

    def __str__(self):
        return json.dumps({
            'data': self.data,
            'left': self.left.to_dict() if self.left is not None else None,
            'right': self.right.to_dict() if self.right is not None else None,
        })

    def to_dict(self):
        return json.loads(str(self))

    def find(self, value, _path=''):
        if value == self.data:
            return '{}>{}'.format(_path, self.data)
        else:
            found = None
            if self.left is not None:
                found = self.left.find(value, _path='{}>{}:left'.format(_path, self.data))
            if found is None and self.right is not None:
                found = self.right.find(value, _path='{}>{}:right'.format(_path, self.data))
            return found

    def dfs(self):
        yield self.data
        if self.left is not None:
            for d in self.left.dfs():
                yield d
        if self.right is not None:
            for d in self.right.dfs():
                yield d

if __name__ == "__main__":

    # + root:a
    #     + left:b
    #         + left:d
    #         + right:e
    #             + left:g
    #             + right:h
    #     + right:c
    #         + right:f
    #             + left:i
    #             + right:j
    tree = BinaryTree('a')
    tree.set_left('b')
    tree.set_right('c')

    tree.left.set_left('d')
    tree.left.set_right('e')
    tree.left.right.set_left('g')
    tree.left.right.set_right('h')

    tree.right.set_right('f')
    tree.right.right.set_left('i')
    tree.right.right.set_right('j')

    print(tree)
    print(tree.to_dict())
    print(type(tree.left))

    print('---')
    print('Depth-first')
    print(list(tree.dfs()))

    print('---')
    print('get path')
    print(tree.find('d'))
    print(tree.find('e'))
    print(tree.find('i'))
    print(tree.find('j'))
