class_12b = {
    "name": "12B",
    "members": [
        {
            "name": "John Doe",
            "grade": 9.5
        },
        {
            "name": "Marry Poppins",
            "grade": 8.5
        },
        {
            "name": "Pete Drake",
            "grade": 9.0
        },
    ]
}
class_12a = {
    "name": "12A",
    "members": [
        {
            "name": "Jake Suli",
            "grade": 8.0
        },
        {
            "name": "Mark Cozonac",
            "grade": 7.5
        },
    ]
}


########################################
def print_class_exam_results(class_results):
    print("----------------------------------")
    print(f"Results for class: {class_results['name']}")
    print("----------------------------------")
    for member in class_results['members']:
        print(f"\t{member['name']:20} {member['grade']:4.1f}")

    print("----------------------------------")
    avg = calculate_class_exam_average(class_results)
    print(f"class average: {avg:4.1f}")





def calculate_class_exam_average(class_results):
    sum = 0
    for member in class_results['members']:
        sum += member['grade']
    avg = sum / len(class_results['members']) 
    return avg   

########################################
print_class_exam_results(class_12a) # <----- call

