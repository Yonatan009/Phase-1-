from Add_VM import Add_VM
from Machine import Machine

class Main:
    
    def __init__(self):
        user_data = Add_VM.get_user_input()
        
        try:
            if user_data:
                self.vm = Machine(user_data["os_name"], user_data["os_vm"], user_data["ram"], user_data["cpu"])
                self.vm.create_logs()
                Add_VM.save_to_json(user_data)
        except Exception as e:
            print(f"Error : {e}")


if __name__ == "__main__":
    Main()