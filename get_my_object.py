import re
from ipaddress import ip_address


def mi_ip_valid(ip):
    """
    This will validate if the IP provided is valid or not.
    Only works for IPv4
    :param ip: IP to be validated
    :return: IP if IP is valid, else None
    29:0:0:0:0:0
    """
    if len(ip.split(".")) == 4:
        for n in ip.split("."):
            if int(n) not in range(2**8):
                return None

        return ip
    else:
        return None


def ip_valid(ip):
    """we will use a library to validate IP is ok"""
    try:
        ip_address(ip)
        return ip
    except ValueError:
        return None


def is_num(num):
    """This function will validate if num is a number"""
    try:
        return int(num)
    except ValueError:
        return 0


def is_code(country_code):
    """This function will validate the code has length of 2, and only letters.
    will return code in upper case or 'NA' if code passed is invalid."""
    if re.match("^[A-Z][A-Z]$", country_code.upper()):
        return country_code.upper()
    else:
        return 'NA'


def quitar_quotes(s):
    """this function simply remove the " characters from the string."""
    res = ""
    for g in s:
        if g != '"':
            res += g

    return res


class mi_linea_ip:
    """This class is created to work with the data on the file 'mi_data.csv'."""
    def __init__(self, ip_from, ip_to, id_from, id_to, code, country):
        print(__name__)
        # print(ip_from, ip_to, id_from, id_to, code, country)
        self.ip_from = ip_valid(ip_from)
        self.ip_to = ip_valid(ip_to)
        self.id_from = is_num(id_from)
        self.id_to = is_num(id_to)
        self.code = is_code(code)
        self.country = country

    def __str__(self):
        return "{}({}): {} - {}".format(self.country,
                                        self.code,
                                        self.ip_from,
                                        self.ip_to)


def mi_gen(mi_file, sep=","):
    for line in mi_file.readlines():
        # linea = line[:-1].replace('"', '').split(sep)
        linea = line[:-1].split(sep)
        for r in range(len(linea)):
            linea[r] = quitar_quotes(linea[r])
        linea = mi_linea_ip(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
        yield linea


if __name__ == '__main__':
    miip1 = '1.2.3.4'
    miip2 = '1.2.3.4123'

    a = mi_linea_ip("1.0.0.0", "1.0.0.255", "16777216", "16777471", "AU", "Australia")
    print(a)
    # Calidate the functions
    # print(is_num("1203"))
    # print(is_num("12DD"))
    # print(is_code("AU"))
    # print(is_code("A1"))
    # print(is_code("AUZ"))
