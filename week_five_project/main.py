from workers import Worker
import random

is_active_options = ["Yes", "No"]

class Recruitment_Program:
    workers = []
    jobs = []
    def __init__(self):
        self.index = 0  # Initialize index for job viewing
        Recruitment_Program.workers.append(Worker(
            "Tunde Adebayo", "Male", "Software Engineer", "B.Sc. Computer Science", 5, "Lagos, Nigeria", True
        ))
        Recruitment_Program.workers.append(Worker(
            "Adams Cynthia", "Female", "Frontend Engineer", "B.Sc. Computer Science", 4, "Lagos, Nigeria", True
        ))
        Recruitment_Program.workers.append(Worker(
            "Hammed Opeyemi", "Male", "Software Engineer", "B.Sc. Computer Science", 6, "Lagos, Nigeria", True
        ))

        Recruitment_Program.jobs.append({"title": "Software Engineer", 
        "description": "Develop and maintain web applications using modern frameworks.", 
        "years_of_experience": 5, 
        "location": "Lekki, Lagos", 
        "salary_expectation": 90000})

        Recruitment_Program.jobs.append({"title": "Frontend Engineer", 
        "description": "Develop and maintain web applications using modern frameworks.", 
        "years_of_experience": 4, 
        "location": "Lekki, Lagos", 
        "salary_expectation": 1000000})

        Recruitment_Program.jobs.append({"title": "Software Engineer", 
        "description": "Develop and maintain web applications using modern frameworks.", 
        "years_of_experience": 6, 
        "location": "Lekki, Lagos", 
        "salary_expectation": 90000})

    def qualified_candidate_report(self, job):
        candidates_count = 0
        for candidate in Recruitment_Program.workers:
            if candidate.job.lower() == job["title"].lower():
                candidates_count += 1  
        else:
            return candidates_count   
        
    def best_candidate(self,job):
        highest_year = 0
    # Finding the best candidate based on years of experience
        for candidate in Recruitment_Program.workers:
            if candidate.job.lower() == job["title"].lower():
                if candidate.years_of_experience > highest_year :
                    highest_year = candidate.years_of_experience
                    self.best_qualified_candidate = candidate

    # Creating input for job
    def create_a_job(self):
        title = input("Write the name of the job title: ")
        description = input("Write the description of the job: ")
        years_of_experience = input("Write the years of experience required for the job: ")
        salary_expectation = input("Write the salary expectation for the job: ")
        location = input("Write the location of the job: ")

     # Apppend job as dictionary to recruitment program job list
        Recruitment_Program.jobs.append({
            "title": title,
            "description": description,
            "years_of_experience": years_of_experience,
            "salary_expectation": salary_expectation,
            "location": location
        })
        return f"Job {title} has been added successfully."

   # Creating input for a worker
    def create_a_worker(self):
        name = input("Write the worker's name: ")
        gender = input("Write the worker's gender: ")
        job = input("Write the job of worker: ")
        qualification = input("Write the worker's qualification: ")
        location = input("Write the worker's location: ")
        years_of_experience = input("Write the worker's years of experience: ")

        is_active = random.choice(is_active_options)  # Randomly selecting if the worker is active or not

        #Adding input to workers class
        Recruitment_Program.workers.append(Worker(name, gender, job, qualification, years_of_experience, location, is_active))

        return f"Worker {name} has been added successfully."
    
    def view_a_job(self):
        while True:
            if self.index == len(Recruitment_Program.jobs):
                self.index = 0
            qualified_candidates = self.qualified_candidate_report(Recruitment_Program.jobs[self.index])
            best_candidates =self.best_candidate(Recruitment_Program.jobs[self.index]) 
            print(best_candidates)

            print(f"{"==" * 24}\n{Recruitment_Program.jobs[self.index]["title"]}\n{"==" * 24}")
            print(f"Location:{Recruitment_Program.jobs[self.index]["location"]}\n{"__" * 24}")
            print(f"Description: {Recruitment_Program.jobs[self.index]["description"]}\n{"__" * 24}")
            print(f"Requirements\nYears of Experience: {Recruitment_Program.jobs[self.index]["years_of_experience"]}\nQualification: {"None"}\n{"__" * 24}")
            print(f"Benefits\nSalary Expectation: {Recruitment_Program.jobs[self.index]["salary_expectation"]}\n{"__" * 24}")
            print(f"Qualified Candidates: {qualified_candidates}\n{"__" * 24}")
            print(f"Best Candidate:\nName: {"Henry"}\nGender: {"Male"}\nJob: {"Software Engineer"}\nQualification: {"B.Sc. Computer Science"}\nYears of Experience: {"3"}\nLocation: {"Lagos, Nigeria"}\n{"__" * 24}")
            option = input("Choose (Prev || Next): ")

            if option.lower().strip() == "Next".lower():
                    self.index += 1
                    print("You are already at the last job.")
            elif option.lower().strip() == "Prev".lower():
                if self.index == 0:
                    self.index = 0
                    print("You are already at the first job.")
                    self.index -= 1
                    continue
                else:
                    print("invalid option. Please choose 'Prev' or 'Next'.")
                    continue
    def run(self):
        print(f"{"--" * 24}\nWelcome to the Recruitment Program!\n{"--" * 24}")

        while True:
            option = input("i. Create a job\nii. Add a worker\niii. View a job\niv. Exit\n (Choose i | ii | iii | iv): ")
            
            if option == 'i':
                print("i")
            elif option == 'ii':
                self.create_a_worker() 
            elif option == 'iii':
                self.view_a_job()
            elif option == 'iv':
                print("Exiting the program. Goodbye!")
                break

if __name__ == "__main__":
    recruitment = Recruitment_Program()
    recruitment.run()