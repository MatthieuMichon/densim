import check_tests_data

if __name__ == '__main__':
    json_ok = check_tests_data.check_test_json()
    if (json_ok == True):
        exit(0)
    exit(-1)

# vim: set et sts=4:
