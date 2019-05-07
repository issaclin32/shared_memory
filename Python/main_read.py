import shared_memory

if __name__ == '__main__':
    response = shared_memory.read_string()
    print(response)