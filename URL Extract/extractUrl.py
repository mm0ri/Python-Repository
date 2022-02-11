import re

def domain_name(url):
    print(url)
    result = re.findall(r'//.\w+', url)
    result = ''.join(result)
    result = result.replace('//', '',)
    print(result)
    return result