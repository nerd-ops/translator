# code by nerd ops

from translate import Translator # 

from_lang = input("ur language  (example : en) : ")
to_lang = input("the language you want to pass it to (example : es): ")

config_var = Translator(from_lang=from_lang ,to_lang=to_lang)

text = input("\ninput ur text ...\n")

print(f"\n[FINAL]\n{str(config_var.translate(text)).lower()}")
