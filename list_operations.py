participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements
if len(participants) == len(scores):
    print("Lists are valid and have the same number of elements.\n")
else:
    print("Error: Lists have different lengths.\n")




# First, display all the current participants with their scores. Use zip()
print("Current Participants and Scores:")
for name, score in zip(participants, scores):
    print(f"{name}: {score}")



# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
new_name = "Gali Prelham"
new_score_str = "48"
print(f"\nAttempting to register new participant: {new_name} with score: {new_score_str}")
if new_name in participants:
    print(f"Error: {new_name} is already registered.")
elif not new_name:
    print("Error: The name cannot be empty.")
elif not new_score_str.isdigit():
    print("Error: The score must be a number.")
elif int(new_score_str) < 0 or int(new_score_str) > 100:
    print("Error: The score must be between 0 and 100.")
else:
    participants.append(new_name)
    scores.append(int(new_score_str))
    print(f"Participant added successfully: {new_name} with score: {new_score_str}")

# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
search_name = "David Kim"
print(f"\nSearching for participant: {search_name}")
if search_name in participants:
    for i, name in enumerate(participants):
        if name == search_name:
            score = scores[i]
            break
    if score >= distinction_score:
        qualification_status = "DISTINCTION"
    elif score >= qualification_score:
        qualification_status = "QUALIFIED"
    else:
        qualification_status = "NOT QUALIFIED"
    print(f"Participant found: {search_name}, Score: {score}, Status: {qualification_status}")



# Display every participant's name, score, and whether they are qualified or not. 
print("\nAll Participants and their Qualification Status:")
for name, score in zip(participants, scores):
    if score >= distinction_score:
        qualification_status = "DISTINCTION"
    elif score >= qualification_score:
        qualification_status = "QUALIFIED"
    else:
        qualification_status = "NOT QUALIFIED"
    print(f"{name}: Score: {score}, Status: {qualification_status}")






# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
print("\nChecking for distinctions and pass status:")
has_distinction = any(score >= distinction_score for score in scores)
all_passed = all(score >= 50 for score in scores)
print(f"Has at least one distinction: {has_distinction}")
print(f"All participants have passed: {all_passed}")

# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.
print("\nUpdating a participant's score:")
update_name = "George Smith"
update_name_score = "85"
if update_name in participants:
    if update_name_score.isdigit() and 0 <= int(update_name_score) <= 100:
        for i, name in enumerate(participants):
            if name == update_name:
                scores[i] = int(update_name_score)
                break
        print(f"Score updated successfully for {update_name}: New Score: {update_name_score}")
    else:
        print("Error: The new score must be a number between 0 and 100.")



# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
withdraw_name = "Fatima Ali"
print(f"\nAttempting to withdraw participant: {withdraw_name}")
if withdraw_name in participants:
    for i, name in enumerate(participants):
        if name == withdraw_name:
            participants.pop(i)
            scores.pop(i)
            break
    print(f"Participant {withdraw_name} has been successfully withdrawn.")


# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
print("\nScoreboard (Descending Order):")
sorted_data = sorted(zip(scores, participants), reverse=True)
rank = 1
for score, name in sorted_data:
    print(f"Rank {rank}: {name} - Score: {score}")
    rank += 1



# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
highest_score = sorted_data[0][0]
lowest_score = sorted_data[-1][0]
total_score = 0
num_distinctions = 0
num_qualified = 0
num_not_qualified = 0
for score in scores:
    total_score += score
    if score >= distinction_score:
        num_distinctions += 1
    elif score >= qualification_score:
        num_qualified += 1
    else:
        num_not_qualified += 1
average_score = total_score / len(scores)
num_highest_score = scores.count(highest_score)
num_lowest_score = scores.count(lowest_score)



# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above
print("\nFinal Report:")
rank = 1
for score, name in sorted_data:
    if score >= distinction_score:
        qualification_status = "DISTINCTION"
    elif score >= qualification_score:
        qualification_status = "QUALIFIED"
    else:
        qualification_status = "NOT QUALIFIED"
    print(f"Rank {rank} | {name} | Score: {score}, Status: {qualification_status}")
    rank += 1
print("\n--- Summary Statistics ---")
print(f"Highest Score: {highest_score} (Achieved by {num_highest_score} participant(s))")
print(f"Lowest Score: {lowest_score} (Achieved by {num_lowest_score} participant(s))")
print(f"Average Score: {average_score:.2f}")
print(f"Distinctions: {num_distinctions} | Qualified: {num_qualified} | Not Qualified: {num_not_qualified}")
    
