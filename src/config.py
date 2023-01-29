from models import Config
import yaml, dacite, os
# from dotenv import load_dotenv

CHANNEL = "playground"

# load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

# load config.yaml
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG: Config = dacite.from_dict(
    Config, yaml.safe_load(open(os.path.join(SCRIPT_DIR, "config.yaml"), "r"))
)

INSTRUCTIONS = CONFIG.instructions
EXAMPLE_CONVERSATIONS = CONFIG.example_conversations