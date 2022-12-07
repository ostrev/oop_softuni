from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_sum = 0
        for worker in self.workers:
            total_sum += worker.salary
        if self.__budget >= total_sum:
            self.__budget -= total_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_many_for_care = 0
        for animal in self.animals:
            total_many_for_care += animal.money_for_care
        if self.__budget >= total_many_for_care:
            self.__budget -= total_many_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_list = []
        tigers_list = []
        cheetahs_list = []
        result = f"You have {len(self.animals)} animals\n"
        for given_animal in self.animals:
            if given_animal.__class__.__name__ == 'Lion':
                lions_list.append(given_animal)
            elif given_animal.__class__.__name__ == 'Tiger':
                tigers_list.append(given_animal)
            elif given_animal.__class__.__name__ == 'Cheetah':
                cheetahs_list.append(given_animal)
        result += f'----- {len(lions_list)} Lions:\n'
        for lion in lions_list:
            result += repr(lion) + '\n'

        result += f'----- {len(tigers_list)} Tigers:\n'
        for tiger in tigers_list:
            result += repr(tiger) + '\n'

        result += f'----- {len(cheetahs_list)} Cheetahs:\n'
        for cheetah in cheetahs_list:
            result += repr(cheetah) + '\n'

        return result.strip()

    def workers_status(self):
        keepers_list = []
        caretakers_list = []
        vets_list = []
        result = f"You have {len(self.workers)} workers\n"
        for given_worker in self.workers:
            if given_worker.__class__.__name__ == 'Keeper':
                keepers_list.append(given_worker)
            elif given_worker.__class__.__name__ == 'Caretaker':
                caretakers_list.append(given_worker)
            elif given_worker.__class__.__name__ == 'Vet':
                vets_list.append(given_worker)
        result += f'----- {len(keepers_list)} Keepers:\n'
        for keeper in keepers_list:
            result += repr(keeper) + '\n'

        result += f'----- {len(caretakers_list)} Caretakers:\n'
        for caretaker in caretakers_list:
            result += repr(caretaker) + '\n'

        result += f'----- {len(vets_list)} Vets:\n'
        for vet in vets_list:
            result += repr(vet) + '\n'

        return result.strip()
