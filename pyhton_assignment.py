class Process:
    def __init__(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def print_table(self):
        print("{:<5} {:<10} {:<15} {:<10}".format("P_ID", "Process", "Start Time", "Priority"))
        for process in self.processes:
            print("{:<5} {:<10} {:<15} {:<10}".format(process.p_id, process.process_name, process.start_time, process.priority))

    def sort_by_p_id(self):
        self.processes.sort(key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.processes.sort(key=lambda x: priority_order[x.priority])

def main():
    flight_table = FlightTable()

    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))

    sorting_options = {
        1: flight_table.sort_by_p_id,
        2: flight_table.sort_by_start_time,
        3: flight_table.sort_by_priority
    }

    print("Sorting Options:")
    print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
    choice = int(input("Enter your choice: "))

    if choice in sorting_options:
        sorting_options[choice]()
        flight_table.print_table()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
