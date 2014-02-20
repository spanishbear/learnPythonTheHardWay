from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not configured."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        print "Engine __init_ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

        while True:
            print "\n-------------"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene

class Death(Scene):
    def enter(self):
        print "Whoops. You died."
        print "Try again."
       
class CentralCorridor(Scene):
    def enter(self):
        print """You are the last surviving member of your ship and your last mission is to get the neutron destruct bomb from the 
        Weapons Armory and blow the ship up after getting into an escape pod. You're running down the central corridor as silent as
        a mouse. Really, it was so silent that it was deafening. You see, your shoes were designed to be completely soundless.  
        Then, outta nowhere a Gothon jumps out.  You are shocked for two reasons: One, how in the hell did this Gothon find you so 
        easily? Second, you expected a terrible monster with sharp, jagged features. A creature straight from the depths of hell, with 
        rows of teeth that one bite feels like a million bites at once, claws so sharp that one slice would behead a person, a stench
        so foul that would knock the breath out of you. Oddly enough though, these Gothons truly were what their name says. Literally.
        They were just gothic humans. Here you are with a smooth-faced gothic boy standing before you, blocking the armory door.
        But you simply do not have the time to think about this conundrum. How was the entire crew defeated by these Gothons? 
        Anyway, what do you do? You have the options of "shooting", "dodging his attack", "running away in confusion", or "telling a joke".
        """ 
        action = raw_input("> ") 

        if action == "shooting":
            print """Bang! Bang! Bang! You closed your eyes while shooting him because you didn't want to see the truth that you were
            shooting a young boy. Unfortunately, you emptied your clip and you did not hit him AT ALL.  He's terribly upset that you 
            tried to kill him. He goes into an extreme rage and kills you instantly with one punch.
            """
            return 'death'
        elif action == "running away in confusion":
            print """After finding out what a Gothon truly is, you immediately run away with the most puzzling look on your face. Suddenly,
            there are other goths. They're watching you run towards them and they almost laugh at the face you're making. 
            But they shoot you instead.
            """
            return 'death'
        elif action == "dodging his attack":
            print """When the Gothon sees you, he tries to shoot with you his Gothic-themed gun. You dodge the gun shot successfully, but 
            you didn't realize that he had a knife in his other hand which he quickly uses to kill you as your dodging. """
        elif action == "telling a joke":
            print """Lucky for you, you had a few gothic friends when you were growing up. You are accustomed to their ways and you know 
            what will make them laugh. After all, they just want to be happy.  You say a joke, a pretty lame joke actually, and the Gothon
            stops, tries not to laugh, then bursts out laughing and can't move. While he's laughing, you shoot him right between his eyes.
            Then you keep walking towards the armory door and you're in!"""
            return 'laser_weapon_armory'
        else:
            print "Huh? Try again"
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print """ You walk in the room and see a box lying in the middle of the room. You walk up to it and see that there's a lock on 
        the box.  You have to guess the 3-digit code . You have only 10 times to do so.
        """
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0 

        while guess != code and guesses < 10: 
            print "bzzzzzzz"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print """The box finally opens up and you pick up the neutron bomb. Then you run to the bridge and place it in the right spot. 
            """
            return 'the_bridge'
        else:
            print "Obviously your will to live has dwindled. Incorrect code. The Gothons blow the ship."
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print """You are on the bridge with the bomb.  You've planted the bomb so now all you want to do is set detonote the bomb.  
        """
        action = raw_input("> ")

        if action == "throw the bomb":
            print "Bomb was thrown and you died""" 
            return 'death'
        elif action == "slowly place the bomb":
            print "Yay!"
        else:
            print "Does not compute. Try again."
            return 'the_bridge'
        

class EscapePod(Scene):
    def enter(self):
        print "You try to escape. You jump into a pod and leave!"
        return 'finished'
        

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        self.scene_name = scene_name
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
print "THIS IS THE A_MAP VARIABLE", a_map
a_game = Engine(a_map)
print "THIS IS THE A_GAME VARIABLE", a_game
a_game.play()

