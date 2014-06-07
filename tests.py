from data.check_tests_data import are_files_json_compliant
import densim.test_all

def main():
    json_ok = are_files_json_compliant('.')
    if json_ok != 0:
        raise Exception
    densim.test_all.main()
    exit(0)


if __name__ == '__main__':
	main()
