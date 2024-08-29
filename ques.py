att=[]

def mark_present(student_name:str):
    if student_name not in att:
        att.append(student_name)
        print(f"{student_name} is marked present")
    else:
        print(f"{student_name} is already present")

def remove_student(student_name:str):
    if student_name in att:
        att.remove(student_name)
        print(f"{student_name} has been remove")
    else:
        print(f"{student_name} is not in the attendance list")

def is_present(student_name: str)->bool:
    return student_name in att

def display_attendance():
    if att:
        print("Students present today:")
        for student in att:
            print(f"{student}")
    else:
        print("No students are present today.")

def quick_sort():
    for i in range(0,len(att)):
        for j in range(i,len(att)):
            if att[i]>att[j]:
                temp=att[i]
                att[i]=att[j]
                att[j]=temp

def display_rev_attendance():
    if att:
        print("Students present today:")
        for i in range(-1,-len(att)-1,-1):
            print(att[i])
    else:
        print("No students are present today.")




if __name__=="__main__":
    while True:
        choice=int(input("1=add\n2=remove\n3=check\n4=display\n5=sort\n6=exit\n"))
        if choice==1:
            while True:
                name=str(input("Enter Name: -1 to exit "))
                if name !="-1":
                    mark_present(name)
                else:
                    break

        if choice==2:
            name=str(input("Enter Name: "))
            remove_student("name")

        if choice==3:
            name=str(input("Enter Name: "))
            print(is_present("name"))  

        if choice==4:
            display_attendance()

        if choice==5:
            quick_sort()
            display_rev_attendance()

        if choice==6:
            break