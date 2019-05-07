import mmap

SHARED_MEMORY_SIZE = 1024
TAG_NAME = "Local\\Test"

def write_string(input_string: str) -> None:
    # clear the shared memory
    with mmap.mmap(0, SHARED_MEMORY_SIZE, TAG_NAME) as map:
        map.write(b'\x00'*SHARED_MEMORY_SIZE)
    
    # write string to shared memory
    with mmap.mmap(0, SHARED_MEMORY_SIZE, TAG_NAME) as map:
        map.write(input_string.encode())
    return
    
def read_string() -> str:
    with mmap.mmap(0, SHARED_MEMORY_SIZE, TAG_NAME) as map:
        map.seek(0)
        raw_data = map.readline()
    return raw_data.decode('utf8').strip('\x00')