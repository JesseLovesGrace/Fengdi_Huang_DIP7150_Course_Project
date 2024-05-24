import os
from packages.spider import answer_spider
from packages.helpers import get_csv_directory, get_csv_name, get_question_id


if __name__ == '__main__':
    while True:
        # 获取问题id/Get the question ID
        question_id = get_question_id()
        if question_id.lower() == "exit":
            print("Exiting the program...")
            break

        # 获取CSV文件名/Get the CSV file name
        csv_name = get_csv_name(question_id)

        # 获取存储CSV文件的目录/Get the directory to store the CSV file
        csv_directory = get_csv_directory()

        # 保存文件名/Save CSV with the name of question ID
        csv_file = os.path.join(csv_directory, '{}.csv'.format(csv_name))

        # Check if the file already exists in the directory
        if os.path.exists(csv_file):
            print(f"File already exists.\nSkipping scraping for question ID: {question_id}\n")
        else:
            # 开始爬取/Running
            answer_spider(v_result_file=csv_file,  # 保存文件名
                          v_question_id=question_id)
    print('爬虫执行完毕！')
    print('Finished Crawling!')
