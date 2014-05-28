import json

def check_test_json():
    try:
        json_data = json.load(open("tests/data/mission-kyoto-4444.json"))
    except Exception:
        print("Fail!")
        return False
    print("OK")
    return True

if __name__ == '__main__':
    json_ok = check_test_json()
    if (json_ok == True):
        exit(0)
    exit(-1)

# vim: set et sts=4:
