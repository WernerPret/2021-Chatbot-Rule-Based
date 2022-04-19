# importing regex and random libraries
import re
import random
import sys


class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'what(\'s)? your planet like\?', 'answer_why_intent': r'why\s.*', 'cubed_intent': r'i \w{4} you to cube (\d+)', 'mult_intent': r'can you multiply (\d+) and (\d+)'}

  # Define .greet() below:
  def greet(self):
    self.name = input("Bidididi! What is your name? \n>")
    will_help = input(f"Hi {self.name} my name is Bidi, will you help me learn about your planet?\n>")
    if self.make_exit(will_help):
      print("OK then, let me just go fuck myself then...")
      return sys.exit(0)
    return self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    if reply in self.negative_responses:
      return True
    return False

  def exit_chat(self, reply):
    if reply in self.exit_commands:
      print("okay, jesus fuck, sorry then?")
      return True
    else:
      return False


  # Define .chat() next:
  def chat(self):
    reply = input(f"{random.choice(self.random_questions)}\n>")
    while not self.exit_chat(reply):
      self.match_reply(reply)
    return sys.exit(0)

  # Define .match_reply() below:
  def match_reply(self, reply):
    for intent, regex_pattern in self.alienbabble.items():
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'describe_planet_intent':return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent': return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent' : return self.cubed_intent(found_match.groups()[0])
      elif found_match and intent == 'mult_intent' : return self.mult_intent(found_match.groups()[0], found_match.groups()[1])
    return self.no_match_intent()
      



  # Define .describe_planet_intent():
  def describe_planet_intent(self):

    responses = ("My planet is a utopia of diverse organisms and species. ", "I am from Opidipus, the capital of the Wayward Galaxies. ")
    print(random.choice(responses))
    return self.chat()

  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = ("I come in peace.", "I am here to collect data on your planet and its inhabitants. ", "I heard the coffee is good. ")
    print(random.choice(responses))
    return self.chat()
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    print(int(number)**3)
    return self.chat()
  def mult_intent(self, num1, num2):
    print(int(num1)*int(num2))
    return self.chat()

  # Define .no_match_intent():
  def no_match_intent(self):
    print("No intiendo... probeer weer")
    return self.chat()

# Create an instance of AlienBot below:
alien = AlienBot()
alien.greet()

