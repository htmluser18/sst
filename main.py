def input_students():
    students=[]
    n=int(input("enter the number of student :"))

    for i in range(n):
        print(f"\n student {i+1}:")
        name=input("enter name :")
        marks=float(input("enter marks :"))

        student={"name":name,"marks":marks}
        students.append(student)
    return students

def calculate_average(students):
    total=sum(s["marks"] for s in students)
    return total/len(students)

def f_topper(students):
    topper=max(students,key=lambda s:s["marks"])
    return topper

def f_lower(students):
    low=min(students,key=lambda s:s["marks"])
    return low

def display_report(students):
    print("\n----student report----")

    avg=calculate_average(students) 
    top=f_topper(students)
    low=f_lower(students)
    print(f" class average : {avg:.2f}"
          f"\n topper:{top["name"]} with {top["marks"]} marks"
          f"\n all students record :")
    
    for s in students:
        print(f"{s["name"]}:{s["marks"]}")

def main():
    students=input_students()
    display_report(students)

if __name__ == "__main__" :
    main()
