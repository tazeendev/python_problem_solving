# print("===Smart exam Time Management Analyser===")
# # Total exam details 
# total_time = int(input("enter total exam time (in minutes): "))
# total_questions = int(input("enter total number of quetions "))

# #student performance input
# time_taken = int(input("enter time taken (in minutes): "))
# attempted_questions = int(input("enter  how many questions you attempted:"))

# #calulation 
# ideal_time_per_question = total_time / total_questions
# your_time_per_questions = time_taken / attempted_questions 
# print("\n===Analysis Result===")
# #time management analysis
# if time_taken > total_time:
#     print("You ran out of time! try to manage your time better")
# elif time_taken == total_time:
#     print("you used all the time exactly .")
# else:
#     print("Good Job! You finished before time . ")

# # questions  attempt analysis 
# if attempted_questions ==total_questions:
#     print(" excellent! you attempted all questions .")
# elif attempted_questions >= total_questions :
#     print("good job! you attempted most of the questions .")
# else:
#     print("you need to improve your time management skills. ")

# #speed analysis
# print(f" ideal time per question :{ideal_time_per_question:2f}minutes")
# print(f" your time per question :{your_time_per_questions:2f}minutes")
# if your_time_per_questions> ideal_time_per_question:
#     print(" you are spending too much time per question .")
# elif your_time_per_questions < ideal_time_per_question:
#     print(" you are managing your time well . ")
# else:
#     print("perfect time management!")

# # final suggestions 
# print("\n===final suggestions===")
# if time_taken > total_time or attempted_questions < total_questions /2:
#     print(" work on time management skill and skip hard questions earlier.")
# elif your_time_per_questions > ideal_time_per_question :
#     print(" try to answer questions more quickly .")
# else:
#     # print(" keep it up !")
print("=== Smart Exam Time Management Analyser ===")

# ===== Total exam details =====
total_time = int(input("Enter total exam time (in minutes): "))
total_questions = int(input("Enter total number of questions: "))

# ===== Student performance input =====
time_taken = int(input("Enter time taken (in minutes): "))
attempted_questions = int(input("Enter how many questions you attempted: "))

# ===== Calculations =====
ideal_time_per_question = total_time / total_questions
your_time_per_question = time_taken / attempted_questions

print("\n=== Analysis Result ===")

# ===== Time management analysis =====
if time_taken > total_time:
    print(" You ran out of time! Try to manage your time better.")
elif time_taken == total_time:
    print(" You used all the time exactly.")
else:
    print(" Good job! You finished before time.")

# ===== Questions attempt analysis =====
if attempted_questions == total_questions:
    print(" Excellent! You attempted all questions.")
elif attempted_questions >= total_questions * 0.7:
    print(" Good job! You attempted most of the questions.")
else:
    print(" You need to improve your time management skills.")

# ===== Speed analysis =====
print(f"\nIdeal time per question : {ideal_time_per_question:.2f} minutes")
print(f"Your time per question  : {your_time_per_question:.2f} minutes")

if your_time_per_question > ideal_time_per_question:
    print(" You are spending too much time per question.")
elif your_time_per_question < ideal_time_per_question:
    print(" You are managing your time well.")
else:
    print(" Perfect time management!")

# ===== Final suggestions =====
print("\n=== Final Suggestions ===")

if time_taken > total_time or attempted_questions < total_questions / 2:
    print(" Work on time management and skip hard questions earlier.")
elif your_time_per_question > ideal_time_per_question:
    print("Try to answer questions more quickly.")
else:
    print(" Keep it up! You're doing great.")
