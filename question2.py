# Decryption function
def decrypt(text, key):
    return encrypt(text, -key)

# Encryption function (provided earlier)
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


# Encrypted code
encrypted_text = '''tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbvir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)'''

# Decrypt the encrypted text using the key
key = 13  # ROT13 is commonly used
decrypted_text = decrypt(encrypted_text, key)

# # Print the decrypted code
# print(decrypted_text)

# Corrected and commented code
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable  # Declare the global variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    # Iterate while the local variable is greater than 0
    while local_variable > 0:
        if local_variable % 2 == 0:  # Check if the number is even
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Set initialized with numbers (duplicates will be removed)
my_set = {1, 2, 3, 4, 5}

# Call the process_numbers function
result = process_numbers()

# Function to modify the dictionary by adding a new key-value pair
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable  # Add a new key-value pair to the dictionary

modify_dict()  # Call the function

# Function to update the global variable
def update_global():
    global global_variable  # Declare the global variable
    global_variable += 10  # Increment the global variable

# Loop to print numbers from 0 to 4
for i in range(5):
    print(i)
    i += 1

# Check conditions and print messages accordingly
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

# Print the global variable, dictionary, and set
print(global_variable)
print(my_dict)
print(my_set)

