import random
import requests

FORM_ID = "1FAIpQLScLq44hS4ddtEJY1bseeglBuQbByUXn-ks9mDXBXz-OR2bK7A"
FORM_URL = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"

AGE_ENTRY = "entry.1566481183"

SCALE_1 = "entry.394222002"
SCALE_2 = "entry.19596365"
SCALE_3 = "entry.256460248"
SCALE_4 = "entry.787753461"
SCALE_5 = "entry.1143693195"
SCALE_6 = "entry.482472558"
SCALE_7 = "entry.735650163"
SCALE_8 = "entry.839594479"
SCALE_9 = "entry.1361374229"
SCALE_10 = "entry.1445859464"

# คะแนนที่สามารถสุ่มได้
VALUES = ["1", "2", "3", "4", "5"]

# Distribution ของแต่ละข้อ
#             1   2   3   4   5
DISTRIBUTION = {
    SCALE_1:  [1, 2, 5, 2, 1],
    SCALE_2:  [1, 5, 2, 2, 1],
    SCALE_3:  [1, 2, 2, 2, 5],
    SCALE_4:  [1, 1, 2, 5, 2],
    SCALE_5:  [1, 2, 5, 2, 1],
    SCALE_6:  [2, 2, 5, 2, 1],
    SCALE_7:  [1, 2, 2, 5, 2],
    SCALE_8:  [1, 2, 2, 5, 1],
    SCALE_9:  [1, 2, 5, 2, 1],
    SCALE_10: [1, 1, 3, 2, 5],
}


def random_scale(scale):
    weights = DISTRIBUTION[scale]

    return random.choices(
        VALUES,
        weights=weights,
        k=1
    )[0]


def generate_data():
    data = {
        AGE_ENTRY: "18 - 22 ปี"
    }

    for scale in DISTRIBUTION:
        data[scale] = random_scale(scale)

    return data


def submit_form(data):
    response = requests.post(FORM_URL, data=data)
    return response.status_code


if __name__ == "__main__":

    for i in range(50):

        # สร้างคำตอบใหม่ทุก response
        data = generate_data()

        status = submit_form(data)

        print(
            f"response = {i + 1} | "
            f"status = {status} | "
            f"data = {data}"
        )
