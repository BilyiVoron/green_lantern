import re

with open("django_success.log") as log_file:

    # res = re.findall(r"\s(?P<bytes>\d+)$", log_file.read(), flags=re.M)
    # print(sum(map(int, res)))

    # for line in log_file.readlines():
    #     if re.search(r"\[\d{2}/[A-z]{3}/\d{4}\s\d{2}:\d{2}:\d{2}\]", line):
    #         print(line)

    # get_counter = 0
    # post_counter = 0
    # for line in log_file.readlines():
        # if re.search(r'"GET\s', line):
        #     get_counter += 1
        #     print(get_counter)
        # if re.search(r'\"POST\s', line):
        #     post_counter += 1
        #     print(post_counter)

    res = re.sub(r'"(GET|POST)\s/admin/*', "/secret_url/", log_file.read(), flags=re.M)
    print(res)
