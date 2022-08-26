subj = {}
with open('6.txt', 'r', encoding='utf-8') as file_init:
    for line in file_init:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Total number of hours per subject: \n {subj}')