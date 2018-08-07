from threading import Thread


class InputReader(Thread):
    def run(self):
        self.line_of_text = input()


print('Enter some text and press enter:')  # print in main thread
thread = InputReader()
thread.start()  # branch out a new thread waiting for keyboard input
# meanwhile main thread carries on with following statements...

count = result = 1
while thread.is_alive():
    result = count * count
    count += 1

print('calculated squares up to {0} * {0} = {1}'.format(count, result))
print('while you typed "{}"'.format(thread.line_of_text))
# fin!
