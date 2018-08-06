# coding: utf-8
import sys


# receivers
class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This is a dummy file"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


# invokers
class ToobarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


# commands
class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


# create recievers
window = Window()
document = Document("dummy_document.txt")
# create commands (know about recievers)
save = SaveCommand(document)
exiet = ExitCommand(window)
# create invokers (composed of commands)
save_button = ToobarButton('save', 'save.png')
save_button.command = save
save_keypress = KeyboardShortcut('s', 'ctrl')
save_keypress.command = save
exit_menu = MenuItem('File', 'Exit')
exit_menu.command = exit


# simpler invoker: use function, not command object with execute()
class SimplerMenuItem:
    def click(self):
        self.command()


# reciever
window = Window()
menu_item = SimplerMenuItem()
menu_item.command = window.exit


# simpler invoker: use magicalized command object with execute(), incase states needed in commands
class SimplerKeyboardShortcut:
    def keypress(self):
        self.command()


# magicalize commands, in case commands has to maintain states
class MagicSaveCommand:
    def __init__(self, document):
        self.document = document

    def __call__(self):
        self.document.save()


# reciever
document = Document('Dummy_text.txt')
shortcut = SimplerKeyboardShortcut()
save_command = MagicSaveCommand(document)
shortcut.command = save_command
