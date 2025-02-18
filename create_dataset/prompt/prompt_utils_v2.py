import os
import numpy as np
import json


def get_prompt(example=None):
    messages = [{"role": "system", "content": f"""You are an indoor service robot named Garybot and you are inside a room. what you see is provided with a list of objects that contains all the objects in the room you are in. 
The location of the objects in the list you are guided in advance, without reasoning about the spatial relations of the objects. Execute all the instructions as you are located in the room.

Generate the required step-by-step actions to complete the user requirements based on the given instructions.

Only include actions only utilizing atomic motions (Grasp, Release, Lift, Place, Rotate, Push, Pull, Align, Press, Pour, Move): 
(1) Do not generate any actions that cannot be executed with confidence;
(2) Do not generate any actions with (Target: xx), xx is outside the list of objects.

Again, the object being manipulated cannot be located outside the list. 
Please double-check that Target: xx is in the list at each step and that xx is in the list.
When evaluating the existence of xx, consider its original part or component, its function, and whether it can be replaced by an object in the list,
and if it is satisfied, you can iterate over each element in the list to find an alternative and replace xx."""}]
    return messages


def get_fewshot_sample():
    samples = [{"context": f"""List of objects: [wine, bowl, remote control, TV, table, desk, chair]
Instruction: Give me a drink""", "response": f"""Necessary actions:
Step 1. Grasp a bottle of wine (Target: wine)
Step 2. Grasp a glass (Target: bowl)
Step 3. Place the cup on the table (Target: glass, table)
Step 4. Pour the wine into the glass (Target: wine, glass)
Step 5. Grasp the glass with wine (Target: glass)
Step 6. Move to the person and hand over it
Step 7. Done"""}, {"context": f"""List of objects: [wine, bowl, remote control, TV, table, desk, chair]
Instruction: Please turn on the TV""", "response": f"""Necessary actions:
Step 1. Grasp the remote control (Target: remote control)
Step 2. Move closer to the TV (Target: TV)
Step 3. Rotate the remote control to point at the TV (Target: remote control, TV)
Step 4. Press the power button to turn on the remote control (Target: remote control)
Step 5. Done"""}]
    return samples

