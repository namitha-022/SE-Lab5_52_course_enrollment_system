import hashlib
import secrets


courses = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

total_tuition = 0.0


def enroll_student(
    course_id,
    student_name,
    credits_registered=3,
    audit_trail=None,
):
   
    global total_tuition

    if audit_trail is None:
        audit_trail = []

    if course_id not in courses or courses[course_id]["is_closed"]:
        return False

    courses[course_id]["seats"] -= 1

    if courses[course_id]["seats"] <= 0:
        courses[course_id]["is_closed"] = True

    total_tuition += courses[course_id]["fee"]

    message = (
        f"Enrolled student {student_name} in course {course_id} "
        f"with {credits_registered} credits successfully"
    )
    audit_trail.append(message)

    return True


def drop_course(course_id):
    if course_id not in courses:
        return False

    courses[course_id]["seats"] += 1
    courses[course_id]["is_closed"] = False

    return True


def check_course_status(course_id):
    course = courses.get(course_id)

    if course is None:
        return False

    return not course["is_closed"]


def calculate_scholarship_tuition(course_id, discount_rate):
    if course_id not in courses:
        raise ValueError("Unknown course ID")

    if not 0 <= discount_rate <= 1:
        raise ValueError(
            "Discount rate must be between 0 and 1"
        )

    base_fee = courses[course_id]["fee"]

    return base_fee * (1 - discount_rate)


def generate_student_hash(roll_no):
    return hashlib.sha256(
        roll_no.encode("utf-8")
    ).hexdigest()


def generate_enrollment_otp():
    return secrets.randbelow(9000) + 1000


def export_course_roster(filename="course_roster.txt"):
    with open(filename, "w", encoding="utf-8") as roster_file:
        roster_file.write(str(courses))

    print(f"Course roster exported to: {filename}")


def get_open_courses_summary(course_catalog):
    return sum(
        not details["is_closed"]
        for details in course_catalog.values()
    )


def main():
    enroll_student("CS101", "Kritika", 4)
    drop_course("CS202")

    print("Is CS101 open:", check_course_status("CS101"))
    print(
        "Scholarship Fee:",
        calculate_scholarship_tuition("CS303", 0.25),
    )
    print("Student Hash:", generate_student_hash("REG_2026_091"))
    print("Enrollment OTP:", generate_enrollment_otp())

    export_course_roster()
    print("Open courses:", get_open_courses_summary(courses))


if __name__ == "__main__":
    main()
