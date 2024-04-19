class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"First Name : {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Age : {self.age}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.is_rewards_member != False:
            print(f"{self.first_name} you are a member.")
        return self


    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            print(f"{self.first_name} you spent {amount} points.You have {self.gold_card_points} points left.")
        else:
            print(f"{self.first_name} you don't have enough points.")

        return self

user = User("Jeni", "Ukperaj", "jeni@gmail.com",24).display_info().enroll().spend_points(50)
user2 = User("Leo", "Messi" ,"messi@gmail.com",37).display_info().enroll().spend_points(80)
user3 = User("Jon", "Jones" , "jonjones@gmail.com", 34).display_info().enroll().spend_points(40)
