**********************************
Name: Fengdi

Surname: Huang

Student ID: 231AHG003

Project: Web crawler on Zhihu.com
**********************************
About the webcrawler:

This is the webcrawler for Zhihu.com, which is the Chinese version of Quora.

It has 3 files used in package named packages:

  1_ The utils.py is responsible for converting the timestamp, gender of the users and clean the contents(removing duplicated texts and illegal characters and etc)

  2_ The spider.py is used for scraping the data from Zhihu posts.

  3_ The helper.py is used for getting the additional names for csv file and the directory.


When using the webcrawler, you need to first find Zhihu question ID.

For example, this is a question in Zhihu containing 7 posts: 

https://www.zhihu.com/question/587848376

The question ID is the number at the end of the url, which is 587848376.


After running the main program, you would need to input the question ID on the terminal. 

And then do what it asks, follow the instruction, input the directory you want the file to be stored, and the additional name for the file (which is in the formate of "知乎回答_question_id_additional_name").

The file would be stored as a CSV file to the directory you wish or the current directory.

And one more thing, make sure to use "utf-8-sig" instead of any other endocding format.

**********************************
PS: If the crawler fails, it is the cookie issue, just replace the cookie in spider.py and you would be fine.
