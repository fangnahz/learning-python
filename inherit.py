# coding: utf-8


class Item:
    name = ''

    def __init__(self, name):
        Item.name = name


class SubItem(Item):
    subname = ''

    def __init__(self, name):
        super().__init__(self, name)
        SubItem.subname = name

    def changeName(self, name):
        self.subname = name

sub_item_1 = SubItem('foo')
sub_item_1.subname
sub_item_1.name
sub_item_2 = SubItem('bar')
sub_item_2.subname
sub_item_2.name

# class var和object var只与引用方式相关
# 在class method中用self.引用，就作为object var处理，只修改自己的object
# 在class method中用CLASSNAME.引用，就作为class var处理，修改所有继承自class的object。
# 同一变量作为class var引用，作为object var引用可以混用
