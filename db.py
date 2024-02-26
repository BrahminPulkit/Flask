import json


class Database:

    def insert(self,name,email,password):
        with open('users.json','r') as rf:
            users = json.load(rf)

            if email in users:
                return 0
            else:
                users[email] = [name,password]

        with open('users.json','w') as wf:
            json.dump(users,wf,indent=4)
            return 1

    def search(self,email,password):
        with open('users.json','r') as rf:
            users = json.load(rf)

            if email in users:
                if users[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
            
    def update_password(self, email, new_password):
        try:
            with open('users.json', 'r') as rf:
                users = json.load(rf)

            if email in users:
                if users[email][1] != new_password:  # Check if new password is different
                    users[email][1] = new_password  # Update password
                else:
                    return 1  # Password is same as current password, no need to update

            with open('users.json', 'w') as wf:
                json.dump(users, wf, indent=4)
                return 1  # Password updated successfully
        except Exception as e:
            print("Error updating password:", e)
            return 0  # Error occurred during password update


