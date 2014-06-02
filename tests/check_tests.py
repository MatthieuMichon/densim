import check_tests_data

if __name__ == '__main__':
    json_ok = check_tests_data.check_all_json_per_directory("tests/data")
    if (json_ok == 0):
        exit(0)
    exit(-1)

# vim: set et sts=4:
