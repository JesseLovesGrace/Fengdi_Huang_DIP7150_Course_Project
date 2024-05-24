import os
from packages.spider import answer_spider
from packages.helpers import get_csv_directory, get_csv_name, get_question_id


if __name__ == '__main__':
    while True:
        # Get the question ID
        question_id = get_question_id()
        if question_id.lower() == "exit":
            print("Exiting the program...")
            break

        # Get the CSV file name
        csv_name = get_csv_name(question_id)

        # Get the directory to store the CSV file
        csv_directory = get_csv_directory()

        # Save CSV with the name of question ID
        csv_file = os.path.join(csv_directory, '{}.csv'.format(csv_name))

        # Check if the file already exists in the directory
        if os.path.exists(csv_file):
            print(f"File already exists.\nSkipping scraping for question ID: {question_id}\n")
        else:
            # Running
            answer_spider(v_result_file=csv_file,  
                          v_question_id=question_id)
    p
    print('Finished Crawling!')
