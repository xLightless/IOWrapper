import os
import time
import pandas as pd
import json

file = "credentials.txt"    

class Client(object):
    def __init__(self,auth=False):
        """ Wraps the authentication process of the HTTP requests into a managable system """
        self.auth = auth
        self.credentials = {}
    
    def set_additional_creds(self):
        """ Appends new credentials to a memory/file location """
        pass

    def set_values_to_new_creds(self):
        """ Sets new values for the appended credentials in '#set_additional_creds()' """
        pass

    def get_keys_and_values(self):
        """ Lets the user get authentication information to be used. If k/v else None """
        pass

    def _update_cred_keys(self):
        """ Updates the credentials of the client if the value exists, else return None """
        pass

    def _update_cred_values(self):                          
        """ Updates the credentials of the client if the key exists, else return None """
       
        d = self.credentials
        msg = input(f">> Enter a Key to update it's value (i.e. 'discord_username'): ")
        if msg in d:
            for k in d.items():
                uv = input(">> Enter the new value of this item: ")
                if msg==k:
                    print("Old Value: ",k,d.get(k))
                    d[k] = [uv]
                    print("New Value: ",k,d.get(k))
                break
            with open(file,"w") as f:
                f.write(str(dict(d.items())))
                f.close()
        else: print("The key you entered could not be found, please try again.")

    def _run_builder(self):
        building = True
        count = 0
        print("Please carefully enter the correct values below...")
        while building:
            try:
                key = input(">> Enter a key for the dictionary: ")
                value = input(f">> Enter a value for {key}: ")
                if key != '': self.credentials[key] = [value]
                if key == '': raise KeyError
            except KeyError:
                count=(count+1)
                print(f"Invalid ['k({key}):value'].\n")
                if count==2:
                    print(">> Too many false attempts to set a key|value, terminating...\n")
                    print(f"Writing valid keys and values to memory/file. Please check '{file}'")
                    building = False
                    if building == False:
                        with open(file,"w") as f:
                            f.write(str(dict(self.credentials.items())))
                            f.close()

    def build(self):
        if self.auth == False:
            print("Building Application...",
            "If you need to use explicit features you will be asked to enter credentials.")

        elif self.auth == True:
            floc = os.path.exists(file)
            try:
                if (~(floc)):
                    create_file = open(file,"x")
                    return create_file
            except Exception:
                pass
            
                if floc==True:
                    with open(file,"r") as f:
                        data = json.dumps(f.read())
                        fdata = data.replace("'",'"')
                        d = dict(fdata)
                        if os.stat(file).st_size != 0:
                            print(d)
                            ans = input("Do you want to update your credentials?: ").lower()
                            if ans=="y":
                                pass
                            else:
                                print("Everything is good, Authentication Over! :D")
                                exit()

                        else:
                            self._run_builder()

client = Client(auth=True)
client.build()