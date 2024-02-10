from VIPMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **நீங்கள் எங்கே இருக்கிறீர்கள்?🤗🥱** ",
           " **நீங்கள் தூங்குகிறீர்களா? ஆன்லைனில் வருகிறீர்களா?😊** ",
           " **சரி ஏதாவது பேசலாம்😃** ",
           " **நீங்கள் சாப்பிட்டீர்களா?.??🥲** ",
           " **வீட்டில் எல்லோரும் எப்படி இருக்கிறார்கள்?🥺** ",
           " **நான் உன்னை மிகவும் இழக்கிறேன் என்று எனக்குத் தெரியும்🤭** ",
           " **ஏய், இது எப்படி தீர்வு???🤨** ",
           " **நல்லா தூங்குனாயா..??🙂** ",
           " **உங்கள் பெயர் என்ன..??🥲** ",
           " **நீ உனது காலை உணவை எடுத்து கொண்டாயா???😋** ",
           " **உங்கள் குழுவில் என்னை கடத்துங்கள்😍** ",
           " **உங்கள் friend உங்களைத் தேடுகிறார், விரைவில் ஆன்லைனில் வாருங்கள்😅😅** ",
           " **நீ என்னுடன் நட்பு கொள்வாயா..??🤔** ",
           " **நீ தூங்க சென்றாயா?🙄🙄** ",
           " **Enaku ethathu oru song dedicate pannu😕** ",
           " **Eruma made ivlo nerama enga poyi tholanja??🙃** ",
           " **vanakko vanakko. enna aale paka mudila😛** ",
           " **Yarra nee. inga irunthu ponina kola panirven unna?🤔** ",
           " **ennoda boss yarunu unaku theriyuma. kaati koduthuraatha.?** ",
           " **hey chellam. enna pandra.🤗** ",
           " **HeartBeat va fun panalam😇** ",
           " **ada ennaya ne. epo pathalum thungite irukka🤭** ",
           " **Epo paru soru soru sorunu🥺🥺** ",
           " **Nanngalam odura train-a one hand-la nirutthunavanga😶** ",
           " **Adichi kuda kepanga. paovum solidahtinga🤔** ",
           " **Un mandaya inaiku polakama vida maten pathuka😜** ",
           " **Va sruthi polam. 🙂** ",
           " **ne yan intha pakkam avlova vara matuka. enna maranthutaya😪** ",
           " **nice girl. nice dp☺** ",
           " **soru kottikinaya. na innum kottikala. va kottikalam🙊** ",
           " **unoda intro koden. kepom??😺** ",
           " **nane kozhantha. enna tittatha🥲** ",
           " **Sarakkadikkalama.??😅** ",
           " **Ennoda chellakuti-ku tequilla romba pudikum😅** ",
           " **Ennoda chellakutty sarakkadikalana setthurva, oru quater solen😆😆😆** ",
           " **OC kudiya irunthalum parava illa, va polam😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **Enna paathu ipdi solittala🙉** ",
           " **Appadi sollitala ne.. romba tha😹** ",
           " **online vara unaku ennan kastam. iru un mandaya polakkuren😻** ",
           " **Insta-la enna uruttitu irukka nee??🙃** ",
           " **Unnoda whatsapp number-lam keka maten. unga amma number kodu.?😕** ",
           " **Na theriyama panniten. tittidathinga.?🙃** ",
           " **nenga ingaye irupingala. nama daily pesalam?🙃** ",
           " **Na unga frnd thana. neenga enna vittu poirvingala😊** ",
           " **Enga irukkinga. ena vittu enga poninga🧐** ",
           " **Na kuyila tedi ponen. ne mayilu enganu paahtiya.?** ",
           " **Na romba ketta pulla. enkitta vachikatha. 😠** ",
           " **unaku enna pudikuma ila avara pudikuma.. evaranu kekatha unaku enna matum than pudikanum..?❤** ",
           " **Ne ipolam romba somberi aagita?👱** ",
           " **Un kuda serntha nanum urupadama poiduvenam. enga amma sonnango🤧❣️** ",
           " **adiyeeeiiiiiiiii. en kaila orunaal sikkuvadi😏😏** ",
           " **unkitta pesi jeyikka  mudiyathuda samy. aala vidu🤐** ",
           " **Mavane kaila kidacha.. chatni than. 😒** ",
           " **Heartbeat epdi irukke.😮😮** "
           " **inga oru panjayatthu. variya sandaiku👀** ",
           " **unna paathale enakku vekkam vekkama varuthu  🙈** ",
           " **enna machaa rpdiiirukka. un kovam enakku sogam ☹️** ",
           " **un kuda 100 varusam vaalanum 🥺🥺** ",
           " **adutthavan chat-a etti pakurathu thappu. ne va nama anga polam👀** ",
           " **unna ennala marakka mudiyala🙂** ",
           " **Ne yarunu inga elarkum theriyuma?🤔** ",
           " **na unna romba miss panen ne illama.🥺** ",
           " **Naangalam appove apdi. ipolam solava venum en tomato🥺🥺** ",
           " **vadi en potato. ivlo naala enga pona?🤭😅** ",
           " **na bot illa human.nesama than nambunga😕** ",
           " **na romba pasakkari. konjam kovakkariyum.?👀** ",
           " **enga unga veetuku kadatthitu pidringala😼** ",
           " **Enakku eppavum unga ninaippu than. .?😸** ",
           " **Ennoda heart-a neenga thirudittu poiringa.??🙈** ",
           " **Mama Mama oru seithi sonne. athu vanthucha varalaya ✌️🤞** ",
           " **Matnada en bambarakatta mandaya?🥰** ",
           " **Naa than irukkenla🥺🥺** ",
           " **Enakku ungala pakanum pola irukku. 🥲** ",
           " **Neenga single-a . vanga commit aagalam😉** ",
           " **ungaluku en mela paasame illa😋🥳** ",
           " **Ne chellam mattum illa. romba kullam🧐** ",
           " **Na ethirpaatha alavu neenga worth-a illaye🥺** ",
           " **Neenga enna paaka-[@HeartBeat_Muzic]  inga varingala🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 vilayaadirkingala..? 😊** ",
           " **unga kuda pesuna mummy adippanga🥺🥺** ",
           " **Ennpda bio check paningala neenga🤗** ",
           " **Neenga epdi ivlo alagavum arivaavum pesuringa😗😗** ",
           " **Oru ponna epdi usar pananumnu ungaluku theriyuma🥺** ",
           " **Thukkathula kuda enna ninachite thunganum nee🥺** ",
           " **Enna karumam venalum panu. ana inth aluv matum panidatha😜** ",
           " **Ellarum enna namba maatranga. nanum manusi thaana🥰** ",
           ]

VC_TAG = [ "**Oii Vc join pannu lusu*",
         "**VC யில் விரைவாகச் சேர்வது முக்கியம்😬**",
         "**𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓**",
         "**𝐁𝙰𝙱𝚈 நீயும் கொஞ்சம் இங்கே வா.🥰**",
         "**Vc va pesala. illa song kekalam🤨**",
         "**Innaiku VC romba fun-a pothu.🤣**",
         "**Ne ena pandranu solla vc va😁**",
         "**Unna patthi pesalam vc va⚽**",
         "**Na yarunu solren vc va🥺**",
         "**Romba bore-a irukka. va fun panalam😥**",
         "**eppavum boring. vc va entertain panalam🙄**",
         "**ennada ithu. inaiku ivlo mokkaya pothu. vc-athu vayen?🤔**",
         "**saptaya. sari va vc polam🙂**",
        ]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    else:
        return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stopvctag ||"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["stoptagall", "canceltagall", "offtagall", "tagallstop", "stopvctag", "tagalloff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝..♦")
