import logging


def configure_logger(log_file_name: str, debug: bool = False):
    """Setups the Python logger output sinks, format and information level."""

    # setup a log sink to a file
    logging.basicConfig(
        filename=log_file_name,
        level=logging.DEBUG,
        datefmt="%H:%M:%S",
        filemode="w+",
        format="%(asctime)s : %(levelname)-8s: %(name)-15s: %(message)s",
    )

    # setup a log sink to the console
    console_level = logging.DEBUG if debug else logging.INFO
    console = logging.StreamHandler()
    console.setLevel(console_level)
    console.setFormatter(
        logging.Formatter("%(asctime)s : %(levelname)-8s: %(name)-15s: %(message)s")
    )

    # Join sinks
    logging.getLogger().addHandler(console)


# ===== Auxiliar classes =====
class Bot:
    def __init__(self, name):
        self.LOG = logging.getLogger(self.__class__.__name__)
        self.__name = name
        self.LOG.debug(f"Bot initialized with name: {self.__name}")

    def say_name(self):
        self.LOG.inf(f"Bot name is {self.__name}")

    def explode(self):
        self.LOG.critical("Exploded.. (X_X)")

class Walker:
    def __init__(self, num_legs = 4):
        self.LOG = logging.getLogger(self.__class__.__name__)
        self.__legs = num_legs
        self.LOG.debug(f"Walker initialized with {self.__legs} legs.")
    
    def move(self):
        self.LOG.info("Walking.")

class CustomBot(Bot, Walker):
    def __init__(self, name, legs = 2):
        Bot.__init__(self, name)
        Walker.__init__(self, legs)
        self.LOG = logging.getLogger(name)
        self.LOG.debug(f"A new custom bot was built.")

# ============================


if __name__ == "__main__":
    configure_logger("log_test.log")
    bender = CustomBot("Bender")
    bender.move()

    rodriguez =  CustomBot("Rodriguez", 4)

    bender.explode()
    rodriguez.move()
