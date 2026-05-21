#Question 1 - Text Processing Program
#Import required modules
import re
import zlib

#TEXT CLEANING FUNCTIONS

def clean_text(text):
    """
    This function removes punctuation and extra spaces
    from the text entered by the user.
    """

    #Remove punctuation except sentence punctuation
    cleaned = re.sub(r"[^\w\s.!?@]", "", text)

    #Remove extra spaces
    cleaned = re.sub(r"\s+", " ", cleaned)

    #Remove spaces at beginning and end
    cleaned = cleaned.strip()

    return cleaned


def extract_emails(text):
    """
    This function uses regular expressions
    to extract email addresses from the text.
    """

    #Regular expression pattern for emails
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"

    #Find all matching emails
    emails = re.findall(email_pattern, text)

    return emails

#TEXT ANALYSIS FUNCTIONS


def count_words(text):
    """
    This function counts the total number of words.
    """

    words = text.split()

    return len(words)


def count_unique_words(text):
    """
    This function counts unique words using set().
    """

    #Convert text to lowercase for accurate counting
    words = text.lower().split()

    unique_words = set(words)

    return len(unique_words)


def count_sentences(text):
    """
    This function counts the number of sentences
    using regular expressions.
    """

    #Split sentences using punctuation marks
    sentences = re.split(r"[.!?]+", text)

    #Remove empty items from the list
    sentences = [sentence for sentence in sentences if sentence.strip() != ""]

    return len(sentences)


#COMPRESSION FUNCTION


def compress_text(text):
    """
    This function compresses text using zlib
    and saves it into a binary file.
    """

    #Convert text into bytes
    text_bytes = text.encode("utf-8")

    #Compress the text
    compressed_data = zlib.compress(text_bytes)

    #Save compressed data to binary file
    with open("compressed_text.bin", "wb") as file:
        file.write(compressed_data)

    print("\nCompressed file created successfully!")


#MAIN PROGRAM

def main():

    print("===================================")
    print(" TEXT PROCESSING AND ANALYSIS TOOL ")
    print("===================================\n")

    #Ask user for text input
    user_text = input("Enter a block of text:\n")

    #Clean the text
    cleaned_text = clean_text(user_text)

    # Analyse the text
    total_words = count_words(cleaned_text)
    unique_words = count_unique_words(cleaned_text)
    total_sentences = count_sentences(cleaned_text)

    #Extract emails
    emails = extract_emails(user_text)

    #Display results
    print("\n========== RESULTS ==========")

    print(f"\nCleaned Text:\n{cleaned_text}")

    print("\nText Statistics")
    print("-------------------------")
    print(f"Total Words      : {total_words}")
    print(f"Unique Words     : {unique_words}")
    print(f"Total Sentences  : {total_sentences}")

    print("\nEmail Addresses")
    print("-------------------------")

    if len(emails) > 0:
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

    #Compress and save text
    compress_text(cleaned_text)


#Run the program
main()