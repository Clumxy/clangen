from scripts.cat.cats import Cat
from scripts.game_structure.game_essentials import game
from scripts.debug_commands.command import Command
from scripts.debug_commands.utils import add_output_line_to_log
from typing import List

class ForcePregnancyCommand(Command):
    def __init__(self):
        super().__init__()
        self.utils = None

    @property
    def name(self):
        return "force_pregnancy"

    @property
    def description(self):
        return "Forcibly makes a cat pregnant, given a cat name or ID."
    
    def callback(self, args: List[str]):
        """
        Forcibly makes a cat pregnant, given a cat name or ID.

        Usage: force_pregnancy <cat name/id>

        :param args: A list containing a single argument, the cat name or ID.
        :type args: list
        :return: None
        :rtype: None
        """
        

        if len(args) != 1:
            add_output_line_to_log(f"Usage: {self.name} <cat name/id>")
            return

        # Get the cat based on the provided name or ID
        cat = game.get_cat_by_ID_or_name(args[0])
        if not cat:
            add_output_line_to_log(f"Could not find cat with name or ID {args[0]}")
            return

        # Check if the cat is already pregnant
        if cat.pregnancy is not None:
            add_output_line_to_log(f"{cat.name} is already pregnant")
            return
        
        # Check if the cat is a female
        if cat.gender != "female":
            add_output_line_to_log(f"{cat.name} is not a female")
            return

        # Check if the cat is not a kit
        if cat.status == "kitten":
            add_output_line_to_log(f"{cat.name} is still a kitten")
            return

        # Check if the cat is an apprentice
        if cat.status in ["apprentice", "medicine cat apprentice", "mediator apprentice"]:
            add_output_line_to_log(f"{cat.name} is an apprentice and cannot have kits")
            return

        # Create a new pregnancy dictionary for the cat
        cat.pregnancy = {
            "moons": 0,  # The number of moons the cat has been pregnant
            "father": None,  # This is used for the father's ID
            "kits": [],  # List of kits that the cat will have
            "adoptive_parents": [],  # List of adoptive parents for the kits
        }

        # Log the success of the command
        add_output_line_to_log(f"Successfully forced pregnancy for {cat.name}")
        return
    
    def help(self):
        """
        Returns a string describing how to use the force_pregnancy command.

        :return: A string describing how to use the force_pregnancy command.
        :rtype: str
        """
        return "Forcibly makes a cat pregnant, given a cat name or ID.\n\n" \
               "Usage: force_pregnancy <cat name/id>"

