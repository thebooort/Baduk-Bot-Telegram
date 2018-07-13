# Main parts and structure are extracted from tgchessbot http://davinchoo.com/project/tgchess/
import time, pickle, os.path
import telepot  # https://github.com/nickoala/telepot

class baduk_bot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        '''Set up local variables'''
        super(baduk_bot, self).__init__(*args, **kwargs)
        self._answerer = telepot.helper.Answerer(self)
        self.gamelog = {}
        self.msglog = []
        self.statslog = {} # Store player stats [W, D, L]

        self.startsheet, self.helpsheet = self.generate_sheets()

    def generate_sheets(self):
        startsheet = "Hello! This is the Telegram Baduk Bot [@Play_Baduk_Bot.](t.me/Play_Baduk_Bot)"
        startsheet += "For the full command list, type `/help`.\n"
        

        helpsheet = "Allowed commands:\n"
        helpsheet += "`/help`: Display help sheet\n"

        return startsheet, helpsheet

    def save_state(self):
        '''Saves gamelog, msglog and statslog for persistence'''
        with open("gamelog.txt", "wb") as f:
            pickle.dump(self.gamelog, f)

        with open("msglog.txt", "wb") as f:
            pickle.dump(self.msglog, f)

        with open("statslog.txt", "wb") as f:
            pickle.dump(self.statslog, f)

    def load_state(self):
        '''Loads gamelog, msglog and statslog for persistence'''
        try:
            with open("gamelog.txt", "rb") as f:
                self.gamelog = pickle.load(f)
        except EOFError:
            self.gamelog = {}

        try:
            with open("msglog.txt", "rb") as f:
                self.msglog = pickle.load(f)
        except EOFError:
            self.msglog = []

        try:
            with open("statslog.txt", "rb") as f:
                self.statslog = pickle.load(f)
        except EOFError:
            self.statslog = {}        
    
    def game_end(self, chat_id, players, winner):
        '''Handle end of game situation'''
        # Remove match from game logs
        del self.gamelog[chat_id]

        # Update player stats [W, D, L] and print results
        if players[0] not in self.statslog: self.statslog[players[0]] = [0,0,0]
        if players[2] not in self.statslog: self.statslog[players[2]] = [0,0,0]
        white_stats = self.statslog[players[0]]
        black_stats = self.statslog[players[2]]

        # Format and send game outcome
        outcome = ""
        if winner == "White":
            white_stats[0] += 1
            black_stats[2] += 1
            outcome = "White wins! {} (W) versus {} (B) : 1-0".format(players[1], players[3])
        elif winner == "Black":
            white_stats[2] += 1
            black_stats[0] += 1
            outcome = "Black wins! {} (W) versus {} (B) : 0-1".format(players[1], players[3])
        elif winner == "Draw":
            white_stats[1] += 1
            black_stats[1] += 1
            outcome = "It's a draw! {} (W) versus {} (B) : 0.5-0.5".format(players[1], players[3])
        self.statslog[players[0]] = white_stats
        self.statslog[players[2]] = black_stats

        bot.sendMessage(chat_id, outcome)     


    def get_sender_details(self, msg):
        '''Extract sender id and name to be used in the match'''
        sender_id = msg["from"]["id"]
        if "username" in msg["from"]:
            sender_username = msg["from"]["username"]
        elif "last_name" in msg["from"]:
            sender_username = msg["from"]["last_name"]
        elif "first_name" in msg["from"]:
            sender_username = msg["from"]["first_name"]
        else:
            sender_username = "Nameless"
        return sender_id, sender_username

    def get_games_involved(self, sender_id):
        return [g for g in self.gamelog.values() if self.is_in_game(g.get_players(), sender_id)]    
 

# this part should call to the match file. Here we should upload all the commands and shit like that

    def on_chat_message(self, msg):
        self.msglog.append(msg)
        content_type, chat_type, chat_id = telepot.glance(msg)
        sender_id, sender_username = self.get_sender_details(msg)
        print(msg, sender_id, sender_username)

        # Note:
        # if chat_id == sender_id, then it's a human-to-bot 1-on-1 chat
        # if chat_id != sender_id, then chat_id is group chat id
        print('Chat Message:', content_type, chat_type, chat_id, msg[content_type])

        tokens = msg[content_type].split(" ")
        match = self.gamelog[chat_id] if chat_id in self.gamelog.keys() else None
        players = match.get_players() if match != None else None

        if tokens[0] == "/start" or tokens[0] == "/start@tgchessbot":
            bot.sendMessage(chat_id, self.startsheet, parse_mode = "Markdown", disable_web_page_preview = True)
        elif tokens[0] == "/help" or tokens[0] == "/help@tgchessbot":
            bot.sendMessage(chat_id, self.helpsheet, parse_mode = "Markdown", disable_web_page_preview = True)
	



    def on_inline_query(self, msg):
        '''Handles online queries by dynamically checking if it matches any keywords in the bank'''
        self.msglog.append(msg)
        print(msg)

        query_id, from_id, query_string = telepot.glance(msg, flavor = "inline_query")
        def compute_answer():
            bank = [{"type": "article", "id": "/start", "title": "/start", "description": "Starts the bot in this chat", "message_text": "/start"},
                    {"type": "article", "id": "/help", "title": "/help", "description": "Displays help sheet for @tgchessbot", "message_text": "/help"},
                    {"type": "article", "id": "/stats", "title": "/stats", "description": "Displays your match statistics with @tgchessbot", "message_text": "/stats"}]
            ans = [opt for opt in bank if query_string in opt["id"]]
            for opt in bank:
                print(query_string, opt["id"], query_string in opt["id"])
            return ans

        self._answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        '''Just logs the message. Does nothing for now'''
        self.msglog.append(msg)
        print(msg)    



# MAIN

telegram_bot_token = "aqui va el token"
bot = baduk_bot(telegram_bot_token)

# For server log
print("Bot is online: ", bot.getMe())
bot.message_loop()
print("Listening...")

# Keep the program running.
while 1:
    time.sleep(10)
    bot.save_state() # Save state periodically
