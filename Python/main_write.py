import time
import shared_memory

if __name__ == '__main__':
    print('Press Ctrl+C to stop')
    while True:
        shared_memory.write_string('Hey!')
        time.sleep(5)
        shared_memory.write_string('What\'s up!')
        time.sleep(5)
    