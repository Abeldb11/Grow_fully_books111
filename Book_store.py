import os
from typing import Final
from telegram import (
    Update, 
    ReplyKeyboardMarkup
)
from telegram.ext import Application, ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters, CallbackQueryHandler
Token: Final = '7682139916:AAG6bjUzxZcUv7Tg4ajrBytMCFEdq1WuA8I'
BOT_USERNAME: Final = '@Grow_to_wholeness_bot'

# Define menus
main_menu = [['AI'], ['Psychology'], ['Philosophy'], ['Self-help'], ['Business'], ['Biography and Almanack']]
ai_menu = [['AI Basics'], ['AI News'], ['Back']]

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text("Main Menu:", reply_markup=markup)

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'AI':
    # List of file paths and their captions (optional)
      files = [
        ('Kurzweil, Ray - The Singularity Is Near.pdf'),
        ('The_Coming_Wave_By_Mustafa_SuleymanMichael_Bhaskar_pdfread_net.pdf'),
        ('Quantum Supremacy By Michio Kaku-pdfread.net.pdf'),
        ('Nexus PDF.pdf'),
        ('2084 by John C. Lennox (z-lib.org).epub.pdf')
    ]

      for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    filename=file_path.split('/')[-1])
                
        except Exception as e:
            await update.message.reply_text(f"Failed to send {file_path}: {e}")


    if text == 'Psychology':
    # List of file paths and their captions (optional)
      files = [
        ('48 Laws of Power, The - Robert Greene.pdf'),
        ('Social_Intelligence_The_New_Science_of_Human_Relationships_Daniel.pdf'),
        ('The Denial of Death.pdf'),
        ('The Psychology of Persuasion.pdf'),
        ('The Road Less Traveled.pdf'),
        ('The Souls Code_ In Search of Character and Calling ( PDFDrive.com ).pdf'),
        ('The-Laws-of-Human-Nature.pdf'),
        ('Steven Pinker The Blank Slate The Modern Denial of Human Nature.pdf'),
        ('12-Rules-for-Life.pdf'),
        ('Man_s Search For Meaning ( PDFDrive.com ).pdf')
    ]

      for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    filename=file_path.split('/')[-1])
                
        except Exception as e:
            await update.message.reply_text(f"Failed to send {file_path}: {e}")

   
    if text == 'Philosophy':
    # List of file paths and their captions (optional)
      files = [
        ('Can Science Explain Everything, John Lennox.pdf'),
        ('Explaining Postmodernism Stephen Hicks.pdf'),
        ('Lord of the Flies by William  Golding (z-lib.org).pdf'),
        ('Beyond good and evil.pdf'),
        ('Nietzsche_OnTheGenealogy.pdf'),
        ('The Master and His Emissary_ The Divided Brain and the Making of the Western World ( PDFDrive ).pdf'),
        ('The Brothers Karamazov (@bookshub25).pdf'),
        ('Crime and Punishment (@bookshub25).pdf'),
        ('Plato_dialogues.pdf'),
        ('Notes_from_Underground_Fyodor_Dostoevsky_Richard_Pevear_Larissa.pdf')
    ]

      for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    filename=file_path.split('/')[-1])
                
        except Exception as e:
            await update.message.reply_text(f"Failed to send {file_path}: {e}")

    
    if text == 'Self-help':
    # List of file paths and their captions (optional)
      files = [
        ('Give-and-Take_-WHY-HELPING-OTHERS-DRIVES-OUR-SUCCESS.pdf'),
        ('mastery-the-keys-to-success-and-long-term-fulfillment_compress.pdf'),
        ('Measure-what-matters.pdf'),
        ('High_Road_Leadership_Bringing_People_Together_in_a_World_That_Divides.pdf'),
        ('How to Win Every Argument ( PDFDrive ).pdf'),
        ('Influence without Authority.pdf'),
        ('Deep Work.pdf'),
        ('simon-sinek-start-with-why.pdf'),
        ('Building a Second Brain By Tiago Forte-pdfread.net.pdf'),
        ('Boundaries_When_to_Say_Yes,_How_to_Say_No_to_Take_Control_of_Your.pdf'),
        ('How to Win Every Argument ( PDFDrive ).pdf'),
        ('Waiting-And-Dating-Myles-MunroeChristiandiet.com_.ng_.pdf')
    ]

      for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    filename=file_path.split('/')[-1])
                
        except Exception as e:
            await update.message.reply_text(f"Failed to send {file_path}: {e}")
    
    if text == 'Business':
    # List of file paths and their captions (optional)
      files = [
        ('Contagious.pdf'),
        ('Made_To_Stick_PDF.pdf'),
        ('thinking in systems.pdf'),
        ('021.pdf'),
        ('Effective Executive ( PDFDrive ).pdf'),
        ('Execution_The_Discipline_of_Getting_Things_Done_PDFDrive_.pdf'),
        ('Finish_what_you_start_the_art_of_following_through,_taking_action.pdf'),
        ('The Art of Profitability.pdf'),
        ('The Lean Startup - Erick Ries.pdf'),
        ('The HOur Between Dog and Wolf.pdf'),
        ('THE_ENTREPRENEURSHIP_JOURNEY.pdf'),
        ('The_Six_Disciplines_of_Strategic_Thinking_Leading_Your_Organization.pdf'),
        ('the-millionaire-fastlane.pdf')
    ]

      for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    filename=file_path.split('/')[-1])
                
        except Exception as e:
            await update.message.reply_text(f"Failed to send {file_path}: {e}")

    if text == 'Biography and Almanack':
    # List of file paths and their captions (optional)
      files = [
        ('A_Promised_Land_by_Barack_Obama.pdf'),
        ('ALSO BY WALTER ISAACSON - English4success ( PDFDrive ).pdf'),
        ('Benjamin_Franklin_An_American_Life_by_Isaacson_Walter_z_lib_PDFDrive.pdf'),
        ('Leonardo da Vinci ( PDFDrive ).pdf'),
        ("Poor Charlies Almanack_ The Wit and Wisdom of Charles T. Munger ( PDFDrive ).pdf"),
        ('poorrichardsalma00franrich.pdf'),
        ('Shoe Dog.pdf'),
        ('story_of_my_life.pdf'),
        ('THE ALMANACK OF NAVAL RAVIKANT.pdf'),
        ('The Innovators (2).pdf'),
        ('1007019.pdf')
    ]

      for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    filename=file_path.split('/')[-1])
                
        except Exception as e:
            await update.message.reply_text(f"Failed to send {file_path}: {e}")



if __name__ == '__main__':
    print('the bot is starting')
    app = ApplicationBuilder().token(Token).build()
    # Set up the bot
    
    
    app.add_handler(CommandHandler("start", start))
    #app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


    app.run_polling(poll_interval= 3)