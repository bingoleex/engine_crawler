import random

def random_agent():

    # Operating system version 
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
        '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]

    # chrome version 
    chrome_version = 'Chrome/{}.0.{}.{}'.format(
        random.randint(55, 62), 
        random.randint(0, 3200), 
        random.randint(0, 140))

    # return like that: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
    return ' '.join(
            ['Mozilla/5.0', random.choice(os_type),
             'AppleWebKit/537.36',
             '(KHTML, like Gecko)',
             chrome_version, 'Safari/537.36'])