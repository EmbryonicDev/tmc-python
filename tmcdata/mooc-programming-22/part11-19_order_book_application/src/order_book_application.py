# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    task_num = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.task_num += 1
        self.id = Task.task_num
        self.complete = False

    def mark_finished(self):
        self.complete = True

    def is_finished(self):
        return self.complete

    def __str__(self):
        shared_text = f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer}"
        ending = "FINISHED" if self.complete else 'NOT FINISHED'
        return f"{shared_text} {ending}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return sorted(list(set([task.programmer for task in self.orders])))

    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError("No Such ID found!")

    def finished_orders(self):
        return [task for task in self.orders if task.complete]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.complete]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("No Such programmer found!")

        finished_tasks = [
            t for t in self.orders if programmer == t.programmer and t.complete]
        finished_hours = sum(t.workload for t in finished_tasks)

        unfinished_tasks = [
            t for t in self.orders if programmer == t.programmer and not t.complete]
        unfinished_hours = sum(t.workload for t in unfinished_tasks)

        return len(finished_tasks), len(unfinished_tasks), finished_hours, unfinished_hours


class App:
    def __init__(self):
        self.collection = OrderBook()

    def help(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def add_order(self):
        description = input('description: ')
        programmer_workload = input('programmer and workload estimate: ')
        programmer = programmer_workload.split(' ')[0]
        workload = programmer_workload.split(' ')[1]
        self.collection.add_order(description, programmer, workload)
        print('added!')

    def finished_orders(self):
        fo = self.collection.finished_orders()
        if len(fo) > 0:
            for order in fo:
                print(order)
            return
        print('no finished task')
    def execute(self):
        self.help()
        while True:
            print('')
            command = int(input('command: '))
            if command == 0:
                break
            if command == 1:
                self.add_order()
            if command == 2:
                self.finished_orders()


app = App()
app.execute()
# if __name__ == '__main__':
