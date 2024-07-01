class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.visits = []

    def add_visit(self, visit_date, doctor, diagnosis, treatment):
        visit = {
            "visit_date": visit_date,
            "doctor": doctor,
            "diagnosis": diagnosis,
            "treatment": treatment
        }
        self.visits.append(visit)
def __str__(self):
    visits_str = ""
    for visit in self.visits:
        visits_str += "Date: " + visit['visit_date'] + ", Doctor: " + visit['doctor'] + ", Diagnosis: " + visit['diagnosis'] + ", Treatment: " + visit['treatment'] + "\n"
    return "Patient ID: " + str(self.patient_id) + ", Name: " + self.name + ", Age: " + str(self.age) + ", Gender: " + self.gender + "\nVisits:\n" + visits_str


class HealthcareManagementSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, gender):
        if patient_id in self.patients:
            print(f"Patient with ID {patient_id} already exists.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, age, gender)
            print(f"Patient {name} added successfully.")

    def view_patient(self, patient_id):
        if patient_id in self.patients:
            print(self.patients[patient_id])
        else:
            print(f"Patient with ID {patient_id} not found.")

    def record_visit(self, patient_id, visit_date, doctor, diagnosis, treatment):
        if patient_id in self.patients:
            self.patients[patient_id].add_visit(visit_date, doctor, diagnosis, treatment)
            print(f"Visit recorded for patient ID {patient_id}.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def list_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            for patient_id, patient in self.patients.items():
                print(f"Patient ID: {patient_id}, Name: {patient.name},Age: {patient.age},Gender: {patient.gender}")

def main():
    system = HealthcareManagementSystem()

    while True:
        print("\nHealthcare Management System")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Record Visit")
        print("4. List Patients")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter patient ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            system.add_patient(patient_id, name, age, gender)
        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            system.view_patient(patient_id)
        elif choice == '3':
            patient_id = input("Enter patient ID: ")
            visit_date = input("Enter visit date (YYYY-MM-DD): ")
            doctor = input("Enter doctor name: ")
            diagnosis = input("Enter diagnosis: ")
            treatment = input("Enter treatment: ")
            system.record_visit(patient_id, visit_date, doctor, diagnosis, treatment)
        elif choice == '4':
            system.list_patients()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
