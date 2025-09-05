# Credit: Randomly0
def format_string(string: str = "") -> str:
  string = string.strip()
  splited_string = string.split(" ")
  cleaner_string = [item for item in splited_string if item]

  #Remove this section of code if you don't want to fix the capitalization error
  for i in range(len(cleaner_string)): 
    cleaner_string[i] = cleaner_string[i].lower().capitalize()


  return " ".join(cleaner_string)


str_input = str(input("Please input ChatGPT output below. This tool will remove any extra spaces from the output of GPT. \n"))


print(format_string(str_input))
