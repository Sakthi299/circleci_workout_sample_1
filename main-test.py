# Import the Add function, and assert that it works correctly.

# The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
# You can write a message to be written if the code returns False

from main import Add

def TestAdd():
    # assert <condition>,<error message>
    assert Add(2,3) == 5, "sum of 2 and 3 should be 5"
    assert Add(5,5) == 11
    print("Add Function works correctly")

if __name__ == '__main__':
    TestAdd()