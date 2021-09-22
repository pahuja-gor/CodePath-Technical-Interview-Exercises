"""
Given a list of students in the class, return a sorted list of the names for all students with no duplicates.
"""
def find_student_names(arr):
  pass


# DO NOT MODIFY
def run_tests():
    for args, expected in [
        (test_1, result_1),
        (test_2, result_2),
        (test_3, result_3),
    ]:
        result = find_student_names(args)
        if result != expected:
            raise ValueError(
                f'For arguments {args}, we expected {expected} but your code gave {result}'
            )
        else:
          print("Test case passed for find_student_names")


test_1 = ["Henry", "Amara", "Henry"]
test_2 = ["Kira", "Louis", "Kai", "Moana", "Maddie", "Ken", "Vera"]
test_3 = ["Aya", "Precious", "Jose", "Joshua", "Malik", "William", "Jayden","Sofia", "Maria","Valentina","Florencia","Camila","April","Charlotte","Noam","Ali","Omar","Eden","Maria","Natalie","Lucas","Adam","Jose","Nikola","Stefan","Martin","Noah","Noam","Alexander","Daniel","Gabriel","Oscar","Anna","Maria"]

result_1 = ["Amara", "Henry"]
result_2 = ["Kai", "Ken", "Kira", "Louis", "Maddie", "Moana", "Vera"]
result_3 = ["Adam", "Alexander", "Ali", "Anna", "April", "Aya", "Camila", "Charlotte", "Daniel", "Eden", "Florencia", "Gabriel", "Jayden", "Jose", "Joshua", "Lucas", "Malik", "Maria", "Martin", "Natalie", "Nikola", "Noah", "Noam", "Omar", "Oscar", "Precious", "Sofia", "Stefan", "Valentina", "William"]
