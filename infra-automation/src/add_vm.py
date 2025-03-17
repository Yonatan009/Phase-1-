# choice library pydantic because the library completely oop project and make validation

import json
import os
from pydantic import BaseModel, Field, ValidationError
import re

class Add_VM(BaseModel):
    # ... required value
    os_name: str = Field(..., min_length=1) #Minimum one letter
    # user library re to provide valid input from user example "centos" == CentOS valid 
    os_vm: str = Field(..., pattern=re.compile(r'^(Ubuntu|Windows|CentOS)$', re.IGNORECASE))
    ram: int = Field(..., ge=1, le=128) #Min one ram and max 128
    cpu: int = Field(..., ge=1, le=16) #Min one cpu and max 16 
    # TODO: need to check how much ram was in computer to maximize
    # TODO: Need to check how much ram in computer
    
    @staticmethod
    def get_user_input() -> dict:
        try:
            os_name = input("Enter name your vm: ").strip().capitalize()
            os_vm = input("Enter witch os system you work example(Ubuntu|Windows|CentOS): ").capitalize().title()
            ram = int(input("Enter how much ram you want in your vm: "))
            cpu = int(input("Enter how much cpu you want in your vm: "))
            user = Add_VM(os_name=os_name, os_vm=os_vm, ram=ram, cpu=cpu)
            print("Your device data is correct.")
            return user.model_dump()
            
        except ValidationError as e:
            print("Error invalid input please try again: ")
            print(f"Error type: {e}")
            return {}
        
    @staticmethod
    def save_to_json(user_input: dict):
        if not user_input:
            print("Error: can't save empty input")
            return
        
        directory = "infra-automation/configs"
        file_path = os.path.join(directory,"json_file.json")
        # check if they dir exists if not create that.
        os.makedirs(directory, exist_ok=True)
        # check if the file "json_file.json" exists?
        if os.path.exists(file_path):
            try:
                with open(file_path, mode='r',encoding='utf-8') as file:
                    vm_list = json.load(file)
            except json.JSONDecodeError:
                vm_list = []
        else:
            vm_list = []
        vm_list.append(user_input)           
        with open(file_path,mode='w',encoding='utf-8') as file:
            json.dump(vm_list,file,indent=4,ensure_ascii=False)
        print("Vm data saving successfully")
            
        
# if __name__ == "__main__":
#     user_data = Add_VM.get_user_input()
#     if user_data:
#         Add_VM.save_to_json(user_data)
                
        
        
    
    
    