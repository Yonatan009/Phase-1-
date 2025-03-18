from Add_VM import Add_VM
import logging

logging.basicConfig(
    filename="infra-automation/logs/log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Machine(Add_VM):
    
    def __init__(self,os_name,os_vm,ram,cpu):
        super().__init__(os_name=os_name, os_vm=os_vm, ram=ram, cpu=cpu)
        
    def to_dict(self):
        return self.model_dump()
     
    def create_logs(self):
        print(f"name of your vm: {self.os_name}, operating system of vm: {self.os_vm}, ram:  {self.ram}, cpu: {self.cpu}")

        logging.info(f"Machine created: {self.os_name}, OS: {self.os_vm}, RAM: {self.ram}, CPU: {self.cpu}")
        
     
    