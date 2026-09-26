import random
import requests

FORM_ID = "1FAIpQLScLq44hS4ddtEJY1bseeglBuQbByUXn-ks9mDXBXz-OR2bK7A"
FORM_URL = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"

# =========================
# Google Form
# =========================

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


# =========================
# Age distribution
# =========================

AGE_OPTIONS = [
    "ต่ำกว่า 18 ปี",
    "18 - 22 ปี",
    "23 - 30 ปี",
    "31 - 40 ปี",
    "41 - 50 ปี",
    "51 ปีขึ้นไป",
]

# น้ำหนักของแต่ละช่วงอายุ
AGE_WEIGHTS = [
    1,  # 18 - 22
    5,  # 23 - 27
    3,  # 28 - 32
    2,  # 33 - 37
    1,  # 38 - 42
    1,
]


def random_age():
    return random.choices(
        AGE_OPTIONS,
        weights=AGE_WEIGHTS,
        k=1
    )[0]


# =========================
# Scale distribution
# =========================

VALUES = ["1", "2", "3", "4", "5"]

#             1  2  3  4  5
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
    SCALE_10: [1, 1, 2, 2, 5],
}



def random_scale(scale):
    return random.choices(
        VALUES,
        weights=DISTRIBUTION[scale],
        k=1
    )[0]


# =========================
# Generate response
# =========================

def generate_data():
    data = {
        # Random age
        AGE_ENTRY: random_age()
    }

    # Random SCALE 1-10
    for scale in DISTRIBUTION:
        data[scale] = random_scale(scale)

    return data


# =========================
# Submit
# =========================

def submit_form(data):
    response = requests.post(
        FORM_URL,
        data=data
    )

    return response.status_code


# =========================
# Main
# =========================

if __name__ == "__main__":

    NUMBER_OF_RESPONSES = 213 

    for i in range(NUMBER_OF_RESPONSES):

        # สร้างคำตอบใหม่ทุกครั้ง
        data = generate_data()

        # ส่งเข้า Google Form
        status = submit_form(data)

        print(
            f"Response {i + 1}/{NUMBER_OF_RESPONSES} | "
            f"status = {status}"
        )

        print(f"Age = {data[AGE_ENTRY]}")

        for scale in DISTRIBUTION:
            print(f"{scale} = {data[scale]}")

        print("-" * 50)
