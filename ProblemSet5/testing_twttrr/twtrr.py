def main():
    input_text = input("Input: ")
    print(shorten(input_text))

def shorten(word):
    shortened =""
    vowels = ["a","e","i","o","u"]
    for i in word:
        if i.lower() not in vowels:
            shortened = shortened + i
    return shortened

if __name__ == "__main__":
    main()