
x start
|
.
.
.
|
v
x def print_class_exam_results(...)
|
v
x def calculate_class_exam_average(...)
|
v
+-- call -> print_class_exam_results()
                |
                .
                .
                .
                v
               print(f"class average: {avgs:4.1f}")