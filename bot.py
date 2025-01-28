import re

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from core import msg_count, TOKEN


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    username = update.effective_user.username
    count = msg_count(user_id=user_id, username=username)

    if count:
        await update.message.reply_text(f'Вы отправили {count} сообщений')
    else:
        await update.message.reply_text('Вы еще не отправляли сообщений')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"/stats - статистика сообщений\n/help - это сообщение")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    username = update.effective_user.username
    msg_count(user_id=user_id, username=username)

    message_text = update.message.text.lower().strip()

    if re.search(r'\bпривет\b', message_text):
        await update.message.reply_text('Приветствую! Чем могу помочь?')
    elif re.search(r'\bкак\s*дела\b', message_text):
        await update.message.reply_text('Извините, я пока не умею отвечать на такие вопросы.')
    elif re.search(r'\bпомощь\b', message_text):
        await help_command(update, context)
    else:
        await update.message.reply_text(update.message.text)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(context.error)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.add_error_handler(error_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()