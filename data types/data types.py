# Text Type
text = "Hello, World!"  # str

# Numeric Types
integer_num = 42        # int
float_num = 3.141      # float
complex_num = 2 + 3j    # complex

# Boolean Type
flag = True             # bool

# Binary Types
byte_data = b'hello'             # bytes
mutable_bytes = bytearray(b'abc')  # bytearray
view = memoryview(b'abc')        # memoryview

# Sequence Types
list_data = [1, 2, 3]            # list
tuple_data = (1, 2, 3)           # tuple
range_data = range(5)           # range

# Mapping Type
dict_data = {"name": "Alice", "age": 30}  # dict

# Set Types
set_data = {1, 2, 3}             # set
frozen_set_data = frozenset([1, 2, 3])  # frozenset

# None Type
none_value = None               # NoneType

# Display all values and their types
all_data = {
    "text": text,
    "integer": integer_num,
    "float": float_num,
    "complex": complex_num,
    "boolean": flag,
    "bytes": byte_data,
    "bytearray": mutable_bytes,
    "memoryview": view,
    "list": list_data,
    "tuple": tuple_data,
    "range": list(range_data),
    "dict": dict_data,
    "set": set_data,
    "frozenset": frozen_set_data,
    "none": none_value,
}

for name, value in all_data.items():
    print(f"{name}: {value} ({type(value).__name__})")
