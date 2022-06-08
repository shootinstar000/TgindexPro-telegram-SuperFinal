import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = 2557747
    api_hash = "3022e575059ce68696f4fa4120ae33a2"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    # index_settings_str = os.environ["INDEX_SETTINGS"].strip()

    # index_settings = json.loads(index_settings_str)

    index_settings = {
      "index_all": False,
      "index_private":True,
      "index_group": True,
      "index_channel": True,
      "exclude_chats": [],
      "include_chats": [-1001750092497])],#my index chat
      "otg": {
          "enable": True,
          "include_private": True,
          "include_group": True,
          "include_channel": True
      }
    }
    otg_settings = index_settings['otg']
    enable_otg = otg_settings['enable']
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string ="1BVtsOHIBu6KX9fXTUMcEQrtQbm2zuHE1owgkmu7GTGd8eL3N5wgO2i_LjxU-bbkjhFdQVifDSGpJU0hLoO--CLQpAofaRHXIW4lti-am0r4IqPvUaV_V0aiNA3d0DKBVdoy12_BgKHbb1mjUE2SDWJn1ACgExOL35AFKy_9bfg9jQoM-QAEF6M6x6oQ_vqrQpysUsQWfjUqRsjvsKdYXO4sa5fSdtjghvCz1cQQK8NhXk6xTj0bpwNhM6yuw0uKQFv3ylRhATdB5Y-LmtXE07NoTJY_CorxII58u9mtUXivxfbKpfDBxZ5898ycuc6XTgNLKmdBsTZkQIzEGkftzo_mR95erwS4="
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

# try:
#     bot_token = os.environ["BOT_TOKEN"]
# except (KeyError, ValueError):
#     traceback.print_exc()
#     print("\n\nPlease set the BOT_TOKEN environment variable correctly")
#     sys.exit(1)



host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
chat_ids = []
alias_ids = []
