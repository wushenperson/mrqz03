import never_jscore

ctx = never_jscore.Context()
with open("./look_at_me_break.js", 'r', encoding='utf8') as fp:
    ctx.compile(fp.read())
