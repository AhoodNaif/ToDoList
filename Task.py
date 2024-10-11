class Task:

    number = 1
    li = []

    def add_task(self, task = "", priority = 0):
        if not task == "" and not priority == 0:
            d = {}
            d["id"] = self.number
            d["task"] = task
            d["priority"] = priority
            d["is_complated"] = 2

            self.number += 1
            self.li.append(d)
        else:
            print("Please Enter Valid Task")
    
    def edit_task(self, id = 0, task = "", priority = 0, is_complated = 0):
        if not id == 0:
            check = False
            for ind, l in enumerate(self.li):
                if id == l["id"]:
                    if not task == "":
                        self.li[ind]["task"] = task
                    if not priority == 0:
                        self.li[ind]["priority"] = priority
                    if not is_complated == 0:
                        self.li[ind]["is_complated"] = is_complated
                    check = True
                    break
            if not check:
                print("Not Found")
        else:
            print("Please Enter Valid ID")

    def delete_task(self, id = 0):
        if not id == 0:
            check = False
            for ind, l in enumerate(self.li):
                if id == l["id"]:
                    self.li.pop(ind)
                    check = True
                    break
            if not check:
                print("Not Found")
        else:
            print("Please Enter Valid ID")

# Start the interactive task manager
main()