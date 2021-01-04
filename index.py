import time
from multiprocessing import Pool,freeze_support
from selenium.common.exceptions import UnexpectedAlertPresentException

import code_list,craw,save_xlsx

if __name__ == "__main__":
    freeze_support()
    start_time = time.time()
    kospi=code_list.kospi_code_list('kospi.xlsx')
    try:
        pool = Pool(processes=4) # 5개의 프로세스를 사용합니다.
        a=pool.map(craw.craw,kospi) # 코스피 133 137

        dic_key,dic_value=craw.craw_df(a)

    except UnexpectedAlertPresentException as e:
        print(e.__dict__["msg"])


    save_xlsx.save_xlsx(dic_key,dic_value)
    print('저장완료')

#하이골드3호-