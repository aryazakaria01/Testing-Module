import os
import textwrap

from PIL import Image, ImageFont, ImageDraw
from LaylaRobot import dispatcher
from LaylaRobot import telethn as bot
from LaylaRobot.events import register as asuna


Credit = "This Plugin Made by Kittu (@A_viyu), if you're using this code in your bot. there is no issue but don't remove this line" 


#@asuna.on_message(filters.command("mmf"))
@asuna(pattern="^/mmf ?(.*)")
async def handler(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("`Reply to an image or a sticker to memify it Nigga!!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.reply("Provide some Text please")
        return
    file = await bot.download_media(reply_message)
    msg = await event.reply("`Memifying this image! Please wait`")

    if "Kittu" in Credit:
       pass

    else: 
       await event.reply("this nigga removed credit line from code")
    text = str(event.pattern_match.group(1)).strip()

    if len(text) < 1:
        return await msg.reply("You might want to try `/mmf text`")
    meme = await drawText(file, text)
    await bot.send_file(event.chat_id, file=meme, force_document=False)   
    await msg.delete()    
    os.remove(meme)



# Taken from https://github.com/UsergeTeam/Userge-Plugins/blob/master/plugins/memify.py#L64
# Maybe replyed to suit the needs of this module

async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    shadowcolor = "black"
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "ariel.ttf"
    else:
        fnt = "./LaylaRobot/resources/MutantAcademyStyle.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ''
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(xy=(((i_width - u_width) / 2) - 2, int((current_h / 640)

                                                             * i_width)), text=u_text, font=m_font, fill=(0, 0, 0))

            draw.text(xy=(((i_width - u_width) / 2) + 2, int((current_h / 640)

                                                             * i_width)), text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=((i_width - u_width) / 2,
                          int(((current_h / 640) * i_width)) - 2),

                      text=u_text,
                      font=m_font,
                      fill=(0,
                            0,
                            0))

            draw.text(xy=(((i_width - u_width) / 2),
                          int(((current_h / 640) * i_width)) + 2),

                      text=u_text,
                      font=m_font,
                      fill=(0,
                            0,
                            0))



            draw.text(xy=((i_width - u_width) / 2, int((current_h / 640)

                                                       * i_width)), text=u_text, font=m_font, fill=(255, 255, 255))

            current_h += u_height + pad

    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, i_height -
                    u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, i_height -
                    u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height -
                                              u_height - int((20 / 640) * i_width)) - 2),
                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(
                xy=((i_width - u_width) / 2, (i_height -

                                              u_height - int((20 / 640) * i_width)) + 2),
                text=l_text, font=m_font, fill=(0, 0, 0))


            draw.text(
                xy=((i_width - u_width) / 2, i_height -
                    u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad          
    image_name = "memify.webp"
    webp_file = os.path.join(image_name)
    img.save(webp_file, "webp")
    return webp_file