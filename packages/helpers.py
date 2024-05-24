import os


def get_question_id():
    """
    Function to get the question ID from the user.
    """
    return input("Please enter the question ID (enter 'exit' to quit): ")


def get_csv_directory():
    """
    Function to get the directory where the CSV file should be stored.
    If the user just presses Enter, return current directory.
    """
    while True:
        csv_directory = input("Enter the output directory (press Enter for current directory): ")
        if csv_directory.strip() == "":
            return os.getcwd()  # Return current directory if user just presses Enter
        elif os.path.exists(csv_directory.strip()):  # Check if the directory exists
            return csv_directory.strip()
        else:
            print("Directory doesn't exist. Please enter a valid directory.")


def get_csv_name(question_id):
    """
    Function to get the additional name to be added to the CSV file name.
    Remove specific illegal characters from the input.
    """
    while True:
        additional_name = input("Enter additional file name (press Enter for no additional name): ")
        if additional_name.strip() == "":
            return '知乎回答_{}'.format(question_id)  # Return default name if user just presses Enter
        else:
            # Remove specific illegal characters from the input
            illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '，', '？', '。']
            cleaned_name = ''.join(c for c in additional_name if c not in illegal_chars)
            return '知乎回答_{}_{}'.format(question_id, cleaned_name.strip())
