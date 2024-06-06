import requests
import time
import pandas as pd
import os
import random
from packages.utils import trans_date, trans_gender, clean_content

# Header
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'cookie': r'_xsrf=gDBx2empdT2adUVXQVAY4KWL5b2RcJTF; __zse_ck=001_B0zii9NfV40cWwwVqmQsWZg7U4RNuRydwOaMEgPXtszhVNhkkEWCD2NPAB0QzkKdHu6o7ZQIKmd8hp3AvlIx2+trLiZ+K85u+=K/kdj+ISxTScOTVUJKsX5eaWPE7y/v; _zap=d04ff5f0-6918-42b3-a97c-fafa63e760c8; d_c0=AFCQy5ROuxiPTqKrbtYBORYT1J7hJfy9Q_A=|1717666817; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1717666820; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1717666820; captcha_session_v2=2|1:0|10:1717666819|18:captcha_session_v2|88:UVRwRllseERvUkMvaktuUHBwWWoyamhZOTB0MHVpWm93L0FLQ2RSZ21ETEJabVlhcFYvVkt2Z05kMzhSWTVScA==|7a0998f62fe654a3de077468c4e26e1cecfb5d25fb8c28ff3e0248fe92ab6f12; BEC=19c89cd421104aa5ab0b51e49af75d17; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1717666821|1717666816; gdxidpyhxdE=kQatPpjwREHXS%2BX%5CvvJQ1AA%2B9k%2FYU%2FXW%2FN1LWN8Ygzo%5CGiCUg3DmvcTR1pStyR7pXmprj3M6zZzL7kH%5CaEcXm8roYoV9UMAX%2BOW3NiHTT3CctvlVL6JGMVbgvLLJ%2Brq0i0bBuTx3Zm9vlAOog%2FaegpbwGn%5CkBBLwAcaQpLhhhwMN2TX2%3A1717667724616'
}

def answer_spider(v_result_file, v_question_id):
    # URL
    url = 'https://www.zhihu.com/api/v4/questions/{}/feeds?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&order=default&platform=desktop'.format(
        v_question_id)
    if os.path.exists(v_result_file):
        print("File '{}' already exists. Skipping scraping for question ID: {}".format(v_result_file, v_question_id))
        return
    while True:
        # Request
        r = requests.get(url, headers=headers)
        if r.status_code == 404:
            print(f"Question ID {v_question_id} does not exist.")
            return
        # Return the Data
        j_data = r.json()
        answer_list = j_data['data']
        # Define Empty List for Data
        author_name_list = []  # Author_Name
        author_gender_list = []  # Gender
        follower_count_list = []  # Follower_Count
        author_url_list = []  # Homepage
        headline_list = []  # Profile_Introduction
        answer_id_list = []  # Answer_ID
        answer_time_list = []  # Answer_Time
        answer_content_list = []  # Answer
        comment_count_list = []  # Comment_Count
        voteup_count_list = []  # Thumbs_Ip
        thanks_count_list = []  # Likes
        is_end = j_data['paging']['is_end']  # If_Last_Page
        page = j_data['paging']['page']
        print('Start Crawling Page {}, Total Answers: {}'.format(page, len(answer_list)))
        time.sleep(random.uniform(0, 1))
        for answer in answer_list:
            # Author_Name
            author_name = answer['target']['author']['name']
            author_name_list.append(author_name)
            # Gender
            author_gender = answer['target']['author']['gender']
            author_gender = trans_gender(author_gender)
            author_gender_list.append(author_gender)
            # Follower_Count
            try:
                follower_count = answer['target']['author']['follower_count']
            except:
                follower_count = ''
            follower_count_list.append(follower_count)
            # Homepage
            author_url = 'https://www.zhihu.com/people/' + answer['target']['author']['url_token']
            author_url_list.append(author_url)
            # Profile_Introduction
            headline = answer['target']['author']['headline']
            headline_list.append(headline)
            # Answer_ID
            answer_id = answer['target']['id']
            answer_id_list.append(answer_id)
            # Timestamp
            answer_time = answer['target']['updated_time']
            answer_time = trans_date(answer_time)
            answer_time_list.append(answer_time)
            # Content
            try:
                answer_content = answer['target']['content']
                answer_content = clean_content(answer_content)
            except:
                answer_content = ''
            answer_content_list.append(answer_content)
            # Comment_Count
            comment_count = answer['target']['comment_count']
            comment_count_list.append(comment_count)
            # Thumbs_Up
            voteup_count = answer['target']['voteup_count']
            voteup_count_list.append(voteup_count)
            # Likes
            thanks_count = answer['target']['thanks_count']
            thanks_count_list.append(thanks_count)

        # Saving Data to CSV
        if os.path.exists(v_result_file):  # If CSV exists, skip header
            header = False
        else:
            header = True
        # Save Data in DataFrame Format
        df = pd.DataFrame(
            {
                '问题id': v_question_id,
                '页码': page,
                '答主昵称': author_name_list,
                '答主性别': author_gender_list,
                '答主粉丝数': follower_count_list,
                '答主主页': author_url_list,
                '答主签名': headline_list,
                '回答id': answer_id_list,
                '回答时间': answer_time_list,
                '评论数': comment_count_list,
                '点赞数': voteup_count_list,
                '喜欢数': thanks_count_list,
                '回答内容': answer_content_list,
            }
        )
        # Save CSV
        df.to_csv(v_result_file, mode='a+', index=False, header=header, encoding='utf_8_sig')

        # If Exit
        if not is_end:  # If not last page
            url = j_data['paging']['next']  # Next Page Request
        else:  # If last page
            print('is_end is True , break now!\n')
            break
